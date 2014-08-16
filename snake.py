#!/usr/bin/python3

from apple import Apple


class Snake:

    def __init__(self, width, height):
        # body[0] is the tail, body[-1] is the head
        x = width // 2
        y = height // 2
        self.width = width
        self.height = height

        body = [(x, y + 2), (x, y + 1), (x, y)]
        self.body = body
        self.x = x
        self.y = y
        self.size = 3
        self.alive = True
        self.direction = 'left'
        self.apples_consumed = 0
        self.apple = Apple(width, height, self.body)

    def move(self):
        # since curses is based off of the top left corner, we need to make
        # these functions appear to be backwards
        if self.direction == 'up':
            self.y -= 1
        elif self.direction == 'down':
            self.y += 1
        elif self.direction == 'left':
            self.x -= 1
        elif self.direction == 'right':
            self.x += 1
        else:
            print('You made a typo')
        #check if ate apple
        if self.position == self.apple.pos:
            self.size += 1
            if self.apple.gold: #increase size by total of 5
                self.size += 4
            self.apple.set_new_pos(self.body)
        #check dead
        if self.out_of_bounds or self.position in self.body:
            self.alive = False
            #delete current head to prevent index out of bound
            del self.body[-1]
        #update head (head at end of list, tail at beginning)
        self.body.append((self.x, self.y))
        #if the snake size is too big, delete its tail, otherwise let it grow to however many units
        if len(self.body) > self.size:
            del self.body[0]

    def set_direction(self, direction):
        if not direction:
            return
        if self.direction == 'up' and direction == 'down':
            return
        if self.direction == 'left' and direction == 'right':
            return
        if self.direction == 'right' and direction == 'left':
            return
        if self.direction == 'down' and direction == 'up':
            return
        self.direction = direction

    @property
    def out_of_bounds(self):
        if self.x < 0 or self.y < 0:
            return True
        return self.x >= self.width or self.y >= self.height

    @property
    def position(self):
        return self.x, self.y
