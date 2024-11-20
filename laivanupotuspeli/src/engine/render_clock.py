import pygame
from engine.abstract_render_clock import AbstractRenderClock
class RenderClock(AbstractRenderClock):
    def __init__(self):
        self._clock = pygame.time.Clock()
        self._delta_ms = 0

    def tick(self, target_fps: float):
        self._delta_ms = self._clock.tick(target_fps)
