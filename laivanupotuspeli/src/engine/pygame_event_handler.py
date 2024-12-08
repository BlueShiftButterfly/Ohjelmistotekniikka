import pygame
from engine.event_relay import EventRelay
from engine.event import Event

class PygameEventHandler:
    def __init__(self, event_relay: EventRelay):
        self._event_relay = event_relay
        self._event_relay.subscribe(self, PygameEventHandler.update, Event.ON_BEFORE_RENDER)

    def update(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self._event_relay.call(Event.ON_APPLICATION_QUIT)
            if event.type == pygame.MOUSEBUTTONDOWN:
                buttons = pygame.mouse.get_pressed()
                if buttons[0] is True:
                    self._event_relay.call(Event.ON_MOUSE0_PRESS)
