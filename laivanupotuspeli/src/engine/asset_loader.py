import pygame
from game.direction import Direction

class AssetLoader:
    """
    Class responsible for loading game assets like sprites.
    """
    def __init__(self):
        self.ship_sprites = {}
        self.sprites = {}

    def load(self):
        """
        Loads all game assets and creates asset dictionaries.
        """
        self.ship_sprites = {
            "2x1": 
            {
                Direction.HORIZONTAL: pygame.transform.rotate(
                    pygame.image.load("src/assets/ship1.png").convert_alpha(),
                    90
                ),
                Direction.VERTICAL: pygame.image.load("src/assets/ship1.png").convert_alpha()
            },
            "3x1": 
            {
                Direction.HORIZONTAL: pygame.transform.rotate(
                    pygame.image.load("src/assets/ship2.png").convert_alpha(),
                    90
                ),
                Direction.VERTICAL: pygame.image.load("src/assets/ship2.png").convert_alpha()
            },
            "4x1": 
            {
                Direction.HORIZONTAL: pygame.transform.rotate(
                    pygame.image.load("src/assets/ship3.png").convert_alpha(),
                    90
                ),
                Direction.VERTICAL: pygame.image.load("src/assets/ship3.png").convert_alpha()
            }
        }
        self.sprites = {
            "sea_bg": pygame.image.load("src/assets/sea_bg.png").convert(),
            "red_marker": pygame.image.load("src/assets/indicator1.png").convert_alpha(),
            "miss_marker": pygame.image.load("src/assets/indicator2.png").convert_alpha()
        }
