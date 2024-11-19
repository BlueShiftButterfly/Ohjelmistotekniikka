import pygame
from engine.renderer import Renderer
from engine.display import Display
from engine.render_clock import RenderClock
from engine.pygame_event_handler import PygameEventHandler
from engine.event_relay import EventRelay
from engine.event import Event

class Application:
    def __init__(self):
        self.init_pygame()
        self.event_bus = EventRelay()
        self.renderer = Renderer(self.event_bus, Display(1280, 720), RenderClock())
        self.pg_event_handler = PygameEventHandler(self.event_bus)
        self.event_bus.subscribe(self, Application.quit, Event.ON_APPLICATION_QUIT)
        self.renderer.start()

    def init_pygame(self):
        pygame.init()

    def quit(self):
        self.renderer.stop()
        pygame.quit()
