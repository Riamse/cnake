import curses
from time import sleep

window = None
snake = None
apple = None
WIDTH = 80
HEIGHT = 24

def __main__():
    try:
        global window, snake, apple
        window = curses.initscr()
        curses.noecho()
        curses.cbreak()
        window.keypad(1)
        curses.newwin(10, 5, 10, 10)
        #print(window.getmaxyx())
        #window.clear()
        #curses.resizeterm(HEIGHT, WIDTH) <- doesnt work
        #window.refresh()
        #sleep(2)

        snake = Snake(WIDTH, HEIGHT)
        apple = Apple(WIDTH, HEIGHT, snake.pos)

        while (snake.alive):
            pass

        quit()
    except:
        print('FATAL ERROR')
        print('Sleeping for 5 seconds so you can read this')
        sleep(5)
        quit()

def quit():
    global window
    curses.nocbreak()
    window.keypad(0)
    curses.echo()
    curses.endwin()

if __name__ == '__main__':
    __main__()

"""

TODO
- resize window? (for terminals with different screen sizes)
- figure out how curses freaking works
- game loop
- how to show score?
    - maybe have number on screen that moves around if your snake gets close to it or something
- portability?

"""