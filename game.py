import curses, webbrowser

import conf, interface, render, runtime

def check_game_finished ():
	if runtime.scores[1] * 2 > runtime.resolution_game[0] * runtime.resolution_game[1]:
		runtime.final_screen_requested = True
		return True
	if runtime.scores[1] + runtime.scores[0] >= runtime.resolution_game[0] * \
		runtime.resolution_game[1]:
		runtime.final_screen_requested = True
		return True
	return False

def count_final_score ():
	for i in runtime.game_grid:
		for j in i:
			if j.color[1] == 0 and j.color[0] == 1:
				runtime.scores[0] += conf.finished_points
				runtime.scores[1] += 1 - conf.finished_points
			elif j.color[1] == 0:
				runtime.scores[1] += 1
	runtime.message = conf.lang_won if runtime.scores[0] > runtime.scores[1] else conf.lang_lost
	runtime.message %= (runtime.scores[0], runtime.scores[1], round(runtime.scores[0] * 100 / \
		(runtime.scores[0] + runtime.scores[1])))

def create_district ():
	district_size = len(runtime.selected)
	if len(runtime.selected) < conf.district_s[0] or len(runtime.selected) > conf.district_s[1]:
		runtime.message = conf.lang_wrongsize % (conf.district_s[0], conf.district_s[1], \
			district_size)
		return # has to be between the district size minimum and maximum
	if not determine_continuous(runtime.selected):
		runtime.message = conf.lang_notcontinuous
		return # has to be a continuous selection of land
	reds = 0
	for i in runtime.selected:
		# Get a count of the colors
		if runtime.game_grid[i[0]][i[1]].color[0] == 1:
			reds += 1
		# Figure out the bounds of the district
		runtime.game_grid[i[0]][i[1]].bounds = [False] * 8
		if not is_shared_block([i[0], i[1] - 1]): # Edge above
			runtime.game_grid[i[0]][i[1]].bounds[0] = True
			runtime.game_grid[i[0]][i[1]].bounds[1] = True
			runtime.game_grid[i[0]][i[1]].bounds[2] = True
		if not is_shared_block([i[0] + 1, i[1]]): # Edge right
			runtime.game_grid[i[0]][i[1]].bounds[2] = True
			runtime.game_grid[i[0]][i[1]].bounds[3] = True
			runtime.game_grid[i[0]][i[1]].bounds[4] = True
		if not is_shared_block([i[0], i[1] + 1]): # Edge below
			runtime.game_grid[i[0]][i[1]].bounds[4] = True
			runtime.game_grid[i[0]][i[1]].bounds[5] = True
			runtime.game_grid[i[0]][i[1]].bounds[6] = True
		if not is_shared_block([i[0] - 1, i[1]]): # Edge left
			runtime.game_grid[i[0]][i[1]].bounds[6] = True
			runtime.game_grid[i[0]][i[1]].bounds[7] = True
			runtime.game_grid[i[0]][i[1]].bounds[0] = True
		if not is_shared_block([i[0] - 1, i[1] - 1]): # Edge above left
			runtime.game_grid[i[0]][i[1]].bounds[0] = True
		if not is_shared_block([i[0] + 1, i[1] - 1]): # Edge above right
			runtime.game_grid[i[0]][i[1]].bounds[2] = True
		if not is_shared_block([i[0] + 1, i[1] + 1]): # Edge below right
			runtime.game_grid[i[0]][i[1]].bounds[4] = True
		if not is_shared_block([i[0] - 1, i[1] + 1]): # Edge below left
			runtime.game_grid[i[0]][i[1]].bounds[6] = True
	if reds == (district_size / 2):
		runtime.message = conf.lang_equ % (reds, district_size)
		return
	reds = True if reds > (district_size / 2) else False
	for i in runtime.selected:
		runtime.game_grid[i[0]][i[1]].selected = False
		runtime.game_grid[i[0]][i[1]].color[1] = 1 if reds else 2
	runtime.selected = []
	runtime.message = conf.lang_newdistrict % ("red" if reds else "blue")
	if reds:
		runtime.scores[0] += district_size
	else:
		runtime.scores[1] += district_size

def deselect (x):
	runtime.game_grid[x[0]][x[1]].selected = False
	runtime.selected = removeall(runtime.selected, x)
	runtime.message = conf.lang_deselected % (x[0] + 1, x[1] + 1, len(runtime.selected))

def determine_continuous (x):
	new_list = []
	for i in x:
		new_list.append((i, False))
	if len(new_list) == 0:
		return False
	delete_touching (new_list, 0)
	for i in new_list:
		if not i[1]:
			return False
	return True

def delete_touching (list, x):
	# Actually only marks items for deletion
	list[x] = (list[x][0], True)
	count = 0
	while count < len(list):
		if (not list[count][1]) and distance(list[x][0], list[count][0]) <= 1:
			delete_touching(list, count)
		count += 1

def distance (x, y):
	if conf.count_corners:
		# Return the Chebyshev distance of two points
		return max(abs(x[0] - y[0]), abs(x[1] - y[1]))
	else:
		# Return the Taxicab distance of two points
		return abs(x[0] - y[0]) + abs(x[1] - y[1])

def game_end ():
	runtime.final_screen_requested = True
	count_final_score()
	runtime.stdscr.addnstr(runtime.resolution_term[1] - 2, 0, runtime.message, \
		runtime.resolution_term[0] - 1)
	runtime.stdscr.clrtoeol()
	render.render_banner(conf.banner_won if runtime.scores[0] > runtime.scores[1] else \
		conf.banner_lost)
	runtime.stdscr.getch()

def handle_input (x):
	if conf.button_up(x):
		runtime.index[1] = max(runtime.index[1] - 1, 0)
	elif conf.button_down(x):
		runtime.index[1] = min(runtime.index[1] + 1, runtime.resolution_game[1] - 1)
	elif conf.button_left(x):
		runtime.index[0] = max(runtime.index[0] - 1, 0)
	elif conf.button_right(x):
		runtime.index[0] = min(runtime.index[0] + 1, runtime.resolution_game[0] - 1)
	elif x == conf.button_sel:
		toggle_select(runtime.index)
	elif x == conf.button_next:
		create_district()

def is_shared_block (x):
	if x[0] < 0 or x[1] < 0:
		return False
	if x[0] >= runtime.resolution_game[0] or x[1] >= runtime.resolution_game[1]:
		return False
	else:
		return runtime.game_grid[x[0]][x[1]].selected

def main_menu_input (x):
	if conf.button_up(x):
		runtime.selected_menu_item = interface.constrain(runtime.selected_menu_item, (1, 11, 1), \
			False)
	elif conf.button_down(x):
		runtime.selected_menu_item = interface.constrain(runtime.selected_menu_item, (1, 11, 1), \
			True)
	elif conf.button_left(x) or conf.button_right(x):
		# Gosh I wish python had enums
		if runtime.selected_menu_item == 1:
			conf.block_scale = interface.constrain(conf.block_scale, conf.settings_block_scale, \
				True if conf.button_right(x) else False)
		if runtime.selected_menu_item == 2:
			conf.count_corners = not conf.count_corners
		if runtime.selected_menu_item == 3:
			conf.difficulty = interface.constrain(conf.difficulty, conf.settings_difficulty, True \
				if conf.button_right(x) else False)
		if runtime.selected_menu_item == 4:
			conf.district_s[0] = interface.constrain(conf.district_s[0], \
				conf.settings_district_size_min, True if conf.button_right(x) else False)
		if runtime.selected_menu_item == 5:
			conf.district_s[1] = interface.constrain(conf.district_s[1], \
				conf.settings_district_size_max, True if conf.button_right(x) else False)
		if runtime.selected_menu_item == 6:
			conf.finished_points = interface.constrain(conf.finished_points, \
				conf.settings_finished_points, True if conf.button_right(x) else False)
	elif x == conf.button_sel:
		if runtime.selected_menu_item > 6:
			webbrowser.open(conf.pages[runtime.selected_menu_item - 7][1])
	conf.district_s.sort()

def removeall(list, x):
	new_list = []
	for i in list:
		if i != x:
			new_list.append(i)
	return new_list

def select (x):
	runtime.game_grid[x[0]][x[1]].selected = True
	runtime.selected.append(x[:])
	# determine_continuous(runtime.selected)
	runtime.message = conf.lang_selected % (x[0] + 1, x[1] + 1, len(runtime.selected))

def toggle_select (x):
	if runtime.game_grid[x[0]][x[1]].selected:
		deselect(x)
	elif runtime.game_grid[x[0]][x[1]].color[1] == 0:
		select(x)
	runtime.message += " " + conf.lang_continuous % (" " if determine_continuous(runtime.selected) \
		else " not ")
