#!/usr/bin/python3

import os
import curses
from time import sleep

from snake import Snake
from apple import Apple

dir_dict = {curses.KEY_UP: "up", curses.KEY_DOWN: "down", curses.KEY_LEFT: "left", curses.KEY_RIGHT: "right"}
HEIGHT, WIDTH = 80, 24#os.get_terminal_size()

def main(window):
    #print(window.getmaxyx())
    #window.clear()
    #curses.resizeterm(HEIGHT, WIDTH) <- doesnt work
    #window.refresh()
    #sleep(2)
    window.nodelay(1)
    window.clear()
    window.addstr(0, 0, "This is a snake game")
    window.refresh()
    #sleep(3)

    snake = Snake(WIDTH, HEIGHT)

    while snake.alive:
        #window.addstr(0, 0, str(snake.body))
        for y, x in snake.body:
            window.addch(y, x, b"X")
            window.addstr(0, 0, str(snake.body))
            window.refresh()
            sleep(0.01)  # curses is retarded
        window.refresh()
        sleep(1)
        window.clear()
        snake.direction = dir_dict.get(window.getch(), 0) or snake.direction
        snake.move()


if __name__ == '__main__':
    curses.wrapper(main)

"""

TODO
- resize window? (for terminals with different screen sizes)
- figure out how curses freaking works
- game loop
- how to show score?
    - maybe have number on screen that moves around if your snake gets close to it or something
- portability?

"""

