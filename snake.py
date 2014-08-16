class Snake:

    def __init__(self, width, height):
        body = []
        x = width / 2
        y = height / 2
        self.width = width
        self.height = height

        body.append((x, y))
        body.append((x, y + 1))
        body.append((x, y + 2))
        self.body = body
        self.x = x
        self.y = y
        self.size = 3
        self.alive = True
        self.direction = 'up'
        self.apples_consumed = 0
        self.apple = Apple(width, height, self.body)

    def move(self):
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
        #update head (head at end of list, tail at beginning)
        self.body.append((self.x, self.y))
        #if the snake size is too big, delete its tail, otherwise let it grow to however many units
        if self.size < len(self.body) and len(self.body) > 0:
            del self.body[0]
        #check if ate apple
        if self.position() == self.apple.pos:
            self.size += 1
            if self.apple.gold: #increase size by total of 5
                self.size += 4
            self.apple.set_new_pos(self.body)
        #check dead
        if self.out_of_bounds():
            self.alive = False
            #delete current head to prevent index out of bound
            del self.body[len(self.body) - 1]

    def out_of_bounds(self):
        if self.x < 0 or self.y < 0:
            return True
        return self.x >= self.width or self.y >= self.height

    @property
    def position(self):
        return self.x, self.y
