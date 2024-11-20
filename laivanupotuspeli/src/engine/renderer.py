from engine.abstract_display import AbstractDisplay
from engine.abstract_render_clock import AbstractRenderClock
from engine.event_relay import EventRelay
from engine.event import Event
from engine.abstract_render_dirty import AbstractRenderDirty
import engine.colors as colors

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
        self._render_layers:list[AbstractRenderDirty] = []
        self._background_color = colors.DARK_BLUE

    def start_loop(self):
        while self._do_rendering:
            self._render()

    def unpause(self):
        self._do_rendering = True

    def pause(self):
        self._do_rendering = False

    def _render(self):
        if self._do_rendering is False:
            return
        self._event_relay.call(Event.ON_BEFORE_RENDER)
        [layer.update() for layer in self._render_layers]
        [self._display.surface.blit(layer.surface, layer.rect) for layer in self._render_layers]
        #self._display.surface.fill(self._background_color)
        self._display.update()
        self._event_relay.call(Event.ON_AFTER_RENDER)
        self._render_clock.tick(60)
