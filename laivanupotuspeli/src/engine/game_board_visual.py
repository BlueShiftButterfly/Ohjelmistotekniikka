import math
import pygame
from engine.rendering import colors as COLORS
from engine.event_relay import EventRelay
from engine.event import Event

class GameBoardVisual:
    def __init__(self, event_relay: EventRelay, cells_x, cells_y, x, y, cellsize):
        self.event_relay = event_relay
        self.height = cells_x * cellsize
        self.width = cells_y * cellsize
        self.cells_x = cells_x
        self.cells_y = cells_y
        self.x = x
        self.y = y
        self.cellsize = cellsize
        self.surface = pygame.Surface((self.width, self.height))
        self.bg_sprite = pygame.Surface((cellsize, cellsize))
        self.marker_sprite = pygame.Surface((cellsize, cellsize), pygame.SRCALPHA)
        pygame.transform.scale(
            pygame.image.load("src/assets/sea_bg.png").convert(),
            (cellsize, cellsize),
            self.bg_sprite
        )
        pygame.transform.scale(
            pygame.image.load("src/assets/indicator1.png").convert_alpha(),
            (cellsize, cellsize),
            self.marker_sprite
        )
        self.markers: list[tuple[int, int]] = []
        self.event_relay.subscribe(self, self.on_mouse_press, Event.ON_MOUSE0_PRESS)

    def render_background(self):
        for y in range(int(self.cells_y)):
            for x in range(int(self.cells_x)):
                self.surface.blit(self.bg_sprite, (x*self.cellsize, y*self.cellsize))
        for x in range(int(self.cells_x)+1):
            pygame.draw.line(
                self.surface,
                COLORS.GRAY,
                (x*self.cellsize, 0),
                (x*self.cellsize, self.height),
                2
            )
        for y in range(int(self.cells_y)+1):
            pygame.draw.line(
                self.surface,
                COLORS.GRAY,
                (0, y*self.cellsize),
                (self.width, y*self.cellsize),
                2
            )

    def render_markers(self, coordinates: list[tuple]):
        for coord in coordinates:
            self.surface.blit(self.marker_sprite, (coord[0]*self.cellsize, coord[1]*self.cellsize))

    def highlight_square(self, coordinates: tuple[int, int], color: pygame.Color):
        if (self.are_coordinates_within_bounds(coordinates) is False):
            return
        pygame.draw.line(
            self.surface,
            color,
            (coordinates[0]*self.cellsize, coordinates[1]*self.cellsize),
            ((coordinates[0]+1)*self.cellsize, coordinates[1]*self.cellsize),
            2
        )
        pygame.draw.line(
            self.surface,
            color,
            (coordinates[0]*self.cellsize, (coordinates[1]+1)*self.cellsize),
            ((coordinates[0]+1)*self.cellsize, (coordinates[1]+1)*self.cellsize),
            2
        )
        pygame.draw.line(
            self.surface,
            color,
            (coordinates[0]*self.cellsize, coordinates[1]*self.cellsize),
            (coordinates[0]*self.cellsize, (coordinates[1]+1)*self.cellsize),
            2
        )
        pygame.draw.line(
            self.surface,
            color,
            ((coordinates[0]+1)*self.cellsize, coordinates[1]*self.cellsize),
            ((coordinates[0]+1)*self.cellsize, (coordinates[1]+1)*self.cellsize),
            2
        )

    def screen_coords_to_grid_coords(self, coordinates: tuple[int, int]):
        return (
            math.floor((coordinates[0] - self.x) / self.cellsize),
            math.floor((coordinates[1] - self.y) / self.cellsize)
        )

    def are_coordinates_within_bounds(self, coordinates: tuple[int, int]):
        return (0 <= coordinates[0] <= self.cells_x and 0 <= coordinates[1] <= self.cells_y)

    def update(self):
        self.render_background()
        self.render_markers(self.markers)
        self.highlight_square(self.screen_coords_to_grid_coords(pygame.mouse.get_pos()), COLORS.GREEN)

    def on_mouse_press(self):
        grid_pos = self.screen_coords_to_grid_coords(pygame.mouse.get_pos())
        if grid_pos in self.markers:
            return
        self.markers.append(grid_pos)
