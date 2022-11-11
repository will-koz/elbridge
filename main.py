#!/bin/python3

import time

import grid, interface, render, runtime

runtime.stdscr = interface.intinit()
runtime.resolution_game = interface.getres(runtime.stdscr)
runtime.game_grid = grid.generate_grid(runtime.resolution_game[1], runtime.resolution_game[0])

exit_requested = False
while not exit_requested:
	render.render(runtime.game_grid, runtime.stdscr)
	exit_requested = True if runtime.stdscr.getch() == ord('q') else False

interface.intterm(runtime.stdscr)
