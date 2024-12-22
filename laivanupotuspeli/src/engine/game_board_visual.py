import math
import pygame
from engine.rendering import colors as COLORS
from engine.event_relay import EventRelay
from engine.event import Event
from game.ship import Ship, SHIP_TYPES
from game.direction import Direction
from engine.asset_loader import AssetLoader
from engine.rendering.abstract_renderable import AbstractRenderable

class GameBoardVisual(AbstractRenderable):
    def __init__(self, event_relay: EventRelay, asset_loader: AssetLoader, cells_x: int, cells_y: int, x: int, y: int, cell_size: int, enabled: bool = True):
        self.event_relay = event_relay
        self.asset_loader = asset_loader
        self.height = cells_x * cell_size
        self.width = cells_y * cell_size
        self.cells_x = cells_x
        self.cells_y = cells_y
        self.x = x
        self.y = y
        self.cell_size = cell_size
        self.board_surface = pygame.Surface((self.width, self.height))

        self.bg_sprite = self.scale_sprite_to_cell_size(self.asset_loader.sprites["sea_bg"])
        self.hit_marker_sprite = self.scale_sprite_to_cell_size(self.asset_loader.sprites["red_marker"], True)
        self.miss_marker_sprite = self.scale_sprite_to_cell_size(self.asset_loader.sprites["miss_marker"], True)
        self.event_relay.subscribe(self, self.update, Event.ON_RENDER)
        self.hit_markers: list[tuple[int, int]] = []
        self.miss_markers: list[tuple[int, int]] = []
        self.board_ships = []
        self.preview_ships = []

        self.do_draw_ships = True

        self._enabled = enabled

    def render_background(self):
        for y in range(int(self.cells_y)):
            for x in range(int(self.cells_x)):
                self.board_surface.blit(self.bg_sprite, (x*self.cell_size, y*self.cell_size))
        for x in range(int(self.cells_x)+1):
            pygame.draw.line(
                self.board_surface,
                COLORS.GRAY,
                (x*self.cell_size, 0),
                (x*self.cell_size, self.height),
                2
            )
        for y in range(int(self.cells_y)+1):
            pygame.draw.line(
                self.board_surface,
                COLORS.GRAY,
                (0, y*self.cell_size),
                (self.width, y*self.cell_size),
                2
            )

    def render_markers(self, coordinates: list[tuple], is_hit_marker = False):
        s = self.hit_marker_sprite
        if is_hit_marker is False:
            s = self.miss_marker_sprite
        for coord in coordinates:
            self.board_surface.blit(s, (coord[0]*self.cell_size, coord[1]*self.cell_size))

    def highlight_square(self, coordinates: tuple[int, int], color: pygame.Color):
        if self.are_coordinates_within_bounds(coordinates) is False:
            return
        pygame.draw.line(
            self.board_surface,
            color,
            (coordinates[0]*self.cell_size, coordinates[1]*self.cell_size),
            ((coordinates[0]+1)*self.cell_size, coordinates[1]*self.cell_size),
            2
        )
        pygame.draw.line(
            self.board_surface,
            color,
            (coordinates[0]*self.cell_size, (coordinates[1]+1)*self.cell_size),
            ((coordinates[0]+1)*self.cell_size, (coordinates[1]+1)*self.cell_size),
            2
        )
        pygame.draw.line(
            self.board_surface,
            color,
            (coordinates[0]*self.cell_size, coordinates[1]*self.cell_size),
            (coordinates[0]*self.cell_size, (coordinates[1]+1)*self.cell_size),
            2
        )
        pygame.draw.line(
            self.board_surface,
            color,
            ((coordinates[0]+1)*self.cell_size, coordinates[1]*self.cell_size),
            ((coordinates[0]+1)*self.cell_size, (coordinates[1]+1)*self.cell_size),
            2
        )

    def screen_to_grid_coords(self, coordinates: tuple[int, int]) -> tuple[int, int]:
        return (
            math.floor((coordinates[0] - self.x) / self.cell_size),
            math.floor((coordinates[1] - self.y) / self.cell_size)
        )

    def are_coordinates_within_bounds(self, coordinates: tuple[int, int]):
        return (0 <= coordinates[0] <= self.cells_x and 0 <= coordinates[1] <= self.cells_y)

    def scale_sprite_to_cell_size(self, sprite: pygame.Surface, alpha: bool = False):
        flags = 0
        if (alpha):
            flags = pygame.SRCALPHA
        surf = pygame.Surface((self.cell_size, self.cell_size), flags)
        pygame.transform.scale(
            sprite,
            (self.cell_size, self.cell_size),
            surf
        )
        return surf

    def update(self, delta: float):
        if self._enabled is False:
            return
        self.render_background()
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
        return (self.x, self.y)

    @property
    def surface(self) -> pygame.Surface:
        return self.board_surface

    def draw_ship(self, ship: Ship):
        y_mod = 0
        if ship.direction == Direction.VERTICAL:
            y_mod = (len(ship.ship_type.get_tiles(Direction.HORIZONTAL))-1) * -1
        self.board_surface.blit(
            self.asset_loader.ship_sprites[ship.ship_type.name][ship.direction],
            (ship.x*self.cell_size, (ship.y + y_mod)*self.cell_size)
        )

    def draw_ship_preview(self, ship_type: str, dir: Direction, pos: tuple[int, int]):
        y_mod = 0
        if dir == Direction.VERTICAL:
            y_mod = (len(SHIP_TYPES[ship_type].get_tiles(Direction.HORIZONTAL))-1) * -1
        surf = self.asset_loader.ship_sprites[SHIP_TYPES[ship_type].name][dir].copy()
        surf.set_alpha(128)
        self.board_surface.blit(
            surf,
            (pos[0]*self.cell_size, (pos[1] + y_mod)*self.cell_size)
        )
