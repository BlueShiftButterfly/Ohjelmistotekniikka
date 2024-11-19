from abc import ABCMeta, abstractmethod

class AbstractDisplay(metaclass=ABCMeta):
    @abstractmethod
    def set_resolution(self):
        raise NotImplementedError("set_resolution method must be defined to use the base class")

    @property
    @abstractmethod
    def surface(self):
        raise NotImplementedError("surface method must be defined to use the base class")

    @property
    @abstractmethod
    def caption(self) -> str:
        raise NotImplementedError("set_caption method must be defined to use the base class")

    @caption.setter
    @abstractmethod
    def caption(self, text: str):
        raise NotImplementedError("set_caption method must be defined to use the base class")

    @abstractmethod
    def update(self):
        raise NotImplementedError("update method must be defined to use the base class")
