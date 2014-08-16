from random import randrange
import time

class Apple:
    def __init__(self, width, height, snake_pos):
        self.gold = None
        self.pos = None
        self.width = width
        self.height = height
        self.set_new_pos(snake_pos)

    def random_pos(self, snake_pos):
        self.gold = (randrange(0, 100) < 3)
        loc = randrange(0, self.width), randrange(0, self.height)
        while loc in snake_pos or loc == self.pos:
            loc = randrange(0, self.width), randrange(0, self.height)
        return loc

    def set_new_pos(self, snake_pos):
        self.pos = self.random_pos(snake_pos)

    @property
    def position(self):
        return self.pos

    @property
    def x(self):
        return self.pos[0]

    @property
    def y(self):
        return self.pos[1]

