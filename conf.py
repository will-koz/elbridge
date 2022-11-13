ascii = False

block_pixel_size = (2, 1)

# (width, height) # TODO revert this to 4, 2 or even 2, 1
block_size = tuple(map(lambda x : x * 4, block_pixel_size))
# block_size = tuple(map(lambda x : x * 2, block_pixel_size))
# block_size = tuple(map(lambda x : x * 1, block_pixel_size))

difficulty = 3
district_s = [6, 8] # district size
fill = " "
filled = "#" if ascii else "\u2593"
has_border = True

lang_beginning = "Beginning %dx%d game."
lang_deselected = "Deselected %d, %d (%d blocks selected)"
lang_equ = "District is evenly split with %d reds over %d blocks"
lang_newdistrict = "Successfully created new %s district"
lang_results = ["Red: %d (%d%%)", "Blue: %d (%d%%)"]
lang_selected = "Selected %d, %d (%d blocks selected)"
lang_wrongsize = "Districts should be between %d and %d, not %d blocks"

line_ul = "/" if ascii else "\u250C"
line_ux = "-" if ascii else "\u2500"
line_ur = "\\" if ascii else "\u2510"
line_xr = "|" if ascii else "\u2502"
line_lr = "/" if ascii else "\u2518"
line_lx = "-" if ascii else "\u2500"
line_ll = "\\" if ascii else "\u2514"
line_xl = "|" if ascii else "\u2502"