def move_robot(grid, pos, instructions):
    direction_map = {
        'U': (-1, 0),
        'D': (1, 0),
        'L': (0, -1),
        'R': (0, 1)
    }

    rows = len(grid)
    cols = len(grid[0])
    r, c = pos

    for inst in instructions:
        dr, dc = direction_map[inst]
        nr, nc = r + dr, c + dc

        if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 0:
            r, c = nr, nc  

    return [r, c]


grid1 = [
  [0, 0, 0, 0],
  [0, 1, 0, 0],
  [0, 0, 1, 0],
  [0, 0, 0, 0]
]
print(move_robot(grid1, [1, 0], "RRDDLUUR"))  

grid2 = [
  [0, 0, 1, 0, 0],
  [1, 0, 0, 1, 0],
  [0, 0, 0, 1, 0],
  [0, 1, 0, 0, 0],
  [0, 0, 0, 1, 0]
]
print(move_robot(grid2, [0, 0], "RDDRURRDDLLUU"))  
