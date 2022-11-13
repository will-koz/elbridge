import curses

import conf, runtime

def create_district ():
	# TODO make sure that each district is continuous
	district_size = len(runtime.selected)
	if len(runtime.selected) < conf.district_s[0] or len(runtime.selected) > conf.district_s[1]:
		runtime.message = conf.lang_wrongsize % (conf.district_s[0], conf.district_s[1], \
			district_size)
		return # has to be between the district size minimum and maximum
	reds = 0
	for i in runtime.selected:
		# Get a count of the colors
		if runtime.game_grid[i[0]][i[1]].color[0] == 1:
			reds += 1
		# Figure out the bounds of the district
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

def handle_input (x):
	if x == curses.KEY_UP or x == ord('k') or x == ord('w'):
		runtime.index[1] = max(runtime.index[1] - 1, 0)
	elif x == curses.KEY_DOWN or x == ord('j') or x == ord('s'):
		runtime.index[1] = min(runtime.index[1] + 1, runtime.resolution_game[1] - 1)
	elif x == curses.KEY_LEFT or x == ord('h') or x == ord('a'):
		runtime.index[0] = max(runtime.index[0] - 1, 0)
	elif x == curses.KEY_RIGHT or x == ord('l') or x == ord('d'):
		runtime.index[0] = min(runtime.index[0] + 1, runtime.resolution_game[0] - 1)
	elif x == ord(' '):
		toggle_select(runtime.index)
	elif x == ord('\n'):
		create_district()

def is_shared_block (x):
	if x[0] < 0 or x[1] < 0:
		return False
	if x[0] >= runtime.resolution_game[0] or x[1] >= runtime.resolution_game[1]:
		return False
	else:
		return runtime.game_grid[x[0]][x[1]].selected

def removeall(list, x):
	new_list = []
	for i in list:
		if i != x:
			new_list.append(i)
	return new_list

def select (x):
	runtime.game_grid[x[0]][x[1]].selected = True
	runtime.selected.append(x[:])
	runtime.message = conf.lang_selected % (x[0] + 1, x[1] + 1, len(runtime.selected))

def toggle_select (x):
	if runtime.game_grid[x[0]][x[1]].selected:
		deselect(x)
	elif runtime.game_grid[x[0]][x[1]].color[1] == 0:
		select(x)
