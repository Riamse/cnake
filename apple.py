from random import randint

class Apple:
    def __init__(self, width, height, snake_pos):
        self.pos = self.random_pos(width, height, snake_pos)
        self.gold = (randint(0, 100) < 3)

    def random_pos(width, height, snake_pos):
        loc = randint(0, width), randint(0, height)
        while loc in snake_pos:
            loc = randint(0, width), randint(0, height)
        return loc

