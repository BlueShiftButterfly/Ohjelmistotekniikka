import pygame
from engine.renderer import Renderer
from engine.display import Display
from engine.render_clock import RenderClock
from engine.pygame_event_handler import PygameEventHandler

class Application:
    def __init__(self):
        self.init_pygame()
        self.renderer = Renderer(Display(1280, 720), RenderClock())
        self.pg_event_handler = PygameEventHandler()
        self.pg_event_handler.register_quit_function(self.quit)
        self.renderer.register_loop(self.pg_event_handler.update)
        self.renderer.start()

    def init_pygame(self):
        pygame.init()

    def quit(self):
        self.renderer.stop()
        pygame.quit()
