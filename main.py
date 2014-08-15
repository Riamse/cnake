#!/usr/bin/python3

import os
import curses
from time import sleep

from snake import Snake
from apple import Apple

window = None
snake = None
apple = None
HEIGHT, WIDTH = os.get_terminal_size()

def __main__(window):
    #print(window.getmaxyx())
    #window.clear()
    #curses.resizeterm(HEIGHT, WIDTH) <- doesnt work
    #window.refresh()
    #sleep(2)
    window.clear()
    window.addstr(0, 0, "This is a snake game")
    window.refresh()
    sleep(3)

    snake = Snake(WIDTH, HEIGHT)
    apple = Apple(WIDTH, HEIGHT, snake.position)

    while snake.alive:
        pass


if __name__ == '__main__':
    curses.wrapper(__main__)

"""

TODO
- resize window? (for terminals with different screen sizes)
- figure out how curses freaking works
- game loop
- how to show score?
    - maybe have number on screen that moves around if your snake gets close to it or something
- portability?

"""

