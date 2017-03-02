from .base import StaticElement
from pygame import Rect


class Wall(StaticElement):
    color = (153, 0, 153)

    def _shape(self, x, y):
        return Rect(x, y, self.width, self.height)
