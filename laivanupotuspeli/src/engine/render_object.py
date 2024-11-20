from engine.abstract_render_dirty import AbstractRenderDirty

class RenderComponent(AbstractRenderDirty):
    def __init__(self, parent_layer: AbstractRenderDirty, surface):
        self._parent_layer = parent_layer
        self._surface = None

    def set_dirty(self):
        self._parent_layer.set_dirty()

    @property
    def surface(self):
        pass

    @property
    def rect(self):
        pass
