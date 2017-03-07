from .base import AnimatedElement
from pygame import Rect, K_LEFT, K_RIGHT, K_UP, K_DOWN
from consts import UP_KEY, DOWN_KEY, RIGHT_KEY, LEFT_KEY


class Player(AnimatedElement):
    speed = 1
    color = (228, 228, 228)
    command_map = {
        UP_KEY: [0, -speed],
        DOWN_KEY: [0, speed],
        RIGHT_KEY: [speed, 0],
        LEFT_KEY: [-speed, 0],
    }

    def _shape(self, x, y):
        return Rect(x, y, self.width, self.height)

    def move(self, key, colision_itens):
        directions = self.command_map.get(key)
        self.move_single_axis(*directions)
        self.make_colision(colision_itens, *directions)

    def move_single_axis(self, dx, dy):
        self.shape.x += dx
        self.shape.y += dy

    def make_colision(self, colision_itens, dx, dy):
        for wall in colision_itens:
            if self.shape.colliderect(wall.shape):
                if dx > 0:
                    self.shape.right = wall.shape.left
                    if wall.is_lazy:
                        if self.shape.centery < wall.shape.centery:
                            self.move(UP_KEY, colision_itens)
                        else:
                            self.move(DOWN_KEY, colision_itens)
                if dx < 0:
                    self.shape.left = wall.shape.right
                    if wall.is_lazy:
                        if self.shape.centery < wall.shape.centery:
                            self.move(UP_KEY, colision_itens)
                        else:
                            self.move(DOWN_KEY, colision_itens)
                if dy > 0:
                    self.shape.bottom = wall.shape.top
                    if wall.is_lazy:
                        if self.shape.centerx > wall.shape.centerx:
                            self.move(RIGHT_KEY, colision_itens)
                        else:
                            self.move(LEFT_KEY, colision_itens)
                if dy < 0:
                    self.shape.top = wall.shape.bottom
                    if wall.is_lazy:
                        if self.shape.centerx < wall.shape.centerx:
                            self.move(LEFT_KEY, colision_itens)
                        else:
                            self.move(RIGHT_KEY, colision_itens)

