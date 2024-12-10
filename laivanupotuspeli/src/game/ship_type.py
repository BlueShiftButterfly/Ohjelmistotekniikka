from game.direction import Direction

class ShipType:
    def __init__(self, tiles_hor: list[tuple[int, int]], tiles_vert: list[tuple[int, int]]):
        self._tiles_horizontal = tiles_hor
        self._tiles_vertical = tiles_vert

    def get_tiles(self, direction: Direction):
        if direction == Direction.HORIZONTAL:
            return self._tiles_horizontal
        return self._tiles_vertical
