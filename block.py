import curses, random

import conf

class Block:
	def __init__ (self):
		# First number is self color. Second number is district color.
		# 0 is undecided district or nonexistant population, 1 is red, 2 is blue
		self.color = [0, 0]

		# TODO add a way for nonexistant populations to exist in a block
		self.color[0] = 1 if random.random() < (1 / conf.difficulty) else 2

		self.selected = False
		self.bounds = [False] * 8

	def render (self, x, y, stdscr):
		args = curses.color_pair(self.color[0])
		character = conf.fill
		if self.color[1] > 0:
			args = curses.color_pair(self.color[1])
			character = conf.filled
		if self.selected: # TODO make a better rendition
			character = "s"
		for i in range(conf.block_size[1]):
			stdscr.addstr(y + i, x, character * conf.block_size[0], args)

		# Now render the edges
		if self.color[1] == 0:
			return
		character = conf.filled2
		if self.bounds[0]:
			for i in range(conf.block_pixel_size[1]):
				stdscr.addstr(y + i, x, character * conf.block_pixel_size[0], args)
		if self.bounds[1]:
			for i in range(conf.block_pixel_size[1]):
				stdscr.addstr(y + i, x + conf.block_pixel_size[0], character * (conf.block_size[0] \
					- 2), args)
		if self.bounds[2]:
			for i in range(conf.block_pixel_size[1]):
				stdscr.addstr(y + i, x + conf.block_size[0] - conf.block_pixel_size[0], character \
					* conf.block_pixel_size[0], args)
		if self.bounds[3]:
			for i in range(conf.block_pixel_size[1], conf.block_size[1] - conf.block_pixel_size[1]):
				stdscr.addstr(y + i, x + conf.block_size[0] - conf.block_pixel_size[0], character \
					* conf.block_pixel_size[0], args)
		if self.bounds[4]:
			for i in range(conf.block_size[1] - conf.block_pixel_size[1], conf.block_size[1]):
				stdscr.addstr(y + i, x + conf.block_size[0] - conf.block_pixel_size[0], character \
					* conf.block_pixel_size[0], args)
		if self.bounds[5]:
			for i in range(conf.block_size[1] - conf.block_pixel_size[1], conf.block_size[1]):
				stdscr.addstr(y + i, x + conf.block_pixel_size[0], character * (conf.block_size[0] \
					- 2), args)
		if self.bounds[6]:
			for i in range(conf.block_size[1] - conf.block_pixel_size[1], conf.block_size[1]):
				stdscr.addstr(y + i, x, character * conf.block_pixel_size[0], args)
		if self.bounds[7]:
			for i in range(conf.block_pixel_size[1], conf.block_size[1] - conf.block_pixel_size[1]):
				stdscr.addstr(y + i, x, character * conf.block_pixel_size[0], args)
