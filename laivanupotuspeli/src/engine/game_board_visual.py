import math
import pygame
from game.ship import Ship, SHIP_TYPES
from game.direction import Direction
from engine.rendering import colors as COLORS
from engine.event_relay import EventRelay
from engine.event import Event
from engine.asset_loader import AssetLoader
from engine.rendering.abstract_renderable import AbstractRenderable

class GameBoardVisual(AbstractRenderable):
    def __init__(
            self,
            event_relay: EventRelay,
            asset_loader: AssetLoader,
            cells_x: int,
            cells_y: int,
            x: int,
            y: int,
            cell_size: int,
            enabled: bool = True
        ):
        self._event_relay = event_relay
        self._asset_loader = asset_loader
        self._height = cells_x * cell_size
        self._width = cells_y * cell_size
        self._cells_x = cells_x
        self._cells_y = cells_y
        self._x = x
        self._y = y
        self._cell_size = cell_size
        self._board_surface = pygame.Surface((self._width, self._height))

        self._bg_sprite = self.scale_sprite(self._asset_loader.sprites["sea_bg"])
        self._hit_marker_sprite = self.scale_sprite(self._asset_loader.sprites["red_marker"], True)
        self._miss_marker_sprite = self.scale_sprite(self._asset_loader.sprites["miss_marker"], True)
        self._event_relay.subscribe(self, self.update, Event.ON_RENDER)
        self.hit_markers: list[tuple[int, int]] = []
        self.miss_markers: list[tuple[int, int]] = []
        self.board_ships = []
        self.preview_ships = []

        self.do_draw_ships = True

        self._enabled = enabled

    def _render_background(self):
        for y in range(int(self._cells_y)):
            for x in range(int(self._cells_x)):
                self._board_surface.blit(self._bg_sprite, (x*self._cell_size, y*self._cell_size))
        for x in range(int(self._cells_x)+1):
            pygame.draw.line(
                self._board_surface,
                COLORS.GRAY,
                (x*self._cell_size, 0),
                (x*self._cell_size, self._height),
                2
            )
        for y in range(int(self._cells_y)+1):
            pygame.draw.line(
                self._board_surface,
                COLORS.GRAY,
                (0, y*self._cell_size),
                (self._width, y*self._cell_size),
                2
            )

    def render_markers(self, coordinates: list[tuple], is_hit_marker = False):
        s = self._hit_marker_sprite
        if is_hit_marker is False:
            s = self._miss_marker_sprite
        for coord in coordinates:
            self._board_surface.blit(s, (coord[0]*self._cell_size, coord[1]*self._cell_size))

    def highlight_square(self, coordinates: tuple[int, int], color: pygame.Color):
        if self.are_coordinates_within_bounds(coordinates) is False:
            return
        pygame.draw.line(
            self._board_surface,
            color,
            (coordinates[0]*self._cell_size, coordinates[1]*self._cell_size),
            ((coordinates[0]+1)*self._cell_size, coordinates[1]*self._cell_size),
            2
        )
        pygame.draw.line(
            self._board_surface,
            color,
            (coordinates[0]*self._cell_size, (coordinates[1]+1)*self._cell_size),
            ((coordinates[0]+1)*self._cell_size, (coordinates[1]+1)*self._cell_size),
            2
        )
        pygame.draw.line(
            self._board_surface,
            color,
            (coordinates[0]*self._cell_size, coordinates[1]*self._cell_size),
            (coordinates[0]*self._cell_size, (coordinates[1]+1)*self._cell_size),
            2
        )
        pygame.draw.line(
            self._board_surface,
            color,
            ((coordinates[0]+1)*self._cell_size, coordinates[1]*self._cell_size),
            ((coordinates[0]+1)*self._cell_size, (coordinates[1]+1)*self._cell_size),
            2
        )

    def screen_to_grid_coords(self, coordinates: tuple[int, int]) -> tuple[int, int]:
        return (
            math.floor((coordinates[0] - self._x) / self._cell_size),
            math.floor((coordinates[1] - self._y) / self._cell_size)
        )

    def are_coordinates_within_bounds(self, coordinates: tuple[int, int]):
        return (0 <= coordinates[0] <= self._cells_x and 0 <= coordinates[1] <= self._cells_y)

    def scale_sprite(self, sprite: pygame.Surface, alpha: bool = False):
        flags = 0
        if alpha:
            flags = pygame.SRCALPHA
        surf = pygame.Surface((self._cell_size, self._cell_size), flags)
        pygame.transform.scale(
            sprite,
            (self._cell_size, self._cell_size),
            surf
        )
        return surf

    def update(self, delta: float):
        if self._enabled is False:
            return
        self._render_background()
        if self.do_draw_ships:
            for s in self.board_ships:
                self.draw_ship(s)
        self.render_markers(self.hit_markers, True)
        self.render_markers(self.miss_markers, False)

    @property
    def enabled(self) -> bool:
        return self._enabled

    @enabled.setter
    def enabled(self, value: bool):
        self._enabled = value

    @property
    def position(self) -> tuple[int, int]:
        return (self._x, self._y)

    @property
    def surface(self) -> pygame.Surface:
        return self._board_surface

    def draw_ship(self, ship: Ship):
        y_mod = 0
        if ship.direction == Direction.VERTICAL:
            y_mod = (len(ship.ship_type.get_tiles(Direction.HORIZONTAL))-1) * -1
        self._board_surface.blit(
            self._asset_loader.ship_sprites[ship.ship_type.name][ship.direction],
            (ship.x*self._cell_size, (ship.y + y_mod)*self._cell_size)
        )

    def draw_ship_preview(self, ship_type: str, direction: Direction, pos: tuple[int, int]):
        y_mod = 0
        if direction == Direction.VERTICAL:
            y_mod = (len(SHIP_TYPES[ship_type].get_tiles(Direction.HORIZONTAL))-1) * -1
        surf = self._asset_loader.ship_sprites[SHIP_TYPES[ship_type].name][direction].copy()
        surf.set_alpha(128)
        self._board_surface.blit(
            surf,
            (pos[0]*self._cell_size, (pos[1] + y_mod)*self._cell_size)
        )
