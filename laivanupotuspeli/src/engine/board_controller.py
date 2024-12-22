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
        self.event_relay = event_relay
        self.game_board: Board = None
        self.board_visual = board_visual
        self.preview_ship_rotation = Direction.VERTICAL
        self.selected_ship_type = None
        self.is_placing_ships = False
        self.is_player1 = is_player1
        self.can_place_guess = False
        self.event_relay.subscribe(self, self.update, Event.ON_RENDER)
        self.event_relay.subscribe(self, self.on_left_click, Event.ON_MOUSE0_PRESS)
        self.event_relay.subscribe(self, self.on_right_click, Event.ON_MOUSE1_PRESS)
        self.event_relay.subscribe(self, self.on_user_request_guess, Event.PLAYER1_REQUEST_GUESS)
        self.event_relay.subscribe(self, self.on_player2_request_guess, Event.PLAYER2_REQUEST_GUESS)
        if is_player1:
            self.event_relay.subscribe(self, self.on_ship_rotate, Event.ON_SHIP_ROTATE)
            self.event_relay.subscribe(self, self.on_select_ship_type, Event.ON_SELECT_SHIP_TYPE)
            self.event_relay.subscribe(self, self.on_confirm_placement, Event.ON_CONFIRM_SHIP_BUTTON)
            self.event_relay.subscribe(self, self.on_request_ship_placement, Event.PLAYER1_REQUEST_SHIP_PLACEMENT)
            self.event_relay.subscribe(self, self.on_update_board, Event.UPDATE_PLAYER1_BOARD)
        else:
            #self.event_relay.subscribe(self, self.on_player2_guess, Event.ON_PLAYER2_SUBMIT_GUESS)
            self.event_relay.subscribe(self, self.set_board, Event.PLAYER2_FINISHED_PLACING_SHIPS)
            self.event_relay.subscribe(self, self.on_update_board, Event.UPDATE_PLAYER2_BOARD)
        
        self.cooldown = 0
        self.ai_coords = None
        self.post_ai_cooldown = 0

    def on_request_ship_placement(self, board: Board):
        self.is_placing_ships = True
        self.game_board = board

    def set_board(self, board: Board):
        self.game_board = board
        self.board_visual.board_ships = list(self.game_board.ships.values())

    def update(self, delta: float):
        if self.cooldown > 0:
            print(f"COOLDOWN {self.cooldown}")
            print(self.ai_coords)
            self.cooldown -= 1
            if self.cooldown == 0 and self.ai_coords is not None:
                print("P2 FAKE GUESS")
                if self.game_board.would_hit_ship(self.ai_coords[0], self.ai_coords[1]):
                    self.board_visual.hit_markers.append(self.ai_coords)
                else:
                    self.board_visual.miss_markers.append(self.ai_coords)
                self.post_ai_cooldown = 60
        if self.post_ai_cooldown > 0:
            print(f"POST AI COOLDOWN {self.post_ai_cooldown}")
            self.post_ai_cooldown -= 1
            if self.post_ai_cooldown == 0:
                print("P2 CONFIRM GUESS")
                #self.ai_coords = None
                self.event_relay.call(Event.ON_PLAYER2_SUBMIT_GUESS, self.ai_coords)
        if self.board_visual.enabled is False:
            return
        if self.is_player1 is True:
            if self.selected_ship_type is None or self.is_placing_ships is False:
                return
            if self.game_board.has_ship_type_left(SHIP_TYPES[self.selected_ship_type]) is False:
                self.selected_ship_type = None
                return
            s_pos = self.board_visual.screen_to_grid_coords(pygame.mouse.get_pos())
            preview_ship = Ship(s_pos[0], s_pos[1], SHIP_TYPES[self.selected_ship_type], self.preview_ship_rotation)
            if self.game_board.is_valid_ship_placement(preview_ship) is True:
                self.board_visual.draw_ship_preview(self.selected_ship_type, self.preview_ship_rotation, s_pos)
        else:
            s_pos = self.board_visual.screen_to_grid_coords(pygame.mouse.get_pos())
            self.board_visual.highlight_square(s_pos, colors.WHITE)

    def on_left_click(self):
        if self.board_visual.enabled is False:
            return
        if self.is_player1 is True:
            if self.is_placing_ships is False:
                return
            if self.selected_ship_type is None:
                return
            if self.game_board.has_ship_type_left(SHIP_TYPES[self.selected_ship_type]) is False:
                self.selected_ship_type = None
                return
            s_pos = self.board_visual.screen_to_grid_coords(pygame.mouse.get_pos())
            preview_ship = Ship(s_pos[0], s_pos[1], SHIP_TYPES[self.selected_ship_type], self.preview_ship_rotation)
            if self.game_board.is_valid_ship_placement(preview_ship) is False:
                return
            if self.game_board.add_ship(preview_ship):
                self.board_visual.board_ships = list(self.game_board.ships.values())
        else:
            if self.can_place_guess is False:
                return
            s_pos = self.board_visual.screen_to_grid_coords(pygame.mouse.get_pos())
            if self.game_board.is_valid_guess_position(s_pos[0], s_pos[1]):
                self.can_place_guess = False
                self.event_relay.call(Event.ON_PLAYER1_SUBMIT_GUESS, s_pos)

    def on_right_click(self):
        if self.board_visual.enabled is False:
            return
        if self.is_player1 is False:
            return
        if self.is_placing_ships is False:
            return
        s_pos = self.board_visual.screen_to_grid_coords(pygame.mouse.get_pos())
        self.game_board.try_remove_ship_at_position(s_pos)
        self.board_visual.board_ships = list(self.game_board.ships.values())

    def on_ship_rotate(self):
        if self.board_visual.enabled is False:
            return
        if self.is_placing_ships is False:
            return
        if self.preview_ship_rotation == Direction.VERTICAL:
            self.preview_ship_rotation = Direction.HORIZONTAL
        else:
            self.preview_ship_rotation = Direction.VERTICAL 

    def on_select_ship_type(self, ship_type: str):
        if self.board_visual.enabled is False:
            return
        if self.is_placing_ships is False:
            return
        self.selected_ship_type = ship_type

    def on_confirm_placement(self):
        if self.board_visual.enabled is False:
            return
        if self.is_placing_ships is False:
            return
        if self.game_board.placed_all_ships():
            self.selected_ship_type = None
            self.is_placing_ships = False
            self.event_relay.call(Event.ON_USER_CONFIRM_SHIP_PLACEMENT, self.game_board)

    def on_user_request_guess(self):
        if self.is_player1:
            self.board_visual.enabled = False
        else:
            self.board_visual.enabled = True
            self.can_place_guess = True

    def on_player2_guess(self, coords):
        print("P2 GUESS")
        if self.is_player1:
            #self.cooldown = 60
            self.board_visual.enabled = True
        else:
            self.board_visual.enabled = False

    def on_player2_request_guess(self, coords):
        
        self.cooldown = 0
        self.post_ai_cooldown = 0
        self.ai_coords = None
        if self.is_player1:
            print(f"BOARD REQUEST P2 GUESS {coords}")
            self.cooldown = random.randint(20, 120)
            self.board_visual.enabled = True
            self.ai_coords = coords
            print(f"AI COORDS {self.ai_coords}")
        else:
            self.board_visual.enabled = False

    def on_update_board(self, board):
        self.game_board = board
        self.board_visual.board_ships = list(self.game_board.ships.values())
        self.board_visual.hit_markers = []
        self.board_visual.miss_markers = []
        for g in self.game_board.opponent_guesses.values():
            if g.hit_ship:
                self.board_visual.hit_markers.append((g.x, g.y))
            else:
                self.board_visual.miss_markers.append((g.x, g.y))
