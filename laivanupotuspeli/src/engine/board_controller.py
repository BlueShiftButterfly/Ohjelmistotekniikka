import pygame
from game.game import SHIP_TYPES
from game.ship import Ship
from engine.event_relay import EventRelay
from engine.event import Event
from game.board import Board
from engine.game_board_visual import GameBoardVisual
from game.direction import Direction

class BoardController:
    def __init__(self, event_relay: EventRelay, game_board: Board, board_visual: GameBoardVisual) -> None:
        self.event_relay = event_relay
        self.game_board = game_board
        self.board_visual = board_visual
        self.preview_ship_rotation = Direction.VERTICAL
        self.selected_ship_type = None
        self.event_relay.subscribe(self, self.on_ship_rotate, Event.ON_SHIP_ROTATE)
        self.event_relay.subscribe(self, self.on_mouse_press, Event.ON_MOUSE0_PRESS)
        self.event_relay.subscribe(self, self.update, Event.ON_BEFORE_RENDER)

    def update(self):
        if self.selected_ship_type is None:
            return
        s_pos = self.board_visual.screen_to_grid_coords(pygame.mouse.get_pos())
        self.board_visual.draw_ship_preview(self.selected_ship_type, self.preview_ship_rotation, s_pos)

    def on_mouse_press(self):
        if self.selected_ship_type is None:
            return
        s_pos = self.board_visual.screen_to_grid_coords(pygame.mouse.get_pos())
        self.board_visual.preview_ships.append(
            Ship(s_pos[0], s_pos[1], SHIP_TYPES[self.selected_ship_type], self.preview_ship_rotation)
        )

    def on_ship_rotate(self):
        if self.preview_ship_rotation == Direction.VERTICAL:
            self.preview_ship_rotation = Direction.HORIZONTAL
        else:
            self.preview_ship_rotation = Direction.VERTICAL 
