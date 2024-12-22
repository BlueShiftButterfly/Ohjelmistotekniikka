from game.board import Board
from game.abstract_player import AbstractPlayer
from game.game_controller import GameController
from engine.event_relay import EventRelay
from engine.event import Event

class Player(AbstractPlayer):
    def __init__(self, event_relay: EventRelay, is_player1: bool, game_controller: GameController):
        self._event_relay = event_relay
        self._is_player1 = is_player1
        self._game_controller = game_controller
        self._event_relay.subscribe(self, self.on_finished_placing, Event.ON_USER_CONFIRM_PLACEMENT)
        self._event_relay.subscribe(self, self.on_player_guess, Event.ON_PLAYER1_SUBMIT_GUESS)

    def request_ships(self, board: Board):
        self._event_relay.call(Event.PLAYER1_REQUEST_SHIP_PLACEMENT, board)

    def on_finished_placing(self, board):
        self._game_controller.set_player_ships(self._is_player1, board)

    def request_guess(self, board: Board):
        self._event_relay.call(Event.PLAYER1_REQUEST_GUESS)

    def on_player_guess(self, coords):
        self._game_controller.set_player_guess(self._is_player1, coords)
