from game.board import Board
from game.player_game_phase import PlayerPhase
from engine.event_relay import EventRelay
from engine.event import Event

class Player:
    def __init__(self, event_relay: EventRelay, is_player1: bool, board: Board):
        self.event_relay = event_relay
        self.is_player1 = is_player1
        self.board = board
        self.current_phase = PlayerPhase.WAIT_SHIP_PLACEMENT
        self.event_relay.subscribe(self, self.start_ship_placement, Event.ROUND_START_SHIP_PLACEMENT)

    def start_ship_placement(self):
        self.current_phase = PlayerPhase.PLACING_SHIPS

    def finish_ship_placement(self):
        self.current_phase = PlayerPhase.WAITING_FOR_GUESS_BEGIN
        event_to_call = Event.PLAYER1_FINISHED_PLACING_SHIPS
        if self.is_player1 is False:
            event_to_call = Event.PLAYER2_FINISHED_PLACING_SHIPS
        self.event_relay.call(event_to_call)
