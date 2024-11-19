from engine.event import Event

class EventRelay:
    def __init__(self):
        self.subscribers:dict[Event, list] = {}

    def subscribe(self, object, func, event: Event):
        if (event not in self.subscribers.keys()):
            self.subscribers[event] = []
        self.subscribers[event].append( tuple([object, func]) )

    def call(self, event: Event):
        if event not in self.subscribers.keys(): return
        for sub in self.subscribers[event]:
            sub[1](sub[0])
