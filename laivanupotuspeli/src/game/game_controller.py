from game.player import Player
from engine.event_relay import EventRelay
from engine.event import Event

class GameController:
    def __init__(self, player1: Player, player2: Player):
        self.player1 = player1
        self.player2 = player2
        self.game_event_relay = EventRelay()
        self.game_event_relay.subscribe(self, self.on_player_end_placement_phase, Event.PLAYER1_FINISHED_PLACING_SHIPS)
        self.game_event_relay.subscribe(self, self.on_player_end_placement_phase, Event.PLAYER2_FINISHED_PLACING_SHIPS)

    def begin_ship_placement_phase(self):
        self.game_event_relay.call(Event.ROUND_START_SHIP_PLACEMENT)

    def on_player_end_placement_phase(self):
        pass
