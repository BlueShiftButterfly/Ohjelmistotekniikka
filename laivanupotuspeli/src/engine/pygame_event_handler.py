import pygame

class PygameEventHandler:
    def __init__(self):
        self.__on_quit_functions = []

    def register_quit_function(self, func):
        self.__on_quit_functions.append(func)

    def update(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                for func in self.__on_quit_functions:
                    func()
