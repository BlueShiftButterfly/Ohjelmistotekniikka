from game.guess import Guess
from game.ship import Ship
from game.ship_type import ShipType

class Board:
    def __init__(self, width: int, height: int):
        self._width = width
        self._height = height
        self.ships: dict[tuple[int, int], Ship] = {}
        self.opponent_guesses: dict[tuple[int, int], Guess] = {}
        self._ships_left_to_place = {
            "2x1": 1,
            "3x1": 2,
            "4x1": 1
        }

    def are_coords_within_bounds(self, coordinates: tuple[int, int]):
        return (
            0 <= coordinates[0] < self._width and
            0 <= coordinates[1] < self._height
        )

    def add_guess(self, x: int, y: int) -> bool:
        guess_coords = (x, y)
        if self.are_coords_within_bounds(guess_coords) is False:
            return False
        if guess_coords in self._opponent_guesses:
            return False
        hit_ship = False
        for k, ship in self._ships.items():
            for c in ship.get_tiles_board_pos():
                if c == (x, y):
                    hit_ship = True
                    ship.incerement_hit_count()
        self._opponent_guesses[guess_coords] = Guess(x, y, hit_ship)
        return True

    def would_hit_ship(self, x: int, y: int) -> bool:
        if self.is_valid_guess_position(x, y) is False:
            return False
        for k, ship in self._ships.items():
            for c in ship.get_tiles_board_pos():
                if c == (x, y):
                    return True
        return False

    def is_valid_guess_position(self, x: int, y: int) -> bool:
        guess_coords = (x, y)
        if self.are_coords_within_bounds(guess_coords) is False:
            return False
        if guess_coords in self._opponent_guesses:
            return False
        return True

    def add_ship(self, ship: Ship) -> bool:
        if self.is_valid_ship_placement(ship) and self.has_ship_type_left(ship.ship_type):
            self._ships[(ship.x, ship.y)] = ship
            self._ships_left_to_place[ship.ship_type.name] -= 1
            return True
        return False

    def do_ships_overlap(self, ship1: Ship, ship2: Ship) -> bool:
        for tile1 in ship1.get_tiles_board_pos():
            for tile2 in ship2.get_tiles_board_pos():
                if tile1[0] == tile2[0] and tile1[1] == tile2[1]:
                    return True
        return False

    def try_remove_ship_at_position(self, coordinates: tuple[int, int]) -> bool:
        for k, ship in self._ships.items():
            for c in ship.get_tiles_board_pos():
                if c == coordinates:
                    self._ships.pop(k)
                    self._ships_left_to_place[ship.ship_type.name] += 1
                    return True
        return False

    def is_valid_ship_placement(self, ship: Ship) -> bool:
        ship_coords = (ship.x, ship.y)
        for c in ship.get_tiles_board_pos():
            if self.are_coords_within_bounds(c) is False:
                return False
        if ship_coords in self._ships.values():
            return False
        for existing_ship in self._ships.values():
            if self.do_ships_overlap(ship, existing_ship):
                return False
        return True

    def placed_all_ships(self):
        for v in self._ships_left_to_place.values():
            if v > 0:
                return False
        return True

    def has_ship_type_left(self, ship_type: ShipType):
        if ship_type is None:
            return False
        return self._ships_left_to_place[ship_type.name] > 0

    def has_unsunk_ships_left(self) -> bool:
        has_unsunk = False
        for s in self._ships.values():
            if s.is_sunk is False:
                has_unsunk = True
        return has_unsunk
