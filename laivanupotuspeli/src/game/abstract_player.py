from abc import ABCMeta, abstractmethod
from game.board import Board

class AbstractPlayer(metaclass=ABCMeta):
    @abstractmethod
    def request_ships(self, board: Board):
        raise NotImplementedError("request_ships method must be defined to use the base class")

    @abstractmethod
    def request_guess(self, board: Board):
        raise NotImplementedError("request_guess method must be defined to use the base class")
