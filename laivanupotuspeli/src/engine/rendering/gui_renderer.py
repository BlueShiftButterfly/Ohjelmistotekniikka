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

        button = tp.Button("Confirm placement")
        ui_list = [
            tp.Group([
                button
            ])
        ]
        button.move(500, 300)
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
