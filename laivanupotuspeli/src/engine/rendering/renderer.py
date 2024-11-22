from engine.rendering.abstract_display import AbstractDisplay
from engine.rendering.abstract_render_clock import AbstractRenderClock
from engine.event_relay import EventRelay
from engine.event import Event
import engine.rendering.colors as colors

class Renderer:
    def __init__(
            self,
            event_relay: EventRelay,
            display: AbstractDisplay,
            render_clock: AbstractRenderClock
        ):
        self._do_rendering = True
        self._display = display
        self._render_clock = render_clock
        self._event_relay = event_relay
        self._renderables = []
        self._background_color = colors.DARK_BLUE

    def start_loop(self):
        while self._do_rendering:
            self._render()

    def unpause(self):
        self._do_rendering = True

    def pause(self):
        self._do_rendering = False

    def _render(self):
        self._event_relay.call(Event.ON_BEFORE_RENDER)
        if self._do_rendering is False:
            return
        self._display.update()
        self._event_relay.call(Event.ON_AFTER_RENDER)
        self._render_clock.tick(60)
