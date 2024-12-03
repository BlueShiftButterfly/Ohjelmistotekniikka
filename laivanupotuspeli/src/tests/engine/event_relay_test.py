import unittest
from unittest.mock import patch
from enum import Enum
from engine.event_relay import EventRelay

class StubEvent(Enum):
    TEST0 = 0
    TEST1 = 1
    TEST2 = 2

class StubEventCaller:
    def call(self):
        pass

class StubEventSubscriber:
    def __init__(self):
        self.val = 0

    def subcall(self):
        self.val = 1

class TestEventRelay(unittest.TestCase):
    def setUp(self):
        self.caller = StubEventCaller()
        self.subscriber = StubEventSubscriber()
        self.subscriber2 = StubEventSubscriber()
        self.event_relay = EventRelay()

    def test_method_is_called_when_subcribed(self):
        with patch.object(self.subscriber, "subcall") as this_should_be_called:
            self.event_relay.subscribe(self.subscriber, self.subscriber.subcall, StubEvent.TEST0)
            self.event_relay.call(StubEvent.TEST0)
            this_should_be_called.assert_called()

    def test_method_is_not_called_when_not_subcribed(self):
        with patch.object(self.subscriber, "subcall") as this_should_be_called:
            self.event_relay.call(StubEvent.TEST0)
            self.assertFalse(this_should_be_called.called)

    def test_method_is_not_called_after_unsubcribed(self):
        with patch.object(self.subscriber, "subcall") as this_should_be_called:
            self.event_relay.subscribe(self.subscriber, self.subscriber.subcall, StubEvent.TEST0)
            self.event_relay.unsubscribe(self.subscriber.subcall, StubEvent.TEST0)
            self.event_relay.call(StubEvent.TEST0)
            self.assertFalse(this_should_be_called.called)

    def test_method_is_not_called_after_unsubcribed_event_in_subscribers(self):
        with patch.object(self.subscriber, "subcall") as this_should_be_called:
            self.event_relay.subscribe(self.subscriber, self.subscriber.subcall, StubEvent.TEST0)
            self.event_relay.subscribe(self.subscriber2, self.subscriber2.subcall, StubEvent.TEST0)
            self.event_relay.unsubscribe(self.subscriber.subcall, StubEvent.TEST0)
            self.event_relay.call(StubEvent.TEST0)
            self.assertFalse(this_should_be_called.called)

    def test_unsubcribe_nonexistent_event_doesnt_change_subscribers(self):
        self.event_relay.unsubscribe(self.subscriber.subcall, StubEvent.TEST0)
        self.assertFalse(StubEvent.TEST0 in self.event_relay._subscribers)

    def test_unsubcribe_nonexistent_object_doesnt_change_subscribers(self):
        self.event_relay.subscribe(self.subscriber, self.subscriber.subcall, StubEvent.TEST0)
        self.event_relay.unsubscribe(self.subscriber.subcall, StubEvent.TEST0)
        self.event_relay.unsubscribe(self.subscriber.subcall, StubEvent.TEST0)
        self.assertFalse(self.subscriber in self.event_relay._subscribers[StubEvent.TEST0])
