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
        self.event_relay = event_relay
        self.is_player1 = is_player1
        self.game_controller = game_controller
        self.event_relay.subscribe(self, self.submit_guess, Event.ON_PLAYER2_SUBMIT_GUESS)

    def request_ships(self, board: Board):
        board.add_ship(Ship(1,8, SHIP_TYPES["2x1"], Direction.VERTICAL))
        board.add_ship(Ship(2,8, SHIP_TYPES["3x1"], Direction.VERTICAL))
        board.add_ship(Ship(3,8, SHIP_TYPES["3x1"], Direction.VERTICAL))
        board.add_ship(Ship(4,8, SHIP_TYPES["4x1"], Direction.VERTICAL))
        print("AI placed ships")
        self.event_relay.call(Event.PLAYER2_FINISHED_PLACING_SHIPS, board)
        self.game_controller.set_player_ships(self.is_player1, board)

    def request_guess(self, board: Board):
        
        x = random.randint(0, 9)
        y = random.randint(0, 9)
        if board.is_valid_guess_position(x, y):
            print(f"ai guessed {x} {y}")
            self.event_relay.call(Event.PLAYER2_REQUEST_GUESS, (x, y))
            #self.game_controller.set_player_guess(self.is_player1, (x, y))
        else:
            self.request_guess(board)

    def submit_guess(self, coords):
        self.game_controller.set_player_guess(self.is_player1, coords)