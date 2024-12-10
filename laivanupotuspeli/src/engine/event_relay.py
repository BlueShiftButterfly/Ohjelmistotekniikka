import inspect
from engine.event import Event

class EventRelay:
    def __init__(self):
        self._subscribers: dict[Event, dict] = {}

    def subscribe(self, obj, func, event: Event):
        if event not in self._subscribers:
            self._subscribers[event] = {}
        self._subscribers[event][func] = obj

    def unsubscribe(self, func, event: Event):
        if event not in self._subscribers:
            return
        if func not in self._subscribers[event]:
            return
        del self._subscribers[event][func]

    def call(self, event: Event, *args):
        if event not in self._subscribers:
            return
        for func, obj in self._subscribers[event].items():
            if inspect.ismethod(func):
                func(*args)
            else:
                func(obj, *args)
