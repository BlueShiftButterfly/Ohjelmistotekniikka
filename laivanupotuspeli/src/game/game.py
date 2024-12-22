from game.game_controller import GameController
from game.player import Player
from game.ai_player import AIPlayer
from engine.event_relay import EventRelay

class Game:
    """
    Game is a top level class that wraps all of the game related objects.
    """
    def __init__(self):
        self.event_relay = EventRelay()
        self._game_controller = GameController(self.event_relay)
        self._player1 = Player(self.event_relay, True, self._game_controller)
        self._player2 = AIPlayer(self.event_relay, False, self._game_controller)

    def start(self):
        """
        Starts the game of Battleship
        """
        self._game_controller.start(self._player1, self._player2)
