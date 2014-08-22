#!/usr/bin/python3

from snake import Snake

class Ai(Snake):
    def __init__(self, width, height):
        super().__init__(width, height - 5)
        grid = [[0 for i in range(width)] for i in range(height - 5)]
        turn_points = [] #tuple -> ((x, y), new_direction)
        apple_loc = self.apple.pos

    def move(self):
        if len(turn_points) > 0:
            if self.position() == turn_points[0][0]:
                self.direction = turn_points[0][1]
                del turn_points[0]
            else:
                self.generate_path()
        super().move()
        #apple location moved, recalculate path to it
        if self.apple.pos != apple_loc:
            self.generate_path()

    #a* implementation of path finding
    def generate_path(self):
        location_queue = [self.position()]
        while len(location_queue > 0) or self.position() != self.apple.pos:
            pass #implement priority queue heuristic algo