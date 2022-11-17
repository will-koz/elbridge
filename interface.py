import curses

import conf, runtime

def constrain (value, bounds, adds):
	# Basic mathematical function that adds (or subtracts), but keeps it bounded according to bounds
	is_int = isinstance(value, int)
	value += bounds[2] if adds else -bounds[2]
	value = value if value <= bounds[1] else bounds[1]
	value = value if value >= bounds[0] else bounds[0]
	value *= 10 ** conf.sigfigs
	value = round(value)
	value /= 10 ** conf.sigfigs
	if is_int:
		value = int(value)
	return value

# GET RESolution
def getres (stdscr):
	width, height = runtime.resolution_term
	height -= 2 # "Progress Bar" and system message
	width -= 2 * conf.block_size[0] # Remove borders
	height -= 2 * conf.block_size[1] # Remove borders
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

def initres (stdscr):
	height, width = stdscr.getmaxyx()
	runtime.resolution_term = (width, height)

# INTerface TERMinate
def intterm (stdscr):
	curses.nocbreak()
	stdscr.keypad(False)
	curses.echo()
	curses.endwin()
