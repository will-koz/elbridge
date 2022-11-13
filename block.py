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