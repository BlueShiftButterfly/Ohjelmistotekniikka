from abc import ABCMeta, abstractmethod

class AbstractRenderClock(metaclass=ABCMeta):
    @abstractmethod
    def tick(self, target_fps: float) -> float:
        raise NotImplementedError("tick method must be defined to use the base class")
