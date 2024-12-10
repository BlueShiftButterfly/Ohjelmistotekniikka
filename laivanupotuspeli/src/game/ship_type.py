from game.direction import Direction

class ShipType:
    def __init__(self, tiles_horizontal: list[tuple[int, int]], tiles_vertical: list[tuple[int, int]]):
        self._tiles_horizontal = tiles_horizontal
        self._tiles_vertical = tiles_vertical

    def get_tiles(self, direction: Direction):
        if direction == Direction.HORIZONTAL:
            return self._tiles_horizontal
        else:
            return self._tiles_vertical
