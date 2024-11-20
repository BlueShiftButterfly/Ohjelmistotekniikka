from enum import Enum

class Event(Enum):
    ON_AFTER_RENDER = 0
    ON_BEFORE_RENDER = 1
    ON_APPLICATION_QUIT = 3

class RenderEvent(Enum):
    ON_RENDER_COMPONENT_UPDATE = 0
    ON_RENDER_LAYER_UPDATE = 1
