import inspect
from engine.event import Event

class EventRelay:
    def __init__(self):
        self._subscribers: dict[Event, dict] = {}

    def subscribe(self, object, func, event: Event):
        if event not in self._subscribers.keys():
            self._subscribers[event] = {}
        self._subscribers[event][func] = object

    def unsubscribe(self, func, event: Event):
        if event not in self._subscribers.keys():
            return
        if func not in self._subscribers[event].keys():
            return
        del self._subscribers[event][func]

    def call(self, event: Event):
        if event not in self._subscribers.keys(): return
        for func, obj in self._subscribers[event].items():
            if inspect.ismethod(func):
                func()
            else:
                func(obj)
