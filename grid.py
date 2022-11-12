from block import Block
import runtime

def generate_grid (w, h):
	grid = []
	for i in range(h):
		grid.append([])
		for j in range(w):
			grid[i].append(Block())
	return grid
