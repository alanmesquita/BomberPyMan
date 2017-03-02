import os
import pygame
from pygame.locals import *
import pygame.time

from events import AVAIABLE_EVENTS
from consts import SCREEN_WIDTH, SCREEN_HEIGHT, BACKGROUND_COLOR, MOVEMENT_KEYS
from scenarios import SCENARIOS
from elements.wall import Wall
from elements.player import Player


class MapManager(object):
    def __init__(self):
        self._itens = []

    @property
    def itens(self):
        return self._itens

    @itens.setter
    def itens(self, value):
        self._itens.append(value)

    def create_from_map(self, map_schema):
        x = y = 0
        for row in map_schema:
            for col in row:
                if col == '#':
                    self.itens = Wall(x, y)
                x += 16
            y += 16
            x = 0


class GameMain(object):
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.screen = pygame.display.set_mode((self.width, self.height))

        self.background = self._get_background()
        self.map_manager = MapManager()
        self.map_manager.create_from_map(SCENARIOS['1']().layout)
        self.player = Player(16, 16)

    def loop(self):
        clock = self._get_clock()
        while 1:
            millis = clock.tick(60)
            self._run_events()
            self._keyboard_event()
            self.draw()
            pygame.display.flip()

    def draw(self):
        # Fill background with color
        self.screen.fill(BACKGROUND_COLOR)

        # Draw map
        for item in self.map_manager.itens:
            pygame.draw.rect(self.screen, item.color, item.shape)

        pygame.draw.rect(self.screen, self.player.color, self.player.shape)

    def _keyboard_event(self):
        key = pygame.key.get_pressed()

        for movement_key in MOVEMENT_KEYS:
            if key[movement_key]:
                self.player.move(movement_key, self.map_manager.itens)

    def _get_clock(self):
        return pygame.time.Clock()

    def _get_background(self):
        background = pygame.Surface(
            (self.screen.get_width(), self.screen.get_height())
        )
        background.fill(BACKGROUND_COLOR)
        return background.convert()

    def _run_events(self):
        for event in pygame.event.get():
            if event.type in AVAIABLE_EVENTS:
                AVAIABLE_EVENTS[event.type]().execute()


if __name__ == "__main__":
    game_main = GameMain(SCREEN_WIDTH, SCREEN_HEIGHT)
    game_main.loop()
