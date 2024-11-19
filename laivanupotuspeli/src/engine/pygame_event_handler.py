import pygame
from engine.event_relay import EventRelay
from engine.event import Event

class PygameEventHandler:
    def __init__(self, event_bus: EventRelay):
        self.__event_bus = event_bus
        self.__event_bus.subscribe(self, PygameEventHandler.update, Event.ON_BEFORE_RENDER)

    def update(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.__event_bus.call(Event.ON_APPLICATION_QUIT)
