import math
import conf, runtime

def render (g, scr):
	# Print the box
	if conf.has_border:
		scr.addstr(0, 0, conf.line_ul + (conf.line_ux * (runtime.resolution_term[0] - 2)) + \
			conf.line_ur)
		for i in range(1, runtime.resolution_term[1] - 3):
			scr.addch(i, 0, conf.line_xl)
			scr.addch(i, runtime.resolution_term[0] - 1, conf.line_xr)
		scr.addstr(conf.line_ll + (conf.line_lx * (runtime.resolution_term[0] - 2)) + conf.line_lr)

	# Print out the blocks
	x_count = 1
	y_count = 1
	for i in g:
		for j in i:
			j.render(conf.block_size[0] * x_count, conf.block_size[1] * y_count, scr)
			y_count += 1
		y_count = 1
		x_count += 1
	scr.addch(conf.block_size[1] * (runtime.index[1] + 1), conf.block_size[0] * (runtime.index[0] + 1), 'i')

	# Add message at the bottom of the window
	scr.addstr(runtime.resolution_term[1] - 2, 0, runtime.message)
	scr.clrtoeol()

	# Add results to bottom of the window
	red_side = conf.lang_results[0] % (runtime.scores[0], math.floor(runtime.scores[0] / \
		runtime.resolution_game[0] / runtime.resolution_game[1] * 100))
	blue_side = conf.lang_results[1] % (runtime.scores[1], math.floor(runtime.scores[1] / \
		runtime.resolution_game[0] / runtime.resolution_game[1] * 100))
	scr.addstr(runtime.resolution_term[1] - 1, 0, red_side + blue_side)
	scr.clrtoeol()
