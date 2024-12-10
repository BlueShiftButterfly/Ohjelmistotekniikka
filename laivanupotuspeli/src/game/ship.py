from game.ship_type import ShipType
from game.direction import Direction

class Ship:
    def __init__(self, x: int, y: int, ship_type: ShipType, direction: Direction):
        self.x = x
        self.y = y
        self.ship_type = ship_type
        self.direction = direction
        self.is_sunk = False
        self._hit_tiles_count = 0

    def get_tiles_board_pos(self):
        real_tiles = []
        for tile in self.ship_type.get_tiles(self.direction):
            real_tile = (tile[0]+self.x, tile[1]+self.y)
            real_tiles.append(real_tile)
        return real_tiles

    def do_coords_overlap(self, coordinates: tuple[int, int]):
        does_overlap = False
        for tile in self.get_tiles_board_pos():
            if coordinates == tile:
                return True
        return does_overlap

    @property
    def hit_tiles_count(self):
        return self._hit_tiles_count

    def incerement_hit_count(self):
        self._hit_tiles_count += 1
        if self.hit_tiles_count >= len(self.ship_type.get_tiles()):
            self.is_sunk = True
