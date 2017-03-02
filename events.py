import sys
import pygame


class Event(object):
    def execute(self):
        pass


class QuitEvent(Event):
    def execute(self):
        sys.exit()


AVAIABLE_EVENTS = {
    pygame.QUIT: QuitEvent
}
