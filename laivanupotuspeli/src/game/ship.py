from game.ship_type import ShipType
from game.direction import Direction

SHIP_TYPES = {
    "2x1": ShipType([(0, 0), (1, 0)], [(0, 0), (0, -1)], "2x1"),
    "3x1": ShipType([(0, 0), (1, 0), (2, 0)], [(0, 0), (0, -1), (0, -2)], "3x1"),
    "4x1": ShipType([(0, 0), (1, 0), (2, 0), (3, 0)], [(0, 0), (0, -1), (0, -2), (0, -3)], "4x1"),
}

class Ship:
    """
    Class representing a ship piece in a Battleship-game.
    """
    def __init__(self, x: int, y: int, ship_type: ShipType, direction: Direction):
        """
        Args:
            x: The ship's x-coordinate on the game board.
            y: The ship's y-coordinate on the game board.
            ship_type: Type of ship. Determines for example the size of the ship piece.
            direction: Wether the ship is laying horizontally or vertically.
        """
        self.x = x
        self.y = y
        self.ship_type = ship_type
        self.direction = direction
        self.is_sunk = False
        self._hit_tiles_count = 0

    def get_tiles_board_pos(self) -> list[tuple[int, int]]:
        real_tiles = []
        for tile in self.ship_type.get_tiles(self.direction):
            real_tile = (tile[0]+self.x, tile[1]+self.y)
            real_tiles.append(real_tile)
        return real_tiles

    @property
    def hit_tiles_count(self) -> int:
        return self._hit_tiles_count

    def incerement_hit_count(self):
        self._hit_tiles_count += 1
        if self.hit_tiles_count >= len(self.ship_type.get_tiles(self.direction)):
            self.is_sunk = True
