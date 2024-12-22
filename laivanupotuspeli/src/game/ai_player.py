import random
from game.abstract_player import AbstractPlayer
from game.board import Board
from game.game_controller import GameController
from game.ship import Ship, SHIP_TYPES
from game.direction import Direction
from engine.event import Event
from engine.event_relay import EventRelay

class AIPlayer(AbstractPlayer):
    """
    Class responsible for opponent AI behaviour.
    """
    def __init__(self, event_relay: EventRelay, is_player1: bool, game_controller: GameController):
        """
        Args:
            event_relay: event_relay object for event based communication
            is_player1: Is AI player1
            game_controller: Game Controller object that controls the flow of the game
        """
        self._event_relay = event_relay
        self._is_player1 = is_player1
        self._game_controller = game_controller
        self._cheat = False
        self._event_relay.subscribe(self, self.submit_guess, Event.ON_PLAYER2_SUBMIT_GUESS)

    def request_ships(self, board: Board):
        for _ in range(100):
            if board.add_ship(Ship(
                random.randint(0, 9),
                random.randint(0, 9),
                SHIP_TYPES["2x1"],
                random.randint(0, 1)
            )):
                break
        for _ in range(100):
            if board.add_ship(Ship(
                random.randint(0, 9),
                random.randint(0, 9),
                SHIP_TYPES["3x1"],
                random.randint(0, 1)
            )):
                break
        for _ in range(100):
            if board.add_ship(Ship(
                random.randint(0, 9),
                random.randint(0, 9),
                SHIP_TYPES["3x1"],
                random.randint(0, 1)
            )):
                break
        for _ in range(100):
            if board.add_ship(Ship(
                random.randint(0, 9),
                random.randint(0, 9),
                SHIP_TYPES["4x1"],
                random.randint(0, 1)
            )):
                break
        self._event_relay.call(Event.PLAYER2_FINISHED_PLACING_SHIPS, board)
        self._game_controller.set_player_ships(self._is_player1, board)

    def request_guess(self, board: Board):
        remaining_guesses = []
        for _x in range(10):
            for _y in range(10):
                remaining_guesses.append((_x, _y))
        if self._cheat:
            remaining_guesses = []
            for s in board.ships.values():
                remaining_guesses.extend(s.get_tiles_board_pos())
        for g in board.opponent_guesses.keys():
            remaining_guesses.remove(g)
        chosen_coords = random.choice(remaining_guesses)

        if board.is_valid_guess_position(chosen_coords[0], chosen_coords[1]):
            self._event_relay.call(Event.PLAYER2_REQUEST_GUESS, chosen_coords)
        else:
            self.request_guess(board)

    def submit_guess(self, coords):
        self._game_controller.set_player_guess(self._is_player1, coords)
