import pygame
from engine.rendering.renderer import Renderer
from engine.rendering.display import Display
from engine.rendering.render_clock import RenderClock
from engine.pygame_event_handler import PygameEventHandler
from engine.event_relay import EventRelay
from engine.event import Event

class Application:
    """
    Main application class. Contains all game-engine components.
    """
    def __init__(self, event_relay: EventRelay):
        """
        Args:
            event_relay: event_relay object for event based communication
        """
        self._init_pygame()
        self.event_relay = event_relay
        self.renderer = Renderer(self.event_relay, Display(1280, 900), RenderClock())
        self.pg_event_handler = PygameEventHandler(self.event_relay)
        self.event_relay.subscribe(self, Application.quit, Event.ON_APPLICATION_QUIT)
        self.renderer.display.caption = "Battleship"

    def start(self):
        """
        Start the application and create window.
        """
        self.renderer.start_loop()

    def _init_pygame(self):
        pygame.init()

    def quit(self):
        """
        Quits the application to desktop.
        """
        pygame.quit()
