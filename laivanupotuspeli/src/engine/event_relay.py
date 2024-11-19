from engine.event import Event

class EventRelay:
    def __init__(self):
        self.subscribers:dict[Event, list] = {}

    def subscribe(self, object, func, event: Event):
        if (event in self.subscribers.keys()):
            self.subscribers[event].append( tuple([object, func]) )
        else:
            self.subscribers[event] = []
            self.subscribers[event].append( tuple([object, func]) )

    def call(self, event: Event):
        if event in self.subscribers.keys():
            for sub in self.subscribers[event]:
                sub[1](sub[0])
