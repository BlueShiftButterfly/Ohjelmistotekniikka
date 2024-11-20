from engine.abstract_display import AbstractDisplay
from engine.abstract_render_clock import AbstractRenderClock
from engine.event_relay import EventRelay
from engine.event import Event

class Renderer:
    def __init__(
            self,
            event_relay: EventRelay,
            display: AbstractDisplay,
            render_clock: AbstractRenderClock
        ):
        self.__do_rendering = True
        self.__display = display
        self.__render_clock = render_clock
        self.__event_relay = event_relay

    def start_loop(self):
        while self.__do_rendering:
            self.__render()

    def unpause(self):
        self.__do_rendering = True

    def pause(self):
        self.__do_rendering = False

    def __render(self):
        self.__event_relay.call(Event.ON_BEFORE_RENDER)
        if self.__do_rendering is False:
            return
        self.__display.update()
        self.__event_relay.call(Event.ON_AFTER_RENDER)
        self.__render_clock.tick(60)
