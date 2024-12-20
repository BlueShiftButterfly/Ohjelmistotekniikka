from engine.rendering.abstract_display import AbstractDisplay
from engine.rendering.abstract_render_clock import AbstractRenderClock
from engine.event_relay import EventRelay
from engine.event import Event
from engine.rendering.abstract_renderable import AbstractRenderable
from engine.rendering.gui_renderer import GUIRenderer
from engine.asset_loader import AssetLoader

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
        self._renderables: list[AbstractRenderable] = []
        self.asset_loader = AssetLoader()
        self.asset_loader.load()
        self.gui_renderer = GUIRenderer(event_relay, self._display)

    def add_renderable(self, renderable: AbstractRenderable):
        self._renderables.append(renderable)

    @property
    def display(self):
        return self._display

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
        for r in self._renderables:
            self._display.surface.blit(r.surface, r.position)
        self._event_relay.call(Event.ON_AFTER_RENDER_BEFORE_DISPLAY)
        self._display.update()
        self._event_relay.call(Event.ON_AFTER_RENDER)
        self._render_clock.tick(60)
