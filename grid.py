def count_neighbours(cell_to_check, grid):
    return len([(idx, cell) for idx, cell in enumerate(grid) if idx != cell_to_check and cell])
