import inspect
from engine.event import Event

class EventRelay:
    """
    Event relay class that works as an event bus for the game and game-engine.
    Used to transmit messages to multiple subscribers without coupling.
    """
    def __init__(self):
        self._subscribers: dict[Event, dict] = {}

    def subscribe(self, obj, func, event: Event):
        """
        Subscribe a given function to an event.
        Args:
            obj: The object that the function is executed from. Should most of the time be the self object.
            func: The function that should be called when the event is triggered.
            event: The event to subscribe to.
        """
        if event not in self._subscribers:
            self._subscribers[event] = {}
        self._subscribers[event][func] = obj

    def unsubscribe(self, func, event: Event):
        """
        Unsubscribes a given function from an event.
        Args:
            func: The function that should unsubscribe.
            event: The event to unsubscribe from.
        """
        if event not in self._subscribers:
            return
        if func not in self._subscribers[event]:
            return
        del self._subscribers[event][func]

    def call(self, event: Event, *args):
        """
        Calls a given event and runs all of the event's subscribers using given arguments.

        Args:
            event: The event to call.
            Any other arguments passed afterwards will be passed to the subscribers. 
        """
        if event not in self._subscribers:
            return
        for func, obj in self._subscribers[event].items():
            if inspect.ismethod(func):
                func(*args)
            else:
                func(obj, *args)
