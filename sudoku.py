original_grid = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0]
]

def get_numbers_in_square(grid, i, j):
    a = i // 3
    b = j // 3
    a *= 3
    b *= 3
    num_list = []
    for x in range(a, a + 3):
        for y in range(b, b + 3):
            if grid[x][y] != 0:
                num_list.append(grid[x][y])
    return num_list

def get_numbers_in_col(grid, j):
    num_list = []
    for i in range(0, 9):
        if grid[i][j] != 0:
            num_list.append(grid[i][j])
    return num_list

def get_numbers_in_row(grid, i):
    num_list = []
    for j in range(0, 9):
        if grid[i][j] != 0:
            num_list.append(grid[i][j])
    return num_list

def disp(grid):
    print('\n')
    print('-'*30, end = '')
    for i in range(0, 9):
        print('\n')
        if i == 3 or i == 6:
            print('\n', end = '')
        for j in range(0, 9):
            print('{0} '.format(grid[i][j]), end = '')
            if j == 2 or j == 5:
                print('\t', end = '')
    print('\n')

def deep_copy(ogrid):
    grid = []
    for i in range(0, len(ogrid)):
        if isinstance(ogrid[i], list):
            grid.append(deep_copy(ogrid[i]))
        else:
            grid.append(ogrid[i])
    return grid

def solve(ogrid):
    grid = deep_copy(ogrid)
    for i in range(0, 9):
        for j in range(0, 9):
            if i == 8 and j == 8 and grid[i][j] != 0:
                return grid
            elif grid[i][j] == 0:
                row_list = get_numbers_in_row(grid, i)
                col_list = get_numbers_in_col(grid, j)
                square_list = get_numbers_in_square(grid, i, j)
                # print(row_list, col_list)
                possible_sols = range(1, 10)
                for sol in possible_sols:
                    if sol not in row_list and sol not in col_list and sol not in square_list:
                        # print(sol, row_list, col_list, square_list)
                        grid[i][j] = sol
                        solved_grid = solve(grid)
                        if solved_grid != -1:
                            return solved_grid
                return -1

disp(solve(original_grid))
# test_grid = [
#     [0, 5, 7, 0, 0, 0, 0, 0, 0],
#     [0, 0, 8, 0, 0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0, 0, 0, 0, 0],
# ]
# print(get_numbers_in_col(test_grid, 2), get_numbers_in_row(test_grid, 0))