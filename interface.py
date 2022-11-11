import curses

import conf, runtime

# GET RESolution
def getres (stdscr):
	height, width = stdscr.getmaxyx()
	runtime.resolution_term = (width, height)
	height -= 2 # "Progress Bar" and system message
	width -= 2 * conf.block_size[0]
	height -= 2 * conf.block_size[1]
	width //= conf.block_size[0]
	height //= conf.block_size[1]
	return (width, height)

# INTerface INITialization:
def intinit ():
	stdscr = curses.initscr()
	curses.cbreak()
	curses.curs_set(0)
	stdscr.keypad(True)
	curses.start_color()
	curses.noecho()

	# Color stuff TODO move pair numbers to conf
	# if conf.ascii:
	curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_RED)
	curses.init_pair(2, curses.COLOR_BLACK, curses.COLOR_BLUE)
	# else:
		# curses.init_pair(1, curses.COLOR_RED, curses.COLOR_BLACK)
		# curses.init_pair(2, curses.COLOR_BLUE, curses.COLOR_BLACK)

	return stdscr

# INTerface TERMinate
def intterm (stdscr):
	curses.nocbreak()
	stdscr.keypad(False)
	curses.echo()
	curses.endwin()
