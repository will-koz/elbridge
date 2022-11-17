import curses, math

import conf, interface, runtime

def main_menu ():
	runtime.stdscr.erase()
	render_banner(conf.banner_name, _y = 0)
	y = len(conf.banner_name)
	print_outs = [
		conf.lang_begin,
		main_menu_item(conf.settings_block_scale[3], conf.block_scale),
		main_menu_item(conf.lang_count_corners, conf.count_corners),
		main_menu_item(conf.settings_difficulty[3], conf.difficulty),
		main_menu_item(conf.settings_district_size_min[3], conf.district_s[0]),
		main_menu_item(conf.settings_district_size_max[3], conf.district_s[1]),
		main_menu_item(conf.settings_finished_points[3], conf.finished_points),
	]
	for i in conf.pages:
		print_outs.append(i[0])
	print_outs[runtime.selected_menu_item] = ' ' + print_outs[runtime.selected_menu_item] + ' '
	for i in range(len(print_outs)):
		y += 2
		right_column = round(conf.column_size * runtime.resolution_term[0])
		args = curses.color_pair(2) if (runtime.selected_menu_item == i) else curses.color_pair(0)
		if y < runtime.resolution_term[1]:
			runtime.stdscr.addstr(y, right_column - (1 if runtime.selected_menu_item == i else 0), \
				print_outs[i], args)

def main_menu_item (string, val):
	width = int(runtime.resolution_term[0] * (1 - 2 * conf.column_size))
	final_string = str(val)
	final_string = string + (' ' * (width - len(string) - len(final_string))) + final_string
	return final_string

def render (g, scr):
	runtime.stdscr.erase()
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

	# Render index
	if conf.block_tiny:
		# Color in the left half of each block
		for i in range(conf.block_size[1]):
			scr.addstr(conf.block_size[1] * (runtime.index[1] + 1) + i, conf.block_size[0] * \
				(runtime.index[0] + 1), conf.filled3 * math.ceil(conf.block_size[0] / 2), \
				curses.color_pair(0))
	else:
		for i in range(conf.block_pixel_size[1]):
			scr.addstr(conf.block_size[1] * (runtime.index[1] + 1) + i, conf.block_size[0] * \
				(runtime.index[0] + 1), conf.filled3 * conf.block_size[0], curses.color_pair(0))
		for i in range(conf.block_pixel_size[1], conf.block_pixel_size[1] * (conf.block_size[1] - \
			1)):
			scr.addstr(conf.block_size[1] * (runtime.index[1] + 1) + i, conf.block_size[0] * \
				(runtime.index[0] + 1), conf.filled3 * conf.block_pixel_size[0], curses.color_pair(0))
		for i in range(conf.block_pixel_size[1], conf.block_pixel_size[1] * (conf.block_size[1] - \
			1)):
			scr.addstr(conf.block_size[1] * (runtime.index[1] + 1) + i, conf.block_size[0] * \
				(runtime.index[0] + 2) - conf.block_pixel_size[0], conf.filled3 * \
				conf.block_pixel_size[0], curses.color_pair(0))
		for i in range(-1, conf.block_pixel_size[1] - 1):
			scr.addstr(conf.block_size[1] * (runtime.index[1] + 2) + i, conf.block_size[0] * \
				(runtime.index[0] + 1), conf.filled3 * conf.block_size[0], curses.color_pair(0))

	# Add message at the bottom of the window
	scr.addnstr(runtime.resolution_term[1] - 2, 0, runtime.message, runtime.resolution_term[0] - 1)
	scr.clrtoeol()

	# Add results to bottom of the window
	red_part = runtime.scores[0] / runtime.resolution_game[0] / runtime.resolution_game[1]
	blue_part = runtime.scores[1] / runtime.resolution_game[0] / runtime.resolution_game[1]

	red_side = conf.lang_results[0] % (runtime.scores[0], round(red_part * 100))
	blue_side = conf.lang_results[1] % (runtime.scores[1], round(blue_part * 100))
	num_spaces = 1
	if sum(runtime.scores) == runtime.resolution_game[0] * runtime.resolution_game[1]:
 		num_spaces = 2
	full_string = " " * (runtime.resolution_term[0] - len(red_side) - len(blue_side) - num_spaces)
	full_string = red_side + full_string + blue_side
	first_part = full_string[:round(red_part * runtime.resolution_term[0])]
	sec_part = full_string[round(red_part * runtime.resolution_term[0]):( \
		runtime.resolution_term[0] - round(blue_part * runtime.resolution_term[0]) - 1)]
	third_part = full_string[(runtime.resolution_term[0] - round(blue_part * \
		runtime.resolution_term[0]) - 1):]
	scr.addstr(runtime.resolution_term[1] - 1, 0, first_part, curses.color_pair(1))
	scr.clrtoeol()
	scr.addstr(sec_part, curses.color_pair(0))
	scr.clrtoeol()
	scr.addstr(third_part, curses.color_pair(2))

def render_banner (banner, _x = -1, _y = -1):
	y = (runtime.resolution_term[1] - (conf.block_pixel_size[1] * len(banner))) // 2
	y = 0 if y < 0 else y
	y = _y if _y >= 0 else y
	for i in banner:
		x = (runtime.resolution_term[0] - (conf.block_pixel_size[0] * len(i))) // 2
		x = 0 if x < 0 else x
		x = _x if _x >= 0 else x
		for j in i:
			character = conf.filled3 if j == 2 else (conf.filled if j == 1 else conf.fill)
			character *= conf.block_pixel_size[0]
			for k in range(conf.block_pixel_size[1]):
				if x + conf.block_pixel_size[0] < runtime.resolution_term[0] - 1 and y + \
					conf.block_pixel_size[1] < runtime.resolution_term[1]:
					runtime.stdscr.addstr(y + k, x, character)
			x += conf.block_pixel_size[0]
			if x > runtime.resolution_term[0]: break
		y += conf.block_pixel_size[1]
		if y > runtime.resolution_term[1]: break
