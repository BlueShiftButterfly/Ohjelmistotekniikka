import pygame_gui
from engine.rendering.abstract_display import AbstractDisplay
from engine.event_relay import EventRelay
from engine.event import Event
from engine.rendering.gui_holder import GUIHolder

class GUIRenderer:
    """
    Class responsible for GUI rendering in-game.
    """
    def __init__(self, event_relay: EventRelay, display: AbstractDisplay):
        """
        Args:
            event_relay: event_relay object for event based communication
            display: pygame display wrapper object
        """
        self._display = display
        self._event_relay = event_relay

        self._pygame_events = None
        self._manager = pygame_gui.UIManager(self._display.resolution, "src/assets/theme.json")
        self._ui_holder = GUIHolder(self._event_relay, self._manager)

        self._event_relay.subscribe(self, self.get_events, Event.ON_PYGAME_EVENTS_UPDATE)
        self._event_relay.subscribe(self, self.update, Event.ON_RENDER)
        self._event_relay.subscribe(self, self.render_gui, Event.ON_AFTER_RENDER_BEFORE_DISPLAY)
        self._event_relay.subscribe(self, self.on_done_placing, Event.ON_USER_CONFIRM_PLACEMENT)
        self._event_relay.subscribe(self, self.on_user_turn, Event.PLAYER1_REQUEST_GUESS)
        self._event_relay.subscribe(self, self.on_opponent_turn, Event.PLAYER2_REQUEST_GUESS)
        self._event_relay.subscribe(self, self.start_placing, Event.PLAYER1_REQUEST_SHIP_PLACEMENT)
        self._event_relay.subscribe(self, self.on_user_win, Event.ON_PLAYER1_WIN)
        self._event_relay.subscribe(self, self.on_opponent_win, Event.ON_PLAYER2_WIN)

    def get_events(self, events):
        self._pygame_events = events
        for event in events:
            self._manager.process_events(event)
            self._ui_holder.process_events(events)

    def update(self, delta: float):
        self._manager.update(delta)

    def render_gui(self):
        self._manager.draw_ui(self._display.surface)

    def start_placing(self, board):
        self._ui_holder.enable_scene("ship_placement")

    def on_done_placing(self, board):
        self._ui_holder.disable_scene("ship_placement")

    def on_user_turn(self):
        self._ui_holder.enable_scene("user_guess")
        self._ui_holder.disable_scene("opponent_guess")

    def on_opponent_turn(self, coords):
        self._ui_holder.enable_scene("opponent_guess")
        self._ui_holder.disable_scene("user_guess")

    def on_user_win(self):
        self._ui_holder.disable_scene("user_guess")
        self._ui_holder.disable_scene("opponent_guess")
        self._ui_holder.enable_scene("user_win")

    def on_opponent_win(self):
        self._ui_holder.disable_scene("user_guess")
        self._ui_holder.disable_scene("opponent_guess")
        self._ui_holder.enable_scene("opponent_win")
