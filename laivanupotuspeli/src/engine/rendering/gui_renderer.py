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

        b1 = tp.Button("Confirm placement")
        b2 = tp.Button("2x1")
        b3 = tp.Button("3x1")
        b4 = tp.Button("4x1")
        b1.at_unclick = lambda : self.event_relay.call(Event.ON_CONFIRM_SHIP_PLACEMENT)
        b2.at_unclick = lambda : self.event_relay.call(Event.ON_SELECT_SHIP_TYPE, "2x1")
        b3.at_unclick = lambda : self.event_relay.call(Event.ON_SELECT_SHIP_TYPE, "3x1")
        b4.at_unclick = lambda : self.event_relay.call(Event.ON_SELECT_SHIP_TYPE, "4x1")
        ui_list = [
            tp.Group([
                b1,
                b2,
                b3,
                b4
            ])
        ]
        b1.move(500, 340)
        b2.move(500, 100)
        b3.move(500, 120)
        b4.move(500, 140)
        self.ui_elements = tp.Group(ui_list, align="right")
        self.updater = self.ui_elements.get_updater()
        self.pygame_events = None

    def get_events(self, events):
        self.pygame_events = events

    def render_gui(self):
        #if self.pygame_events is None:
        #    return
        #print("UPDATE")
        self.updater.update(events=self.pygame_events)
