def bucket_fill(grid, pos, new_value):

    print(pos)
    print('--- MAP ---')
    for gr in grid:
        print(gr)
    print('------------')

    directions = [
        (-1, 0),  # góra
        (1, 0),   # dół
        (0, 1),   # prawo
        (0, -1)   # lewo
    ]

    row = pos[0]
    col = pos[1]

    old_value = grid[row][col]

    if old_value == new_value:
        return grid

    def fill(row, col):

        if row < 0 or row >= len(grid):
            return
        if col < 0 or col >= len(grid[0]):
            return

        if grid[row][col] != old_value:
            return

        grid[row][col] = new_value

        for dr, dc in directions:
            fill(row + dr, col + dc)

    fill(row, col)

    # --- [row] [col] ---
    # grid[pos[0]][pos[1]] = new_value # .
    
    # grid[pos[0-1]][pos[1]] = new_value # <
    
    # grid[pos[0+1]][pos[1-1]] = new_value # ^

    # grid[pos[0]][pos[1+1]] = new_value # >
    
    # grid[pos[0-1]][pos[1]] = new_value # v


    # for gr in grid:    
    #     print(gr)
    # print('------------')

    print('--- AFTER ---')
    for gr in grid:
        print(gr)
    print('------------')

    return grid


# print(bucket_fill([["Y", "G", "G"], ["Y", "Y", "Y"], ["B", "Y", "R"]], [1, 2], "B"))
