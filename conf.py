ascii = False

block_size = (8, 4) # (width, height) # TODO revert this to 4, 2 or even 2, 1

# color_BLUE = 1
# color_DARKBLUE = 2
# color_DARKRED = 3
# color_RED = 4

difficulty = 3
fill = " "
has_border = True

lang_beginning = "Beginning %dx%d game."
lang_deselected = "Deselected %d, %d (%d blocks selected)"
lang_selected = "Selected %d, %d (%d blocks selected)"

line_ul = "/" if ascii else "\u250C"
line_ux = "-" if ascii else "\u2500"
line_ur = "\\" if ascii else "\u2510"
line_xr = "|" if ascii else "\u2502"
line_lr = "/" if ascii else "\u2518"
line_lx = "-" if ascii else "\u2500"
line_ll = "\\" if ascii else "\u2514"
line_xl = "|" if ascii else "\u2502"
