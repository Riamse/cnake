#!/usr/bin/python3

from snake import Snake
from time import sleep
from copy import deepcopy

class Ai(Snake):
    def __init__(self, width, height):
        Snake.__init__(self, width, height - 5)
        self.travel_points = []
        self.apple_loc = self.apple.pos
        #DEBUG
        #self.f = open('log.out', 'w')
        self.generate_path()
        self.quit = False
        self.start = False

    def move(self):
        if self.travel_points:
            self.x, self.y = self.travel_points.pop(0)
        Snake.move(self, by_dir=False)
        #apple location moved, recalculate path to it
        if self.apple.pos != self.apple_loc:
            self.generate_path()
            self.apple_loc = self.apple.pos

    #implement a* path finding here
    def generate_path(self):
        location_queue = [(self.position, deepcopy(self.body))]
        came_from = {}
        came_from[self.position] = None

        #instead of using priority queue, use regular list and sort it
        #with key function that returns distance to destinatetion
        while len(location_queue) > 0:
            current = location_queue.pop(0)
            moving_wall = deepcopy(current[1])
            current = current[0]

            if current == self.apple.pos:
                travel_points = []
                track_current = current
                while came_from[track_current] != None:
                    # construct the path by backtracking from the apple
                    # to our starting point
                    travel_points.append(track_current)
                    track_current = came_from[track_current]
                #travel_points.sort(key=self.dist)
                self.travel_points = travel_points[::-1]
                """
                #DEBUG STUFF
                self.f.write('=========================\n')
                self.f.write(str(self.travel_points))
                self.f.write('\n')
                grid = [['.' for i in range(self.width)] for i in range(self.height)]
                for item in travel_points:
                    x, y = item
                    grid[y][x] = 'X'
                grid[self.y][self.x] = 'S'
                for i in grid:
                    for j in i:
                        self.f.write(j)
                    self.f.write('\n')
                #DEBUG STUFF
                """
                break
            neighbors = self.get_adjacent_locs(current, moving_wall)
            for next in neighbors:
                if next not in came_from:
                    next_moving_wall = deepcopy(moving_wall)
                    if len(next_moving_wall) > self.size:
                        del next_moving_wall[0]
                    next_moving_wall.append(next)
                    location_queue.append((next, next_moving_wall))
                    came_from[next] = current
            location_queue.sort(key=self.dist) #priority queue it

    def adjacent(self, a, b):
        if abs(a[0] - b[0]) <= 1 and a[1] == b[1] or abs(a[1] - b[1]) <= 1 and a[0] == b[0]:
            return True
        return False

    def get_dir(self, pt1, pt2):
        if pt2[0] == pt1[0] and pt2[1] != pt1[1]: #vertical
            if pt2[1] > pt1[1]:
                return 'down'
            else:
                return 'up'
        #horizontal
        if pt2[0] > pt1[0]:
                return 'right'
        return 'left'

    def dist(self, val):
        val = val[0]
        dx = self.apple.x - val[0]
        dy = self.apple.y - val[1]
        #to_square = dx * dx + dy * dy
        #return to_square ** 2
        return abs(dx) + abs(dy) + self.width - val[0]

    def get_adjacent_locs(self, location, moving_wall):
        neighbors = []
        if location[0] + 1 < self.width:
            neighbors.append((location[0] + 1, location[1]))
        if location[0] - 1 >= 0:
            neighbors.append((location[0] - 1, location[1]))
        if location[1] + 1 < self.height:
            neighbors.append((location[0], location[1] + 1))
        if location[1] - 1 >= 0:
            neighbors.append((location[0], location[1] - 1))
        return list(set(neighbors) - set(moving_wall))
