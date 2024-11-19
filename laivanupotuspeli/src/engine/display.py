import pygame
from engine.abstract_display import AbstractDisplay

class Display(AbstractDisplay):
    def __init__(self, screen_width: int, screen_height: int):
        self.__surface: pygame.Surface = self.set_resolution(screen_width, screen_height)

    def set_resolution(self, screen_width: int, screen_height: int):
        self.__surface = pygame.display.set_mode((screen_width, screen_height))

    @property
    def surface(self):
        return self.__surface

    @property
    def caption(self) -> str:
        return pygame.display.get_caption()

    @caption.setter
    def caption(self, text: str):
        pygame.display.set_caption(text)

    def update(self):
        pygame.display.update()
