from enum import Enum

class PlayerPhase(Enum):
    WAIT_SHIP_PLACEMENT = 0
    PLACING_SHIPS = 1
    WAITING_FOR_GUESS_BEGIN = 2
    WAITING_FOR_TURN = 3
    SELECTING_GUESS = 4
