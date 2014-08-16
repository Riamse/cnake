from random import randint

class Apple:
    def __init__(self, width, height, snake_pos):
        self.gold = None
        self.pos = None
        self.width = width
        self.height = height
        self.set_new_pos(snake_pos)

    def random_pos(self, snake_pos):
        self.gold = (randint(0, 100) < 3)
        loc = randint(0, self.width), randint(0, self.height)
        while loc in snake_pos:
            loc = randint(0, self.width), randint(0, self.height)
        return loc

    def set_new_pos(self, snake_pos):
        self.pos = self.random_pos(snake_pos)