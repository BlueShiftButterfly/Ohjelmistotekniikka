from game.game_controller import GameController
from game.player import Player
from game.board import Board
from engine.event_relay import EventRelay

class Game:
    def __init__(self):
        self.event_relay = EventRelay()
        self.player1 = Player(self.event_relay, True, Board(10, 10))
        self.player2 = Player(self.event_relay, False, Board(10, 10))
        self.game_controller = GameController(self.player1, self.player2, self.event_relay)
