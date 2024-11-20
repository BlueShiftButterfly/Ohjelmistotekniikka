import pygame
from engine.abstract_render_dirty import AbstractRenderDirty

class RenderLayer(AbstractRenderDirty):
    def __init__(self, priority: int = 0):
        self._surface: pygame.Surface = pygame.Surface(100, 100)
        self._priority = priority
        self._render_components = []
        self._is_dirty = False

    def set_dirty(self):
        self._is_dirty = True

    def update(self):
        if self._is_dirty is False:
            return
        [self._surface.blit(component.surface, component.rect) for component in self._render_components]

    @property
    def surface(self):
        pass

    @property
    def rect(self):
        pass
