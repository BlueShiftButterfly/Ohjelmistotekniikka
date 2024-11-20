from abc import ABCMeta, abstractmethod

class AbstractRenderDirty(metaclass=ABCMeta):
    @abstractmethod
    def set_dirty(self):
        raise NotImplementedError("set_dirty method must be defined to use the base class")

    @abstractmethod
    def update(self):
        raise NotImplementedError("update method must be defined to use the base class")

    @property
    @abstractmethod
    def surface(self):
        raise NotImplementedError("surface method must be defined to use the base class")

    @property
    @abstractmethod
    def rect(self):
        raise NotImplementedError("rect method must be defined to use the base class")