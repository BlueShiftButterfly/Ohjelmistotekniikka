import random
from game.board import Board
from game.player_game_phase import PlayerPhase
from engine.event_relay import EventRelay
from engine.event import Event
from game.abstract_player import AbstractPlayer
from game.guess import Guess
from game.game_controller import GameController
from game.ship import Ship, SHIP_TYPES
from game.direction import Direction

class AIPlayer(AbstractPlayer):
    def __init__(self, event_relay: EventRelay, is_player1: bool, game_controller: GameController):
        self._event_relay = event_relay
        self._is_player11 = is_player1
        self._game_controller = game_controller
        self._cheat = False
        self._event_relay.subscribe(self, self.submit_guess, Event.ON_PLAYER2_SUBMIT_GUESS)

    def request_ships(self, board: Board):
        board.add_ship(Ship(1,8, SHIP_TYPES["2x1"], Direction.VERTICAL))
        board.add_ship(Ship(2,8, SHIP_TYPES["3x1"], Direction.VERTICAL))
        board.add_ship(Ship(3,8, SHIP_TYPES["3x1"], Direction.VERTICAL))
        board.add_ship(Ship(4,8, SHIP_TYPES["4x1"], Direction.VERTICAL))
        print("AI placed ships")
        self._event_relay.call(Event.PLAYER2_FINISHED_PLACING_SHIPS, board)
        self._game_controller.set_player_ships(self._is_player1, board)

    def request_guess(self, board: Board):
        remaining_guesses = []
        for _x in range(10):
            for _y in range(10):
                remaining_guesses.append((_x, _y))
        if self._cheat:
            remaining_guesses = []
            for s in board._ships.values():
                remaining_guesses.extend(s.get_tiles_board_pos())
        for g in board._opponent_guesses.keys():
            remaining_guesses.remove(g)
        #x = random.randint(0, 9)
        #y = random.randint(0, 9)
        chosen_coords = random.choice(remaining_guesses)
        
        if board.is_valid_guess_position(chosen_coords[0], chosen_coords[1]):
            print(f"ai guessed {chosen_coords}")
            self._event_relay.call(Event.PLAYER2_REQUEST_GUESS, chosen_coords)
            #self.game_controller.set_player_guess(self.is_player1, (x, y))
        else:
            self.request_guess(board)

    def submit_guess(self, coords):
        self._game_controller.set_player_guess(self._is_player1, coords)
