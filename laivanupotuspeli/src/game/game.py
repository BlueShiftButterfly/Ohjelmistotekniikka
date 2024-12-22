from game.game_controller import GameController
from game.player import Player
from game.ai_player import AIPlayer
from game.board import Board
from engine.event_relay import EventRelay
from game.ship_type import ShipType

class Game:
    def __init__(self):
        self.event_relay = EventRelay()
        self.game_controller = GameController(self.event_relay)
        self.player1 = Player(self.event_relay, True, self.game_controller)
        self.player2 = AIPlayer(self.event_relay, False, self.game_controller)

    def start(self):
        self.game_controller.start(self.player1, self.player2)
