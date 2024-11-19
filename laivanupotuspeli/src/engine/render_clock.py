import pygame
from engine.abstract_render_clock import AbstractRenderClock
class RenderClock(AbstractRenderClock):
    def __init__(self):
        self.__clock = pygame.time.Clock()
        self.__delta_ms = 0

    def tick(self, target_fps: float):
        self.__delta_ms = self.__clock.tick(target_fps)
