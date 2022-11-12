import curses

import conf, runtime

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

def removeall(list, x):
	new_list = []
	for i in list:
		if i != x:
			new_list.append(i)
	runtime.stdscr.addstr(runtime.resolution_term[1] - 1, 0, str(new_list))
	return new_list

def select (x):
	runtime.game_grid[x[0]][x[1]].selected = True
	runtime.selected.append(x[:])
	runtime.stdscr.addstr(runtime.resolution_term[1] - 1, 0, str(runtime.selected))
	runtime.message = conf.lang_selected % (x[0] + 1, x[1] + 1, len(runtime.selected))

def toggle_select (x):
	if runtime.game_grid[x[0]][x[1]].selected:
		deselect(x)
	else:
		select(x)
