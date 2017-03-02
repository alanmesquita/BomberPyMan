class Element(object):
    color = (0, 0, 0)

    def __init__(self, x, y, width=16, height=16):
        self.width, self.height = width, height
        self.shape = self._shape(x, y)

    def _shape(self, x, y):
        pass


class StaticElement(Element):
    is_static = True


class AnimatedElement(Element):
    speed = 0
    animation_speed = 0
