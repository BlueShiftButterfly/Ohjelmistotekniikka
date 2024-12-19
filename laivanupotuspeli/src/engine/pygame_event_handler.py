import pygame
from engine.event_relay import EventRelay
from engine.event import Event

class PygameEventHandler:
    def __init__(self, event_relay: EventRelay):
        self._event_relay = event_relay
        self._event_relay.subscribe(self, PygameEventHandler.update, Event.ON_BEFORE_RENDER)

    def update(self):
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                self._event_relay.call(Event.ON_APPLICATION_QUIT)
            if event.type == pygame.MOUSEBUTTONDOWN:
                buttons = pygame.mouse.get_pressed()
                if buttons[0] is True:
                    self._event_relay.call(Event.ON_MOUSE0_PRESS)
                if buttons[2] is True:
                    self._event_relay.call(Event.ON_MOUSE1_PRESS)
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    self._event_relay.call(Event.ON_SHIP_ROTATE)
                if event.key == pygame.K_ESCAPE:
                    self._event_relay.call(Event.ON_APPLICATION_QUIT)
        self._event_relay.call(Event.ON_PYGAME_EVENTS_UPDATE, events)
