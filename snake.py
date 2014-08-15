class Snake:

    def __init__(self, width, height):
        body = []
        x = width / 2
        y = height / 2

        body.append((x, y))
        body.append((x, y + 1))
        body.append((x, y + 2))
        self.body = body
        self.x = x
        self.y = y
        self.size = 3
        self.alive = True
        self.direction = 'up'

    def move(self):
        #if the snake size is too big, delete its tail, otherwise let it grow to however many units
        if self.size < len(self.body):
            del self.body[len(self.body) - 1] #check if im doing self right please lol, deleting its tail
        if self.direction == 'up':
            self.x -= 1
        elif self.direction == 'down':
            self.x += 1
        elif self.direcition == 'left':
            self.y -= 1
        elif self.direction == 'right':
            self.y += 1
        else:
            print('You made a typo')

    @property
    def position(self):
        return self.x, self.y
