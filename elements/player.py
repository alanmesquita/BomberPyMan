from .base import AnimatedElement
from pygame import Rect, K_LEFT, K_RIGHT, K_UP, K_DOWN
from consts import UP_KEY, DOWN_KEY, RIGHT_KEY, LEFT_KEY


class Player(AnimatedElement):
    speed = 1
    color = (0, 0, 0)
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
                if dx < 0:
                    self.shape.left = wall.shape.right
                if dy > 0:
                    self.shape.bottom = wall.shape.top
                if dy < 0:
                    self.shape.top = wall.shape.bottom
