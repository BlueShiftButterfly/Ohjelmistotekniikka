import pygame
from engine.rendering import colors as COLORS

class GameBoardVisual:
    def __init__(self, cells_x, cells_y, x, y, cellsize):
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
        self.render_background()
        self.render_markers([(0,0), (5,2), [9,9], [2,6]])

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
