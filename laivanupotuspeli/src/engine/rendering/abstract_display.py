from abc import ABCMeta, abstractmethod
import pygame

class AbstractDisplay(metaclass=ABCMeta):
    @property
    @abstractmethod
    def resolution(self) -> tuple:
        raise NotImplementedError("resolution method must be defined to use the base class")

    @resolution.setter
    def resolution(self, res: tuple[int, int]):
        raise NotImplementedError("resolution method must be defined to use the base class")

    @property
    @abstractmethod
    def surface(self) -> pygame.Surface:
        raise NotImplementedError("surface method must be defined to use the base class")

    @property
    @abstractmethod
    def caption(self) -> str:
        raise NotImplementedError("caption method must be defined to use the base class")

    @caption.setter
    @abstractmethod
    def caption(self, text: str):
        raise NotImplementedError("caption method must be defined to use the base class")

    @abstractmethod
    def update(self):
        raise NotImplementedError("update method must be defined to use the base class")
