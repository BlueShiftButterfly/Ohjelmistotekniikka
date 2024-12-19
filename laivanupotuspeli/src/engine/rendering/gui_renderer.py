import pygame
import pygame_gui
from engine.rendering.abstract_display import AbstractDisplay
from engine.event_relay import EventRelay
from engine.event import Event

class GUIRenderer:
    def __init__(self, event_relay: EventRelay, display: AbstractDisplay):
        self.display = display
        self.event_relay = event_relay
        self.event_relay.subscribe(self, self.get_events, Event.ON_PYGAME_EVENTS_UPDATE)
        self.event_relay.subscribe(self, self.update, Event.ON_RENDER)
        self.event_relay.subscribe(self, self.render_gui, Event.ON_AFTER_RENDER_BEFORE_DISPLAY)
        self.event_relay.subscribe(self, self.on_finish_placing_ships, Event.ON_USER_CONFIRM_SHIP_PLACEMENT)
        self.pygame_events = None
        self.manager = pygame_gui.UIManager(self.display.resolution)

        self.confirm_placement_button = pygame_gui.elements.UIButton(
            relative_rect=pygame.Rect((1000, 640), (200, 50)),
            text="Confirm Ship Placement",
            manager=self.manager
        )

        self.s1_button = pygame_gui.elements.UIButton(
            relative_rect=pygame.Rect((1000, 400), (100, 50)),
            text="2x1",
            manager=self.manager
        )

        self.s2_button = pygame_gui.elements.UIButton(
            relative_rect=pygame.Rect((1000, 450), (100, 50)),
            text="3x1",
            manager=self.manager
        )

        self.s3_button = pygame_gui.elements.UIButton(
            relative_rect=pygame.Rect((1000, 500), (100, 50)),
            text="4x1",
            manager=self.manager
        )

    def get_events(self, events):
        self.pygame_events = events
        for event in events:
            if event.type == pygame_gui.UI_BUTTON_PRESSED:
                if event.ui_element == self.confirm_placement_button:
                    self.event_relay.call(Event.ON_CONFIRM_SHIP_BUTTON)
                if event.ui_element == self.s1_button:
                    self.event_relay.call(Event.ON_SELECT_SHIP_TYPE, "2x1")
                if event.ui_element == self.s2_button:
                    self.event_relay.call(Event.ON_SELECT_SHIP_TYPE, "3x1")
                if event.ui_element == self.s3_button:
                    self.event_relay.call(Event.ON_SELECT_SHIP_TYPE, "4x1")
            self.manager.process_events(event)

    def update(self, delta: float):
        self.manager.update(delta)

    def render_gui(self):
        self.manager.draw_ui(self.display.surface)

    def on_finish_placing_ships(self):
        self.confirm_placement_button.kill()
        self.s1_button.kill()
        self.s2_button.kill()
        self.s3_button.kill()
