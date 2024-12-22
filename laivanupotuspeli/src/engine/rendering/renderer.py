from engine.rendering.abstract_display import AbstractDisplay
from engine.rendering.abstract_render_clock import AbstractRenderClock
from engine.event_relay import EventRelay
from engine.event import Event
from engine.rendering.abstract_renderable import AbstractRenderable
from engine.rendering.gui_renderer import GUIRenderer
from engine.asset_loader import AssetLoader
from engine.rendering import colors

class Renderer:
    """Class responsible for game rendering. Renders renderable objects and calls update event every frame."""
    def __init__(
            self,
            event_relay: EventRelay,
            display: AbstractDisplay,
            render_clock: AbstractRenderClock
        ):
        """
        Args:
            event_relay: event_relay object for event based communication
            display: pygame display wrapper object
            render_clock: pygame clock wrapper object
        """
        self._do_rendering = True
        self._display = display
        self._render_clock = render_clock
        self._event_relay = event_relay
        self._renderables: list[AbstractRenderable] = []
        self._asset_loader = AssetLoader()
        self._asset_loader.load()
        self._gui_renderer = GUIRenderer(event_relay, self._display)
        self._delta: float = 0

    def add_renderable(self, renderable: AbstractRenderable):
        """
        Add given renderable object to render queue.
        Args:
            renderable: the object to add to the render queue
        """
        self._renderables.append(renderable)

    @property
    def asset_loader(self):
        return self._asset_loader

    @property
    def display(self):
        return self._display

    def start_loop(self):
        """
        Start the render loop.
        """
        while self._do_rendering:
            self._render()

    def _render(self):
        if self._do_rendering is False:
            return
        self._display.surface.fill(colors.BLACK)
        self._event_relay.call(Event.ON_BEFORE_RENDER)
        self._delta = self._render_clock.tick(60)/1000.0
        self._event_relay.call(Event.ON_RENDER, self._delta)
        for r in self._renderables:
            if r.enabled is False:
                continue
            self._display.surface.blit(r.surface, r.position)
        self._event_relay.call(Event.ON_AFTER_RENDER_BEFORE_DISPLAY)
        self._display.update()
        self._event_relay.call(Event.ON_AFTER_RENDER)
