from game.guess import Guess
from game.ship import Ship
from game.ship_type import ShipType

class Board:
    def __init__(self, width: int, height: int):
        self.width = width
        self.height = height
        self.ships: dict[tuple[int, int], Ship] = {}
        self.opponent_guesses: dict[tuple[int, int], Guess] = {}
        self.ships_left_to_place = {
            "2x1": 1,
            "3x1": 2,
            "4x1": 1
        }

    def are_coords_within_bounds(self, coordinates: tuple[int, int]):
        return (
            0 <= coordinates[0] < self.width and
            0 <= coordinates[1] < self.height
        )

    def add_guess(self, x: int, y: int) -> bool:
        guess_coords = (x, y)
        if self.are_coords_within_bounds(guess_coords) is False:
            return False
        if guess_coords in self.opponent_guesses:
            return False
        hit_ship = False
        for ship in self.ships.values():
            if ship.do_coords_overlap(guess_coords):
                hit_ship = True
                ship.incerement_hit_count()
        self.opponent_guesses[guess_coords] = Guess(x, y, hit_ship)
        return True

    def add_ship(self, ship: Ship) -> bool:
        if self.is_valid_ship_placement(ship) and self.has_ship_type_left(ship.ship_type):
            self.ships[(ship.x, ship.y)] = ship
            self.ships_left_to_place[ship.ship_type.name] -= 1
            return True
        return False

    def do_ships_overlap(self, ship1: Ship, ship2: Ship) -> bool:
        for tile1 in ship1.get_tiles_board_pos():
            for tile2 in ship2.get_tiles_board_pos():
                if tile1[0] == tile2[0] and tile1[1] == tile2[1]:
                    return True
        return False

    def try_remove_ship_at_position(self, coordinates: tuple[int, int]) -> bool:
        for k, ship in self.ships.items():
            for c in ship.get_tiles_board_pos():
                if c == coordinates:
                    self.ships.pop(k)
                    self.ships_left_to_place[ship.ship_type.name] += 1
                    return True
        return False

    def is_valid_ship_placement(self, ship: Ship) -> bool:
        ship_coords = (ship.x, ship.y)
        for c in ship.get_tiles_board_pos():
            if self.are_coords_within_bounds(c) is False:
                return False
        if ship_coords in self.ships.values():
            return False
        for existing_ship in self.ships.values():
            if self.do_ships_overlap(ship, existing_ship):
                return False
        return True

    def placed_all_ships(self):
        for v in self.ships_left_to_place.values():
            if v > 0:
                return False
        return True

    def has_ship_type_left(self, ship_type: ShipType):
        if ship_type is None:
            return False
        return self.ships_left_to_place[ship_type.name] > 0
