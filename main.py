#!/usr/bin/python3

import os
import sys
import traceback
import curses
from time import sleep

from snake import Snake
from apple import Apple
if sys.version < '3':
    from ai_py2 import Ai
else:
    from ai import Ai

class Color():
    BLACK = 1 #snake color
    GREEN = 2 #apple color
    GOLD = 3 #apple golden color

dir_dict = {curses.KEY_UP: "up", curses.KEY_DOWN: "down", curses.KEY_LEFT: "left", curses.KEY_RIGHT: "right"}
WIDTH, HEIGHT = 80, 24#os.get_terminal_size()


def game_over(window, snake):
    window.clear()
    window.addstr(0, 0, "Game Over! You lose.")
    window.addstr(1, 0, "You had %d points" % (snake.size - 3, ))
    window.refresh()
    sleep(3)

def main(window):
    curses.use_default_colors()
    curses.init_pair(Color.BLACK, curses.COLOR_BLACK, curses.COLOR_BLACK)
    curses.init_pair(Color.GREEN, curses.COLOR_GREEN, curses.COLOR_BLACK)
    curses.init_pair(Color.GOLD, curses.COLOR_YELLOW, curses.COLOR_BLACK)

    curses.curs_set(0)  # invisible cursor
    window.clear()
    window.nodelay(1)
    
    # intro screen 
    ai = Ai(WIDTH, HEIGHT)
    #press enter to start the game
    message_tracker = 0
    skip_count = 2
    message = "  PRESS ENTER TO START  "
    while not ai.start:
        ai.move() #make snake game play by itself on start menu
        display(window, ai, accept_input=False, sleep_rate=0.08)
        if not ai.alive:
            ai = Ai(WIDTH, HEIGHT)
        if ai.quit:
            sys.exit()
        
        #window.addstr(HEIGHT - 3, i, message, curses.color_pair(Color.BLACK))
        for i in range(0, WIDTH + 1, WIDTH // 3):
            for pos, j in enumerate(message):
                window.addch(HEIGHT - 3, (i + pos + message_tracker) % WIDTH, j)
        if skip_count == 2:
            message_tracker += 1
            message_tracker %= WIDTH
            skip_count = 0
        skip_count += 1
        window.refresh()
    del ai
    window.clear()

    snake = Snake(WIDTH, HEIGHT)
    while snake.alive:
        display(window, snake)
    else:
        game_over(window, snake)

def display(window, snake, accept_input=True, sleep_rate=0.05):
    y, x = window.getmaxyx()
    if y < HEIGHT or x < WIDTH:
        window.addstr(0, 0, "Please reset your terminal to default size to play")
        window.refresh()
        sleep(3)
        sys.exit()
    if y > HEIGHT:
        for i in range(0, WIDTH):
            window.addch(HEIGHT, i, b"#")
    if x > WIDTH:
        for i in range(0, HEIGHT):
            window.addch(i, WIDTH, b"#")

    apple_colour = curses.color_pair(Color.GOLD) if snake.apple.gold else curses.color_pair(Color.GREEN)
    window.addch(snake.apple.y, snake.apple.x, b"A", apple_colour)
    window.move(0, 0)
    window.addch(snake.body[-1][1], snake.body[-1][0], b"X")
    for x, y in snake.body[:-1]:
        window.addch(y, x, b"O")
        window.refresh()
        #sleep(0.01)  # curses is retarded
    window.refresh()
    sleep(sleep_rate)
    window.clear()
    ch = window.getch()
    if ch in [ord("q"), 27]: #27 == escape button
        if not accept_input:
            snake.quit = True
        else:
            snake.alive = False
    elif ch == ord("\n"):
        snake.start = True
    if accept_input:
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
