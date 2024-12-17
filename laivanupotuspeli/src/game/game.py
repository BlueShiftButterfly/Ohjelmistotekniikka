from game.game_controller import GameController
from game.player import Player
from game.board import Board
from engine.event_relay import EventRelay
from game.ship_type import ShipType

SHIP_TYPES = {
    "2x1": ShipType([(0, 0), (1, 0)], [(0, 0), (0, 1)], "2x1"),
    "3x1": ShipType([(0, 0), (1, 0), (2, 0)], [(0, 0), (0, 1), (0, 2)], "3x1"),
    "4x1": ShipType([(0, 0), (1, 0), (2, 0), (3, 0)], [(0, 0), (0, 1), (0, 2), (0, 3)], "4x1"),
}


class Game:
    def __init__(self):
        self.event_relay = EventRelay()
        self.player1 = Player(self.event_relay, True, Board(10, 10))
        self.player2 = Player(self.event_relay, False, Board(10, 10))
        self.game_controller = GameController(self.player1, self.player2, self.event_relay)
