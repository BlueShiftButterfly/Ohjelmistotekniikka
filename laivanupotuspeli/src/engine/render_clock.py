import pygame

class RenderClock:
    def __init__(self):
        self.__clock = pygame.time.Clock()
        self.__deltaMS = 0

    def tick(self, target_fps):
        self.__deltaMS = self.__clock.tick(target_fps)