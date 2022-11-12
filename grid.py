from block import Block
import runtime

def generate_grid (w, h):
	grid = []
	for i in range(w):
		grid.append([])
		for j in range(h):
			grid[i].append(Block())
	return grid
