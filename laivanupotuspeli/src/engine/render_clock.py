import pygame

class RenderClock:
    def __init__(self):
        self.__clock = pygame.time.Clock()
        self.__delta_ms = 0

    def tick(self, target_fps):
        self.__delta_ms = self.__clock.tick(target_fps)
