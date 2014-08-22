#!/usr/bin/python3

from snake import Snake
from time import sleep

class Ai(Snake):
    def __init__(self, width, height):
        super().__init__(width, height - 5)
        #grid = [[-1 for i in range(width)] for i in range(height - 5)]
        turn_points = [] #tuple -> ((x, y), new_direction)
        apple_loc = self.apple.pos
        self.generate_path()

    def move(self):
        if len(turn_points) > 0:
            if self.position == turn_points[0][0]:
                self.direction = turn_points[0][1]
                del turn_points[0]
            else:
                self.generate_path()
        super().move()
        #apple location moved, recalculate path to it
        if self.apple.pos != apple_loc:
            self.generate_path()

    #implement a* path finding here
    def generate_path(self):
        location_queue = [self.position]
        
        #instead of using priority queue, use regular list and sort it
        #with key function that returns distance to destinatetion
        while len(location_queue) > 0 or self.position != self.apple.pos:
            current = location_queue[0]
            del location_queue[0]
            if x + 1 < self.width:
                location_queue.append((current[0] + 1, current[1]))
            if x - 1 >= 0:
                location_queue.append((current[0] - 1, current[1]))
            if y + 1 < self.height:
                location_queue.append((current[0], current[1] + 1))
            if y - 1 >= 0:
                location_queue.append((current[0], current[1] - 1))
            location_queue.sort(key=self.dist) #priority queue it
            

    def dist(self, val):
        dx = self.apple.x - val[0]
        dy = self.apple.y - val[1]
        to_square = dx * dx + dy * dy
        return to_square ** 2