import pygame
from engine.rendering.renderer import Renderer
from engine.rendering.display import Display
from engine.rendering.render_clock import RenderClock
from engine.pygame_event_handler import PygameEventHandler
from engine.event_relay import EventRelay
from engine.event import Event

class Application:
    def __init__(self, event_relay: EventRelay):
        self.init_pygame()
        self.event_relay = event_relay
        self.renderer = Renderer(self.event_relay, Display(1280, 720), RenderClock())
        self.pg_event_handler = PygameEventHandler(self.event_relay)
        self.event_relay.subscribe(self, Application.quit, Event.ON_APPLICATION_QUIT)

    def start(self):
        self.renderer.start_loop()

    def init_pygame(self):
        pygame.init()

    def quit(self):
        self.renderer.pause()
        pygame.quit()
