from engine.display import Display
from engine.render_clock import RenderClock
from engine.event_relay import EventRelay
from engine.event import Event

class Renderer:
    def __init__(self, event_bus: EventRelay, display: Display, render_clock: RenderClock):
        self.__do_rendering = True
        self.__display = display
        self.__render_clock = render_clock
        self.__event_bus = event_bus

    def start(self):
        while self.__do_rendering:
            self.__render()

    def stop(self):
        self.__do_rendering = False

    def __render(self):
        self.__event_bus.call(Event.ON_BEFORE_RENDER)
        if self.__do_rendering is False: return
        self.__display.update()
        self.__event_bus.call(Event.ON_AFTER_RENDER)
        self.__render_clock.tick(60)
