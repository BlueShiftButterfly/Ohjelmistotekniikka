import pygame
from engine.rendering.abstract_render_clock import AbstractRenderClock
class RenderClock(AbstractRenderClock):
    def __init__(self):
        self._clock = pygame.time.Clock()

    def tick(self, target_fps: float) -> float:
        return self._clock.tick(target_fps)
