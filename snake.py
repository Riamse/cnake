class Snake:

    def __init__(self, width, height):
        self.pos = (width / 2, height / 2)
        self.alive = True
        self.size = 3
        self.body = []
        self.body.append(pos)
        self.body.append((pos[0], pos[1] + 1))
        self.body.append((pos[0], pos[1] + 2))
        self.direction = 'up'

    def move(self):
        #if the snake size is too big, delete its tail, otherwise let it grow to however many units
        if self.size < len(self.body):
            del self.body[len(self.body) - 1] #check if im doing self right please lol, deleting its tail
        if self.direction == 'up':
            self.pos = (self.pos[0] - 1, self.pos[1])
        elif self.direction == 'down':
            self.pos = (self.pos[0] + 1, self.pos[1])
        elif self.direcition == 'left':
            self.pos = (self.pos[0], self.pos[1] - 1)
        elif self.direction == 'right':
            self.pos = (self.pos[0], self.pos[1] + 1)
        else:
            print('You made a typo')

