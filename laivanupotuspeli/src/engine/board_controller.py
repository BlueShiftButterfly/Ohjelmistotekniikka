import random
import pygame
from game.ship import Ship, SHIP_TYPES
from engine.event_relay import EventRelay
from engine.event import Event
from game.board import Board
from engine.game_board_visual import GameBoardVisual
from game.direction import Direction
from engine.rendering import colors

class BoardController:
    def __init__(self, event_relay: EventRelay, board_visual: GameBoardVisual, is_player1: bool = True) -> None:
        self._event_relay = event_relay
        self._game_board: Board = None
        self._board_visual = board_visual
        self._preview_ship_rotation = Direction.VERTICAL
        self._selected_ship_type = None
        self._is_placing_ships = False
        self._is_player1 = is_player1
        self._can_place_guess = False
        self._event_relay.subscribe(self, self.update, Event.ON_RENDER)
        self._event_relay.subscribe(self, self.on_left_click, Event.ON_MOUSE0_PRESS)
        self._event_relay.subscribe(self, self.on_right_click, Event.ON_MOUSE1_PRESS)
        self._event_relay.subscribe(self, self.on_user_request_guess, Event.PLAYER1_REQUEST_GUESS)
        self._event_relay.subscribe(self, self.on_player2_request_guess, Event.PLAYER2_REQUEST_GUESS)
        if is_player1:
            self._event_relay.subscribe(self, self.on_ship_rotate, Event.ON_SHIP_ROTATE)
            self._event_relay.subscribe(self, self.on_select_ship_type, Event.ON_SELECT_SHIP_TYPE)
            self._event_relay.subscribe(self, self.on_confirm_placement, Event.ON_CONFIRM_SHIP_BUTTON)
            self._event_relay.subscribe(self, self.on_request_ship_placement, Event.PLAYER1_REQUEST_SHIP_PLACEMENT)
            self._event_relay.subscribe(self, self.on_update_board, Event.UPDATE_PLAYER1_BOARD)
        else:
            self._event_relay.subscribe(self, self.set_board, Event.PLAYER2_FINISHED_PLACING_SHIPS)
            self._event_relay.subscribe(self, self.on_update_board, Event.UPDATE_PLAYER2_BOARD)
        
        self._cooldown = 0
        self._ai_coords = None
        self._post_ai_cooldown = 0

    def on_request_ship_placement(self, board: Board):
        self._is_placing_ships = True
        self._game_board = board

    def set_board(self, board: Board):
        self._game_board = board
        self._board_visual.board_ships = list(self._game_board.ships.values())

    def update(self, delta: float):
        if self._cooldown > 0:
            self._cooldown -= 1
            if self._cooldown == 0 and self._ai_coords is not None:
                if self._game_board.would_hit_ship(self._ai_coords[0], self._ai_coords[1]):
                    self._board_visual.hit_markers.append(self._ai_coords)
                else:
                    self._board_visual.miss_markers.append(self._ai_coords)
                self._post_ai_cooldown = 60
        if self._post_ai_cooldown > 0:
            self._post_ai_cooldown -= 1
            if self._post_ai_cooldown == 0:
                self._event_relay.call(Event.ON_PLAYER2_SUBMIT_GUESS, self._ai_coords)
        if self._board_visual.enabled is False:
            return
        if self._is_player1 is True:
            if self._selected_ship_type is None or self._is_placing_ships is False:
                return
            if self._game_board.has_ship_type_left(SHIP_TYPES[self._selected_ship_type]) is False:
                self._selected_ship_type = None
                return
            s_pos = self._board_visual.screen_to_grid_coords(pygame.mouse.get_pos())
            preview_ship = Ship(s_pos[0], s_pos[1], SHIP_TYPES[self._selected_ship_type], self._preview_ship_rotation)
            if self._game_board.is_valid_ship_placement(preview_ship) is True:
                self._board_visual.draw_ship_preview(self._selected_ship_type, self._preview_ship_rotation, s_pos)
        else:
            s_pos = self._board_visual.screen_to_grid_coords(pygame.mouse.get_pos())
            self._board_visual.highlight_square(s_pos, colors.WHITE)

    def on_left_click(self):
        if self._board_visual.enabled is False:
            return
        if self._is_player1 is True:
            if self._is_placing_ships is False:
                return
            if self._selected_ship_type is None:
                return
            if self._game_board.has_ship_type_left(SHIP_TYPES[self._selected_ship_type]) is False:
                self._selected_ship_type = None
                return
            s_pos = self._board_visual.screen_to_grid_coords(pygame.mouse.get_pos())
            preview_ship = Ship(s_pos[0], s_pos[1], SHIP_TYPES[self._selected_ship_type], self._preview_ship_rotation)
            if self._game_board.is_valid_ship_placement(preview_ship) is False:
                return
            if self._game_board.add_ship(preview_ship):
                self._board_visual.board_ships = list(self._game_board.ships.values())
        else:
            if self._can_place_guess is False:
                return
            s_pos = self._board_visual.screen_to_grid_coords(pygame.mouse.get_pos())
            if self._game_board.is_valid_guess_position(s_pos[0], s_pos[1]):
                self._can_place_guess = False
                self._event_relay.call(Event.ON_PLAYER1_SUBMIT_GUESS, s_pos)

    def on_right_click(self):
        if self._board_visual.enabled is False:
            return
        if self._is_player1 is False:
            return
        if self._is_placing_ships is False:
            return
        s_pos = self._board_visual.screen_to_grid_coords(pygame.mouse.get_pos())
        self._game_board.try_remove_ship_at_position(s_pos)
        self._board_visual.board_ships = list(self._game_board.ships.values())

    def on_ship_rotate(self):
        if self._board_visual.enabled is False:
            return
        if self._is_placing_ships is False:
            return
        if self._preview_ship_rotation == Direction.VERTICAL:
            self._preview_ship_rotation = Direction.HORIZONTAL
        else:
            self._preview_ship_rotation = Direction.VERTICAL 

    def on_select_ship_type(self, ship_type: str):
        if self._board_visual.enabled is False:
            return
        if self._is_placing_ships is False:
            return
        self._selected_ship_type = ship_type

    def on_confirm_placement(self):
        if self._board_visual.enabled is False:
            return
        if self._is_placing_ships is False:
            return
        if self._game_board.placed_all_ships():
            self._selected_ship_type = None
            self._is_placing_ships = False
            self._event_relay.call(Event.ON_USER_CONFIRM_SHIP_PLACEMENT, self._game_board)

    def on_user_request_guess(self):
        if self._is_player1:
            self._board_visual.enabled = False
        else:
            self._board_visual.enabled = True
            self._can_place_guess = True

    def on_player2_guess(self, coords):
        if self._is_player1:
            self._board_visual.enabled = True
        else:
            self._board_visual.enabled = False

    def on_player2_request_guess(self, coords):
        
        self._cooldown = 0
        self._post_ai_cooldown = 0
        self._ai_coords = None
        if self._is_player1:
            self._cooldown = random.randint(20, 120)
            self._board_visual.enabled = True
            self._ai_coords = coords
        else:
            self._board_visual.enabled = False

    def on_update_board(self, board):
        self._game_board = board
        self._board_visual.board_ships = list(self._game_board.ships.values())
        self._board_visual.hit_markers = []
        self._board_visual.miss_markers = []
        for g in self._game_board.opponent_guesses.values():
            if g.hit_ship:
                self._board_visual.hit_markers.append((g.x, g.y))
            else:
                self._board_visual.miss_markers.append((g.x, g.y))
