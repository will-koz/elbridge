#!/bin/python3

import time

import conf, game, grid, interface, render, runtime

runtime.stdscr = interface.intinit()
runtime.resolution_game = interface.getres(runtime.stdscr)
runtime.game_grid = grid.generate_grid(runtime.resolution_game[0], runtime.resolution_game[1])
runtime.message = conf.lang_beginning % (runtime.resolution_game[0], runtime.resolution_game[1])

exit_requested = False
while not exit_requested:
	render.render(runtime.game_grid, runtime.stdscr)
	character = runtime.stdscr.getch()
	if character == ord('q'): # Maybe set the character in conf
		exit_requested = True
	else:
		# Handle character
		game.handle_input(character)

interface.intterm(runtime.stdscr)
