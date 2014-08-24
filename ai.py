#!/usr/bin/python3

from snake import Snake
from time import sleep

class Ai(Snake):
    def __init__(self, width, height):
        super().__init__(width, height - 5)
        #grid = [[-1 for i in range(width)] for i in range(height - 5)]
        turn_points = [] #tuple -> ((x, y), new_direction)
        self.apple_loc = self.apple.pos
        self.generate_path()

    def move(self):
        if len(self.turn_points) > 0:
            if self.position == self.turn_points[0][0]:
                self.direction = self.turn_points[0][1]
                del self.turn_points[0]
        super().move()
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
        #instead of using priority queue, use regular list and sort it
        #with key function that returns distance to destinatetion
        while len(location_queue) > 0:
            current = location_queue[0]
            del location_queue[0]
            if current == self.apple.pos:
                travel_points = []
                track_current = current
                while came_from[track_current] != None:
                    travel_points.append(track_current)
                    track_current = came_from[track_current]
                travel_points.sort(key=self.dist)
                self.turn_points = self.find_turn_points(travel_points[::-1])
                break
            neighbors = self.get_adjacent_locs(current)
            for next in neighbors:
                new_cost = cost_at[current] + 1
                if next not in cost_at or new_cost < cost_at[next]:
                    cost_at[next] = new_cost
                    location_queue.append(next)
                    came_from[next] = current
            location_queue.sort(key=self.dist) #priority queue it

    def find_turn_points(self, travel_points):
        f = open('log.out', 'w')
        f.write('Position:')
        f.write(str(self.position))
        f.write('\nApple:')
        f.write(str(self.apple.pos))
        f.write('\nAll Path:')
        f.write(str(travel_points))
        f.write('\nTurn Path:')
        turns = []
        if len(travel_points) == 2:
            new_direction = self.get_dir(travel_points[1], travel_points[0])
            turns.append((travel_points[1], new_direction))
            return turns
        loc = travel_points[0]
        current_direction = self.get_dir(travel_points[0], travel_points[1])
        for point in travel_points[1:]:
            new_direction = self.get_dir(loc, point)
            if new_direction != current_direction:
                turns.append((loc, new_direction))
                current_direction = new_direction
            loc = point
        f.write(str(turns))
        f.write('\n\n')
        grid = [['.' for i in range(self.width)] for i in range(self.height)]
        for item in travel_points:
            x, y = item
            grid[y][x] = 'X'
        grid[self.y][self.x] = 'S'
        for i in grid:
            for j in i:
                f.write(j)
            f.write('\n')
        f.close()
        #print('finish')
        #sleep(20)
        return turns

    #get direction of pt1 -> pt2
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