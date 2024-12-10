from game.guess import Guess
from game.ship import Ship

class Board:
    def __init__(self, width: int, height: int):
        self.width = width
        self.height = height
        self.ships: dict[tuple[int, int], Ship] = {}
        self.opponent_guesses: dict[tuple[int, int], Guess] = {}

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
        ship_coords = (ship.x, ship.y)
        if self.are_coords_within_bounds(ship_coords) is False:
            return False
        if ship_coords in self.ships:
            return False
        for existing_ship in self.ships:
            if self.do_ships_overlap(ship, existing_ship):
                return False
        self.ships[ship_coords] = ship
        return True

    def do_ships_overlap(self, ship1: Ship, ship2: Ship):
        for tile1 in ship1.get_tiles_board_pos():
            for tile2 in ship2.get_tiles_board_pos():
                if tile1 == tile2:
                    return True
        return False
