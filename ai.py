#!/usr/bin/python3

from snake import Snake
from time import sleep
from copy import deepcopy

class Ai(Snake):
    def __init__(self, width, height):
        super().__init__(width, height - 5)
        self.travel_points = []
        self.apple_loc = self.apple.pos
        #DEBUG
        self.f = open('log.out', 'w')
        self.generate_path()

    def move(self):
        if self.travel_points:
            self.x, self.y = self.travel_points.pop(0)
        super().move(by_dir=False)
        #apple location moved, recalculate path to it
        if self.apple.pos != self.apple_loc:
            self.generate_path()
            self.apple_loc = self.apple.pos

    #implement a* path finding here
    def generate_path(self):
        location_queue = [self.position]
        came_from = {}
        cost_at = {}
        came_from[location_queue[0]] = None
        cost_at[location_queue[0]] = 0

        #fix moving wall
        """
        moving_wall = [(self.body[i], i) for i in enumerate(self.body)]
        visited = deepcopy(moving_wall)
        depth = len(moving_wall) + 1
        """
        #instead of using priority queue, use regular list and sort it
        #with key function that returns distance to destinatetion
        while len(location_queue) > 0:
            current = location_queue[0]
            del location_queue[0]
            """
            visited.append((current, depth))
            depth += 1
            visited.sort(key=lambda coordinate: coordinate[1])
            #remove lowest depth item
            lowest = moving_wall[0]
            for compare in moving_wall[1:]:
                if compare[1] < lowest[1]:
                    lowest = compare
            moving_wall
            """
            if current == self.apple.pos:
                travel_points = []
                track_current = current
                while came_from[track_current] != None:
                    travel_points.append(track_current)
                    track_current = came_from[track_current]
                #travel_points.sort(key=self.dist)
                self.travel_points = travel_points[::-1]
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
                break
            #neighbors = self.get_adjacent_locs(current, moving_wall)
            neighbors = self.get_adjacent_locs(current, self.body)
            for next in neighbors:
                new_cost = cost_at[current] + 1
                if next not in cost_at or new_cost < cost_at[next]:
                    cost_at[next] = new_cost
                    location_queue.append(next)
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
        dx = self.apple.x - val[0]
        dy = self.apple.y - val[1]
        to_square = dx * dx + dy * dy
        return to_square ** 2

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
