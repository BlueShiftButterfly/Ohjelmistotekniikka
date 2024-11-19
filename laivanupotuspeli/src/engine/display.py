import pygame

class Display:
    def __init__(self, screen_width: int, screen_height: int):
        self.__surface: pygame.Surface = self.set_resolution(screen_width, screen_height)

    def set_resolution(self, screen_width: int, screen_height: int):
        self.__surface = pygame.display.set_mode((screen_width, screen_height))

    @property
    def surface(self):
        return self.__surface

    def set_caption(self, caption: str):
        pygame.display.set_caption(caption)

    def update(self):
        pygame.display.update()
