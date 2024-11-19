from enum import Enum

class Event(Enum):
    ON_AFTER_RENDER = 0
    ON_BEFORE_RENDER = 1
    ON_APPLICATION_QUIT = 3
