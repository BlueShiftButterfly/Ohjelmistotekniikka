import pygame
import pygame_gui
from engine.rendering.abstract_display import AbstractDisplay
from engine.event_relay import EventRelay
from engine.event import Event
from engine.rendering.gui_scene import GUI_Holder

class GUIRenderer:
    def __init__(self, event_relay: EventRelay, display: AbstractDisplay):
        self.display = display
        self.event_relay = event_relay

        self.pygame_events = None
        self.manager = pygame_gui.UIManager(self.display.resolution, "src/assets/theme.json")
        self.ui_holder = GUI_Holder(self.event_relay, self.manager)

        self.event_relay.subscribe(self, self.get_events, Event.ON_PYGAME_EVENTS_UPDATE)
        self.event_relay.subscribe(self, self.update, Event.ON_RENDER)
        self.event_relay.subscribe(self, self.render_gui, Event.ON_AFTER_RENDER_BEFORE_DISPLAY)
        self.event_relay.subscribe(self, self.on_finish_placing_ships, Event.ON_USER_CONFIRM_SHIP_PLACEMENT)
        self.event_relay.subscribe(self, self.on_user_turn, Event.PLAYER1_REQUEST_GUESS)
        self.event_relay.subscribe(self, self.on_opponent_turn, Event.PLAYER2_REQUEST_GUESS)
        self.event_relay.subscribe(self, self.start_placing_ships, Event.PLAYER1_REQUEST_SHIP_PLACEMENT)
        self.event_relay.subscribe(self, self.on_user_win, Event.ON_PLAYER1_WIN)
        self.event_relay.subscribe(self, self.on_opponent_win, Event.ON_PLAYER2_WIN)

    def get_events(self, events):
        self.pygame_events = events
        for event in events:
            self.manager.process_events(event)
            self.ui_holder.process_events(events)

    def update(self, delta: float):
        self.manager.update(delta)

    def render_gui(self):
        self.manager.draw_ui(self.display.surface)

    def start_placing_ships(self, board):
        self.ui_holder.enable_scene("ship_placement")

    def on_finish_placing_ships(self, board):
        self.ui_holder.disable_scene("ship_placement")

    def on_user_turn(self):
        self.ui_holder.enable_scene("user_guess")
        self.ui_holder.disable_scene("opponent_guess")

    def on_opponent_turn(self, coords):
        self.ui_holder.enable_scene("opponent_guess")
        self.ui_holder.disable_scene("user_guess")

    def on_user_win(self):
        self.ui_holder.disable_scene("user_guess")
        self.ui_holder.disable_scene("opponent_guess")
        self.ui_holder.enable_scene("user_win")

    def on_opponent_win(self):
        self.ui_holder.disable_scene("user_guess")
        self.ui_holder.disable_scene("opponent_guess")
        self.ui_holder.enable_scene("opponent_win")
