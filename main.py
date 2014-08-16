#!/usr/bin/python3

import os
import sys
import traceback
import curses
from time import sleep

from snake import Snake
from apple import Apple

class Color():
    BLACK = 1 #snake color
    GREEN = 2 #apple color
    GOLD = 3 #apple golden color

dir_dict = {curses.KEY_UP: "up", curses.KEY_DOWN: "down", curses.KEY_LEFT: "left", curses.KEY_RIGHT: "right"}
WIDTH, HEIGHT = 80, 24#os.get_terminal_size()

def main(window):
    curses.use_default_colors()
    curses.init_pair(Color.BLACK, curses.COLOR_BLACK, curses.COLOR_BLACK)
    curses.init_pair(Color.GREEN, curses.COLOR_GREEN, curses.COLOR_BLACK)
    curses.init_pair(Color.GOLD, curses.COLOR_YELLOW, curses.COLOR_BLACK)
    #for i in range(0, curses.COLORS):
        #curses.init_pair(i, i, -1)
    curses.curs_set(0)  # invisible cursor
    window.nodelay(1)
    window.clear()

    snake = Snake(WIDTH, HEIGHT)

    while snake.alive:
        apple_colour = curses.color_pair(Color.GOLD) if snake.apple.gold else curses.color_pair(Color.GREEN)
        window.addch(snake.apple.y, snake.apple.x, b"A", apple_colour)
        window.move(0, 0)
        window.addch(snake.body[-1][1], snake.body[-1][0], b"X")
        for x, y in snake.body[:-1]:
            window.addch(y, x, b"O")
            window.refresh()
            #sleep(0.01)  # curses is retarded
        window.refresh()
        sleep(0.05)
        window.clear()
        ch = window.getch()
        if ch == ord("q"):
            snake.alive = False
        snake.set_direction(dir_dict.get(ch, None))
        snake.move()


if __name__ == '__main__':
    try:
        curses.wrapper(main)
    except curses.error:
        raise
    except Exception:
        traceback.print_exc()
        raise SystemExit(0)