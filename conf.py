import curses

ascii = True

banner_lost = [
	[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
		0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
	[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
		0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
	[0, 0, 2, 0, 2, 0, 0, 2, 2, 0, 0, 2, 0, 0, 2, 0, 0, 0, 2, 0, 0, 0, 0, 0, 2, 2, 0, 0, 0, 2, 2, 2,
		0, 2, 2, 2, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0],
	[0, 0, 2, 1, 2, 1, 2, 0, 1, 2, 0, 2, 1, 0, 2, 1, 0, 0, 2, 1, 0, 0, 0, 2, 0, 1, 2, 0, 2, 0, 1, 1,
		1, 0, 2, 1, 1, 0, 0, 2, 0, 2, 0, 1, 0, 0],
	[0, 0, 0, 2, 0, 1, 2, 1, 0, 2, 1, 2, 1, 0, 2, 1, 0, 0, 2, 1, 0, 0, 0, 2, 1, 0, 2, 1, 2, 2, 2, 2,
		0, 0, 2, 1, 0, 0, 0, 0, 1, 2, 1, 0, 0, 0],
	[0, 0, 0, 2, 1, 0, 2, 1, 0, 2, 1, 2, 1, 0, 2, 1, 0, 0, 2, 1, 0, 0, 0, 2, 1, 0, 2, 1, 0, 1, 1, 2,
		1, 0, 2, 1, 0, 0, 0, 2, 0, 2, 1, 0, 0, 0],
	[0, 0, 0, 2, 1, 0, 0, 2, 2, 0, 1, 0, 2, 2, 0, 1, 0, 0, 2, 2, 2, 2, 0, 0, 2, 2, 0, 1, 2, 2, 2, 0,
		1, 0, 2, 1, 0, 0, 0, 0, 1, 0, 2, 0, 0, 0],
	[0, 0, 0, 0, 1, 0, 0, 0, 1, 1, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1,
		0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
	[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
		0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
	[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
		0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
]
banner_name = [
	[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
		0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
	[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
		0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
	[0, 0, 2, 2, 2, 2, 2, 0, 2, 0, 0, 0, 0, 0, 2, 2, 2, 2, 0, 0, 2, 2, 2, 2, 0, 0, 2, 2, 2, 2, 2, 0,
		2, 2, 2, 2, 0, 0, 0, 2, 2, 2, 0, 0, 2, 2, 2, 2, 2, 0, 0, 0],
	[0, 0, 2, 1, 1, 1, 1, 1, 2, 1, 0, 0, 0, 0, 2, 1, 1, 1, 2, 0, 2, 1, 1, 1, 2, 0, 0, 1, 2, 1, 1, 1,
		2, 1, 1, 1, 2, 0, 2, 0, 1, 1, 2, 0, 2, 1, 1, 1, 1, 1, 0, 0],
	[0, 0, 2, 2, 2, 0, 0, 0, 2, 1, 0, 0, 0, 0, 2, 2, 2, 2, 0, 1, 2, 2, 2, 2, 0, 1, 0, 0, 2, 1, 0, 0,
		2, 1, 0, 0, 2, 1, 2, 1, 0, 0, 0, 1, 2, 2, 2, 0, 0, 0, 0, 0],
	[0, 0, 2, 1, 1, 1, 0, 0, 2, 1, 0, 0, 0, 0, 2, 1, 1, 1, 2, 0, 2, 1, 2, 1, 1, 0, 0, 0, 2, 1, 0, 0,
		2, 1, 0, 0, 2, 1, 2, 1, 0, 2, 2, 0, 2, 1, 1, 1, 0, 0, 0, 0],
	[0, 0, 2, 2, 2, 2, 2, 0, 2, 2, 2, 2, 2, 0, 2, 2, 2, 2, 0, 1, 2, 1, 0, 2, 2, 0, 2, 2, 2, 2, 2, 0,
		2, 2, 2, 2, 0, 1, 0, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 0, 0, 0],
	[0, 0, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 0, 0, 1, 0, 0, 1, 1, 0, 1, 1, 1, 1, 1,
		0, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 0],
	[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
		0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
	[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
		0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
]
banner_won = [
	[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
		0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
	[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
		0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
	[0, 0, 0, 2, 2, 2, 0, 0, 0, 2, 2, 2, 0, 0, 0, 2, 2, 2, 0, 0, 2, 2, 2, 2, 0, 0, 0, 0, 0, 2, 2, 2,
		0, 0, 0, 2, 2, 2, 0, 0, 2, 2, 0, 2, 2, 0, 2, 2, 2, 2, 2, 0, 0, 0],
	[0, 0, 2, 0, 1, 1, 2, 0, 2, 0, 1, 1, 2, 0, 2, 0, 1, 1, 2, 0, 2, 1, 1, 1, 2, 0, 0, 0, 2, 0, 1, 1,
		2, 0, 2, 0, 1, 1, 2, 0, 2, 1, 2, 0, 2, 1, 2, 1, 1, 1, 1, 1, 0, 0],
	[0, 0, 2, 1, 0, 0, 0, 1, 2, 1, 0, 0, 2, 1, 2, 1, 0, 0, 2, 1, 2, 1, 0, 0, 2, 1, 0, 0, 2, 1, 0, 0,
		0, 1, 2, 1, 0, 0, 2, 1, 2, 1, 2, 1, 2, 1, 2, 2, 2, 0, 0, 0, 0, 0],
	[0, 0, 2, 1, 0, 2, 2, 0, 2, 1, 0, 0, 2, 1, 2, 1, 0, 0, 2, 1, 2, 1, 0, 0, 2, 1, 0, 0, 2, 1, 0, 2,
		2, 0, 2, 2, 2, 2, 2, 1, 2, 1, 0, 1, 2, 1, 2, 1, 1, 1, 0, 0, 0, 0],
	[0, 0, 0, 2, 2, 2, 2, 1, 0, 2, 2, 2, 0, 1, 0, 2, 2, 2, 0, 1, 2, 2, 2, 2, 0, 1, 0, 0, 0, 2, 2, 2,
		2, 1, 2, 1, 1, 1, 2, 1, 2, 1, 0, 0, 2, 1, 2, 2, 2, 2, 2, 0, 0, 0],
	[0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 1, 1, 1, 0, 0, 0, 1, 1, 1, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 1, 1,
		1, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 1, 1, 1, 1, 0, 0],
	[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
		0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
	[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
		0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
]

block_pixel_size = (2, 1)
# block_scale = 4
block_scale = 3
# block_scale = 2
# block_scale = 1

# (width, height)
# block_size = tuple(map(lambda x : x * block_scale, block_pixel_size))
block_size = block_pixel_size # This is overwritten in main.py

# block_tiny = True if block_size[0] <= 2 or block_size[1] <= 2 else False
block_tiny = True # This is overwritten in main.py

button_finish = ord('f')
button_next = ord('\n')
button_quit = ord('q')
button_sel = ord(' ')

button_up = lambda x : x == curses.KEY_UP or x == ord('k') or x == ord('w')
button_down = lambda x : x == curses.KEY_DOWN or x == ord('j') or x == ord('s')
button_left = lambda x : x == curses.KEY_LEFT or x == ord('h') or x == ord('a')
button_right = lambda x : x == curses.KEY_RIGHT or x == ord('l') or x == ord('d')

column_size = 1 / 3 # Only used on main menus

count_corners = False
difficulty = 3.0
district_s = [5, 9] # district size
fill = " "
filled = "." if ascii else "\u2592"
filled2 = "0" if ascii else "\u2593"
filled3 = "#" if ascii else "\u2588"
finished_points = 0.1
has_border = True

lang_begin = "Press ENTER to begin the game..."
lang_beginning = "Beginning %dx%d game."
lang_continuous = "(selection is%scontinuous)"
lang_count_corners = "Count corners:"
lang_deselected = "Deselected %d, %d : %d blocks selected"
lang_equ = "District is evenly split with %d reds over %d blocks"
lang_lost = "You lost. Final score: %d-%d (%d%%)"
lang_newdistrict = "Successfully created new %s district"
lang_notcontinuous = "In real life, you might be able to get away with that, but here districts \
need to be continuous"
lang_results = ["Red: %d (%d%%)", "Blue: %d (%d%%)"]
lang_selected = "Selected %d, %d : %d blocks selected"
lang_won = "You won %d-%d! (%d%%)"
lang_wrongsize = "Districts should be between %d and %d, not %d blocks"

line_ul = "/" if ascii else "\u250C"
line_ux = "-" if ascii else "\u2500"
line_ur = "\\" if ascii else "\u2510"
line_xr = "|" if ascii else "\u2502"
line_lr = "/" if ascii else "\u2518"
line_lx = "-" if ascii else "\u2500"
line_ll = "\\" if ascii else "\u2514"
line_xl = "|" if ascii else "\u2502"

pages = [
	("CGP Grey on the shortest-splitline algo.", "https://www.youtube.com/watch?v=kUS9uvYyn3A"),
	("Read more about Gerrymandering", "https://wikipedia.org/wiki/Gerrymandering"),
	("Read more about the Wasted Vote Effect", "https://en.wikipedia.org/wiki/Wasted_vote"),
	("Read more about shortest-splitline algo.", "https://www.rangevoting.org/GerryExamples.html"),
	("Ugly Gerry", "http://uglygerry.com/")
]

selected = "s" if ascii else "\u2584"

settings_block_scale = (1, 8, 1, "Block scale:")
# settings_count_corners is a boolean
settings_difficulty = (2, 4, 0.1, "Difficulty:")
settings_district_size_min = (1, 10, 1, "District Size:")
settings_district_size_max = (5, 20, 1, "District Size:")
settings_finished_points = (0, 0.3, 0.01, "Points per block after game end:")

sigfigs = 2
