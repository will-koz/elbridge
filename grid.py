from block import Block

def generate_grid (w, h):
	grid = []
	for i in range(w):
		grid.append([])
		for j in range(h):
			grid[i].append(Block())
	grid[0][0].selected = True
	return grid
