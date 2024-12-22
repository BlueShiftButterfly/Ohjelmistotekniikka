import pygame
from game.ship import Ship, SHIP_TYPES
from engine.event_relay import EventRelay
from engine.event import Event
from game.board import Board
from engine.game_board_visual import GameBoardVisual
from game.direction import Direction

class BoardController:
    def __init__(self, event_relay: EventRelay, game_board: Board, board_visual: GameBoardVisual, is_player1: bool = True) -> None:
        self.event_relay = event_relay
        self.game_board = game_board
        self.board_visual = board_visual
        self.preview_ship_rotation = Direction.VERTICAL
        self.selected_ship_type = None
        self.is_placing_ships = True
        self.event_relay.subscribe(self, self.on_ship_rotate, Event.ON_SHIP_ROTATE)
        self.event_relay.subscribe(self, self.on_left_click, Event.ON_MOUSE0_PRESS)
        self.event_relay.subscribe(self, self.on_right_click, Event.ON_MOUSE1_PRESS)
        self.event_relay.subscribe(self, self.update, Event.ON_RENDER)
        self.event_relay.subscribe(self, self.on_select_ship_type, Event.ON_SELECT_SHIP_TYPE)
        self.event_relay.subscribe(self, self.on_confirm_placement, Event.ON_CONFIRM_SHIP_BUTTON)
        self.event_relay.subscribe(self, self.on_player1_guess, Event.PLAYER1_START_GUESS)

    def update(self, delta: float):
        if self.selected_ship_type is None or self.is_placing_ships is False:
            return
        if self.game_board.has_ship_type_left(SHIP_TYPES[self.selected_ship_type]) is False:
            self.selected_ship_type = None
            return
        s_pos = self.board_visual.screen_to_grid_coords(pygame.mouse.get_pos())
        preview_ship = Ship(s_pos[0], s_pos[1], SHIP_TYPES[self.selected_ship_type], self.preview_ship_rotation)
        if self.game_board.is_valid_ship_placement(preview_ship) is True:
            self.board_visual.draw_ship_preview(self.selected_ship_type, self.preview_ship_rotation, s_pos)

    def on_left_click(self):
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

    def on_right_click(self):
        if self.is_placing_ships is False:
            return
        s_pos = self.board_visual.screen_to_grid_coords(pygame.mouse.get_pos())
        self.game_board.try_remove_ship_at_position(s_pos)
        self.board_visual.board_ships = list(self.game_board.ships.values())

    def on_ship_rotate(self):
        if self.is_placing_ships is False:
            return
        if self.preview_ship_rotation == Direction.VERTICAL:
            self.preview_ship_rotation = Direction.HORIZONTAL
        else:
            self.preview_ship_rotation = Direction.VERTICAL 

    def on_select_ship_type(self, ship_type: str):
        if self.is_placing_ships is False:
            return
        self.selected_ship_type = ship_type

    def on_confirm_placement(self):
        if self.is_placing_ships is False:
            return
        if self.game_board.placed_all_ships():
            self.selected_ship_type = None
            self.is_placing_ships = False
            self.event_relay.call(Event.ON_USER_CONFIRM_SHIP_PLACEMENT)

    def on_player1_guess(self):
        self.board_visual.enabled = not self.board_visual.enabled

    def on_player2_guess(self):
        pass