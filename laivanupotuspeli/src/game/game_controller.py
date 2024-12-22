from game.abstract_player import AbstractPlayer
from engine.event_relay import EventRelay
from engine.event import Event
from game.player_game_phase import PlayerPhase
from game.board import Board

class GameController:
    def __init__(self, event_relay: EventRelay):
        self.event_relay = event_relay
        self.player1:AbstractPlayer = None
        self.player1_board: Board = None
        self.player2:AbstractPlayer = None
        self.player2_board: Board = None

    def start(self, player1:AbstractPlayer, player2:AbstractPlayer):
        self.player1 = player1
        self.player2 = player2
        self.player1.request_ships(Board(10, 10))
        self.player2.request_ships(Board(10, 10))

    def set_player_ships(self, is_player1, board):
        if is_player1:
            self.player1_board = board
        else:
            self.player2_board = board
        if self.player1_board is not None and self.player2_board is not None:
            #for s in self.player2_board.ships.values():
            #    s._hit_tiles_count = 100
            #    s.is_sunk = True
            self.player1.request_guess(self.player2_board)

    def set_player_guess(self, is_player1, coords):
        if is_player1:
            self.player2_board.add_guess(coords[0], coords[1])
            if self.player2_board._opponent_guesses[coords].hit_ship:
                print("PLAYER 1 HIT!")
                if self.player2_board.has_unsunk_ships_left():
                    self.player1.request_guess(self.player2_board)
                else:
                    print("PLAYER 1 WINS!!!")
                    self.event_relay.call(Event.ON_PLAYER1_WIN)
            else:
                print("PLAYER 1 MISS!")
                self.player2.request_guess(self.player1_board)
            self.event_relay.call(Event.UPDATE_PLAYER2_BOARD, self.player2_board)
        else:
            self.player1_board.add_guess(coords[0], coords[1])
            if self.player1_board._opponent_guesses[coords].hit_ship:
                print("PLAYER 2 HIT!")
                if self.player1_board.has_unsunk_ships_left():
                    self.player2.request_guess(self.player1_board)
                else:
                    print("PLAYER 2 WINS!!!")
                    self.event_relay.call(Event.ON_PLAYER2_WIN)
            else:
                print("PLAYER 2 MISS!")
                self.player1.request_guess(self.player2_board)
            self.event_relay.call(Event.UPDATE_PLAYER1_BOARD, self.player1_board)
