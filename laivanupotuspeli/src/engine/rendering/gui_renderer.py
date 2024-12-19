import thorpy as tp
from engine.rendering.abstract_display import AbstractDisplay
from engine.event_relay import EventRelay
from engine.event import Event

class GUIRenderer:
    def __init__(self, event_relay: EventRelay, display: AbstractDisplay):
        self.display = display
        self.event_relay = event_relay
        tp.init(self.display.surface, tp.theme_classic)
        self.event_relay.subscribe(self, self.get_events, Event.ON_PYGAME_EVENTS_UPDATE)
        self.event_relay.subscribe(self, self.render_gui, Event.ON_AFTER_RENDER_BEFORE_DISPLAY)
        self.debug_text = tp.Text("This is some text")
        self.b1 = tp.Button("Confirm placement")
        self.b2 = tp.Button("2x1")
        self.b3 = tp.Button("3x1")
        self.b4 = tp.Button("4x1")
        self.b1.at_unclick = lambda : self.event_relay.call(Event.ON_CONFIRM_SHIP_BUTTON)
        self.b2.at_unclick = lambda : self.event_relay.call(Event.ON_SELECT_SHIP_TYPE, "2x1")
        self.b3.at_unclick = lambda : self.event_relay.call(Event.ON_SELECT_SHIP_TYPE, "3x1")
        self.b4.at_unclick = lambda : self.event_relay.call(Event.ON_SELECT_SHIP_TYPE, "4x1")
        self.ship_placing_ui = tp.Group([
                self.b1,
                self.b2,
                self.b3,
                self.b4,
                #self.debug_text
            ], align="right")

        self.b1.move(500, 340)
        self.b2.move(500, 100)
        self.b3.move(500, 120)
        self.b4.move(500, 140)
        self.ui_elements = tp.Group([self.ship_placing_ui, tp.Group([tp.Text("This is some text")], align="right")], align="right")
        self.updater = self.ui_elements.get_updater()
        self.pygame_events = None

    def get_events(self, events):
        self.pygame_events = events

    def render_gui(self):
        self.updater.update(events=self.pygame_events)

    def set_debug_text(self, text: str):
        self.debug_text.set_text(text)
