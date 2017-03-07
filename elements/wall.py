from .base import StaticElement
from pygame import Rect


class Wall(StaticElement):
    color = (199, 199, 199)
    is_lazy = False

    def _shape(self, x, y):
        return Rect(x, y, self.width, self.height)


class LazyWall(Wall):
    is_lazy = True
