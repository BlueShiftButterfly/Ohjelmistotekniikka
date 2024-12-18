from abc import ABCMeta, abstractmethod
import pygame

class AbstractRenderable(metaclass=ABCMeta):
    @property
    @abstractmethod
    def position(self) -> tuple[int, int]:
        raise NotImplementedError("position method must be defined to use the base class")

    @property
    @abstractmethod
    def surface(self) -> pygame.Surface:
        raise NotImplementedError("surface method must be defined to use the base class")
