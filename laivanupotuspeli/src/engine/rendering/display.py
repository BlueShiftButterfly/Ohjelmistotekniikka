import pygame
from engine.rendering.abstract_display import AbstractDisplay

class Display(AbstractDisplay):
    def __init__(self, screen_width: int, screen_height: int):
        self._surface: pygame.Surface = pygame.display.set_mode((screen_width, screen_height))

    @property
    def resolution(self) -> tuple:
        return (self._surface.get_width(), self._surface.get_height())

    @resolution.setter
    def resolution(self, res: tuple[int, int]):
        self._surface = pygame.display.set_mode((res[0], res[1]))

    @property
    def surface(self):
        return self._surface

    @property
    def caption(self) -> str:
        return pygame.display.get_caption()

    @caption.setter
    def caption(self, text: str):
        pygame.display.set_caption(text)

    def update(self):
        pygame.display.update()
