import curses, runtime

def deselect (x):
	pass

def handle_input (x):
	if x == curses.KEY_UP or x == ord('k') or x == ord('w'):
		runtime.index[1] = max(runtime.index[1] - 1, 0)
	elif x == curses.KEY_DOWN or x == ord('j') or x == ord('s'):
		runtime.index[1] = min(runtime.index[1] + 1, runtime.resolution_game[1] - 1)
	elif x == curses.KEY_LEFT or x == ord('h') or x == ord('a'):
		runtime.index[0] = max(runtime.index[0] - 1, 0)
	elif x == curses.KEY_RIGHT or x == ord('l') or x == ord('d'):
		runtime.index[0] = min(runtime.index[0] + 1, runtime.resolution_game[0] - 1)
	elif x == ' ':
		toggle_select(runtime.index)

def select (x):
	pass

def toggle_select (x):
	#
	pass
