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
        came_from = {}
        cost_at = {}
        came_from[location_queue[0]] = None
        cost_at[location_queue[0]] = 0
        #instead of using priority queue, use regular list and sort it
        #with key function that returns distance to destinatetion
        while len(location_queue) > 0:
            current = location_queue[0]
            del location_queue[0]
            if current == self.apple.pos:
                print('Target found')
                sleep(3)
                break
                #implement backtrack
            neighbors = self.get_adjacent_locs(current)
            for next in neighbors:
                new_cost = cost_at[current] + 1
                if next not in cost_at or new_cost < cost_at[next]:
                    cost_at[next] = new_cost
                    location_queue.append(next)
                    came_from[next] = current
            location_queue.sort(key=self.dist) #priority queue it

    def dist(self, val):
        dx = self.apple.x - val[0]
        dy = self.apple.y - val[1]
        to_square = dx * dx + dy * dy
        return to_square ** 2

    def get_adjacent_locs(self, location):
        neighbors = []
        if location[0] + 1 < self.width:
            neighbors.append((location[0] + 1, location[1]))
        if location[0] - 1 >= 0:
            neighbors.append((location[0] - 1, location[1]))
        if location[1] + 1 < self.height:
            neighbors.append((location[0], location[1] + 1))
        if location[1] - 1 >= 0:
            neighbors.append((location[0], location[1] - 1))
        return neighbors