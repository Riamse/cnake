import curses

crs = None

def __main__():
	global crs
	crs = curses.initscr()
	curses.noecho()
	curses.cbreak()
	crs.keypad(1)
	quit()

def quit():
	global crs
	curses.nocbreak()
	crs.keypad(0)
	curses.echo()
	curses.endwin()

if __name__ == '__main__':
	__main__()