#!/bin/python3

import time

import conf, game, grid, interface, render, runtime

runtime.stdscr = interface.intinit()
interface.initres(runtime.stdscr)

# --------------------------------------------------------------------------------------------------

# Main menu
exit_requested = False
while not exit_requested:
	render.main_menu()
	character = runtime.stdscr.getch()
	if character == conf.button_next:
		exit_requested = True

conf.block_size = tuple(map(lambda x : x * conf.block_scale, conf.block_pixel_size))
conf.block_tiny = True if conf.block_size[0] <= 2 or conf.block_size[1] <= 2 else False

# --------------------------------------------------------------------------------------------------

runtime.resolution_game = interface.getres(runtime.stdscr)
runtime.game_grid = grid.generate_grid(runtime.resolution_game[0], runtime.resolution_game[1])
runtime.message = conf.lang_beginning % (runtime.resolution_game[0], runtime.resolution_game[1])

exit_requested = False
while not exit_requested:
	render.render(runtime.game_grid, runtime.stdscr)
	character = runtime.stdscr.getch()
	if character == conf.button_quit:
		exit_requested = True
	elif character == conf.button_finish:
		exit_requested = True
		runtime.final_screen_requested = True
	else:
		# Handle character
		game.handle_input(character)

if runtime.final_screen_requested:
	render.render_banner(conf.banner_name)
	runtime.stdscr.getch()

interface.intterm(runtime.stdscr)
