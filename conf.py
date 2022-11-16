ascii = False

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

# (width, height) # TODO revert this to (4, 2) or even (2, 1)
block_size = tuple(map(lambda x : x * block_scale, block_pixel_size))

block_tiny = True if block_size[0] <= 2 or block_size[1] <= 2 else False

count_corners = False
difficulty = 3
district_s = [5, 9] # district size
fill = " "
filled = "#" if ascii else "\u2592"
filled2 = "#" if ascii else "\u2593"
filled3 = "#" if ascii else "\u2588"
has_border = True

lang_beginning = "Beginning %dx%d game."
lang_continuous = "(selection is%scontinuous)"
lang_deselected = "Deselected %d, %d : %d blocks selected"
lang_equ = "District is evenly split with %d reds over %d blocks"
lang_newdistrict = "Successfully created new %s district"
lang_notcontinuous = "In real life, you might be able to get away with that, but here districts \
need to be continuous"
lang_results = ["Red: %d (%d%%)", "Blue: %d (%d%%)"]
lang_selected = "Selected %d, %d : %d blocks selected"
lang_wrongsize = "Districts should be between %d and %d, not %d blocks"

line_ul = "/" if ascii else "\u250C"
line_ux = "-" if ascii else "\u2500"
line_ur = "\\" if ascii else "\u2510"
line_xr = "|" if ascii else "\u2502"
line_lr = "/" if ascii else "\u2518"
line_lx = "-" if ascii else "\u2500"
line_ll = "\\" if ascii else "\u2514"
line_xl = "|" if ascii else "\u2502"
