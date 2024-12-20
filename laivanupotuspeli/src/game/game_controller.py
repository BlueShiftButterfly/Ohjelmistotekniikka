from game.player import Player
from engine.event_relay import EventRelay
from engine.event import Event
from game.player_game_phase import PlayerPhase

class GameController:
    def __init__(self, player1: Player, player2: Player, event_relay: EventRelay):
        self.player1 = player1
        self.player2 = player2
        self.game_event_relay = event_relay
        self.game_event_relay.subscribe(self, self.on_player_finish_ship_placement, Event.PLAYER1_FINISHED_PLACING_SHIPS)
        self.game_event_relay.subscribe(self, self.on_player_finish_ship_placement, Event.PLAYER2_FINISHED_PLACING_SHIPS)

    def begin_ship_placement_phase(self):
        self.game_event_relay.call(Event.ROUND_START_SHIP_PLACEMENT)

    def on_player_finish_ship_placement(self):
        if (
            self.player1.current_phase == PlayerPhase.WAITING_FOR_GUESS_BEGIN# and
            #self.player2.current_phase == PlayerPhase.WAITING_FOR_GUESS_BEGIN
        ):
            self.start_player_turn(True)

    def start_player_turn(self, is_player1_turn: bool):
        if is_player1_turn:
            self.game_event_relay.call(Event.PLAYER1_START_GUESS)
        else:
            self.game_event_relay.call(Event.PLAYER2_START_GUESS)
