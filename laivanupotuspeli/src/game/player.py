from game.board import Board
from game.player_game_phase import PlayerPhase
from engine.event_relay import EventRelay
from engine.event import Event
from game.abstract_player import AbstractPlayer
from game.guess import Guess
from game.game_controller import GameController
from game.ship import Ship, SHIP_TYPES
from game.direction import Direction

class Player(AbstractPlayer):
    def __init__(self, event_relay: EventRelay, is_player1: bool, game_controller: GameController):
        self.event_relay = event_relay
        self.is_player1 = is_player1
        self.game_controller = game_controller
        self.event_relay.subscribe(self, self.on_finished_placing_ships, Event.ON_USER_CONFIRM_SHIP_PLACEMENT)
        self.event_relay.subscribe(self, self.on_player_guess, Event.ON_PLAYER1_SUBMIT_GUESS)

    def request_ships(self, board: Board):
        #board.add_ship(Ship(1,8, SHIP_TYPES["2x1"], Direction.VERTICAL))
        #board.add_ship(Ship(2,8, SHIP_TYPES["3x1"], Direction.VERTICAL))
        #board.add_ship(Ship(3,8, SHIP_TYPES["3x1"], Direction.VERTICAL))
        #board.add_ship(Ship(4,8, SHIP_TYPES["4x1"], Direction.VERTICAL))
        #input("press enter to continue player ship placing phase")
        #self.game_controller.set_player_ships(self.is_player1, board)
        self.event_relay.call(Event.PLAYER1_REQUEST_SHIP_PLACEMENT, board)

    def on_finished_placing_ships(self, board):
        self.game_controller.set_player_ships(self.is_player1, board)

    def request_guess(self, board: Board):
        #x = int(input("enter x coordinate for guess: "))
        #y = int(input("enter y coordinate for guess: "))
        #if board.is_valid_guess_position(x, y):
        #    print(f"you guessed {x} {y}")
        #    self.game_controller.set_player_guess(self.is_player1, (x, y))
        self.event_relay.call(Event.PLAYER1_REQUEST_GUESS)

    def on_player_guess(self, coords):
        self.game_controller.set_player_guess(self.is_player1, coords)
