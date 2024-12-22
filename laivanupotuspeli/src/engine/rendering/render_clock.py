import pygame
from engine.rendering.abstract_render_clock import AbstractRenderClock

class RenderClock(AbstractRenderClock):
    """
    Pygame Clock wrapper
    """
    def __init__(self):
        self._clock = pygame.time.Clock()

    def tick(self, target_fps: float) -> float:
        """
        Call the pygame tick function. Limits the FPS of the application and returns frame delta.
        Args:
            target_fps: Maximum number of frames to render per second
        """
        return self._clock.tick(target_fps)
