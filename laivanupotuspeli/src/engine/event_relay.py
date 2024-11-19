from engine.event import Event

class EventRelay:
    def __init__(self):
        self.subscribers:dict[Event, dict] = {}

    def subscribe(self, object, func, event: Event):
        if event not in self.subscribers.keys():
            self.subscribers[event] = {}
        self.subscribers[event][func] = object

    def unsubscribe(self, func, event: Event):
        if event not in self.subscribers.keys():
            return
        if func not in self.subscribers[event].keys():
            return
        del self.subscribers[event][func]

    def call(self, event: Event):
        if event not in self.subscribers.keys(): return
        for func, obj in self.subscribers[event].items():
            func(obj)
