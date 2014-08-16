#!/usr/bin/python3

import os
import sys
import traceback
import curses
from time import sleep

from snake import Snake
from apple import Apple

dir_dict = {curses.KEY_UP: "up", curses.KEY_DOWN: "down", curses.KEY_LEFT: "left", curses.KEY_RIGHT: "right"}
WIDTH, HEIGHT = 80, 24#os.get_terminal_size()

def main(window):
    curses.use_default_colors()
    for i in range(0, curses.COLORS):
        curses.init_pair(i, i, -1)
    curses.curs_set(0)  # invisible cursor
    window.nodelay(1)
    window.clear()

    snake = Snake(WIDTH, HEIGHT)

    while snake.alive:
        apple_colour = curses.color_pair(3) if snake.apple.gold   or 1 else 0
        window.addch(snake.apple.y, snake.apple.x, b"A", apple_colour)
        window.move(0, 0)
        for x, y in snake.body:
            window.addch(y, x, b"X")
            window.refresh()
            #sleep(0.01)  # curses is retarded
        window.refresh()
        sleep(0.1)
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

"""

TODO
- resize window? (for terminals with different screen sizes)
- figure out how curses freaking works
- game loop
- how to show score?
    - maybe have number on screen that moves around if your snake gets close to it or something
- portability?

"""

