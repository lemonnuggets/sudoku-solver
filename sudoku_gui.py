import pygame
import sudoku
import time
# import sys
CELL_SIDE = 30
FONT_SIZE = 30
WIDTH = 600
HEIGHT = 600
MY_FONT = 0     # redefined later
GRID_COL = (0, 0, 0)
SPCL_BG_COL = (100, 255, 100)
BG_COL = (255, 255, 255)
TEXT_COL = (0, 0, 0)
DELAY = 0.02
original_grid = [
    [0, 0, 0, 0, 5, 1, 0, 0, 0],
    [0, 5, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 5, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 7, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0]
]

def draw_text(screen , font, text, color, bg_col, x, y, align="nw"):
    text_surface = font.render(text, True, color, bg_col)
    text_rect = text_surface.get_rect()
    if align == "nw":
        text_rect.topleft = (x, y)
    if align == "ne":
        text_rect.topright = (x, y)
    if align == "sw":
        text_rect.bottomleft = (x, y)
    if align == "se":
        text_rect.bottomright = (x, y)
    if align == "n":
        text_rect.midtop = (x, y)
    if align == "s":
        text_rect.midbottom = (x, y)
    if align == "e":
        text_rect.midright = (x, y)
    if align == "w":
        text_rect.midleft = (x, y)
    if align == "center":
        text_rect.center = (x, y)
    screen.blit(text_surface, text_rect)

def solve_and_show(screen, ogrid):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return pygame.QUIT
    grid = Grid(sudoku.deep_copy(ogrid.grid_data))
    for i in range(0, 9):
        for j in range(0, 9):
            if i == 8 and j == 8 and grid.grid_data[i][j] != 0:
                return grid
            elif grid.grid_data[i][j] == 0:
                row_list = sudoku.get_numbers_in_row(grid.grid_data, i)
                col_list = sudoku.get_numbers_in_col(grid.grid_data, j)
                square_list = sudoku.get_numbers_in_square(grid.grid_data, i, j)
                # print(row_list, col_list)
                possible_sols = range(1, 10)
                for sol in possible_sols:
                    if sol not in row_list and sol not in col_list and sol not in square_list:
                        # print(sol, row_list, col_list, square_list)
                        grid.grid_data[i][j] = sol
                        time.sleep(DELAY)
                        draw(screen, grid, i, j)
                        solved_grid = solve_and_show(screen, grid)
                        if solved_grid == pygame.QUIT:
                            return pygame.QUIT
                        elif solved_grid != -1:
                            return solved_grid
                return -1

class Grid:
    def __init__(self, grid_data):
        self.grid_data = grid_data

    def draw_grid(self, screen, grid, a, b, startx, starty):
        grid_col = GRID_COL
        text_col = pygame.Color(*TEXT_COL)
        spcl_bg_col = pygame.Color(*SPCL_BG_COL)
        bg_col = pygame.Color(*BG_COL)
        for i in range(0, len(grid)):
            for j in range(0, len(grid[i])):
                w = 1
                # render number in cell
                if grid[i][j] != 0 and (i, j) != (a, b):
                    draw_text(screen, MY_FONT, str(grid[i][j]), text_col, bg_col, int(startx + (j + 0.5) * CELL_SIDE), int(starty + (i + 0.5) * CELL_SIDE), 'center')
                elif (i, j) == (a, b):
                    draw_text(screen, MY_FONT, str(grid[i][j]), text_col, spcl_bg_col, int(startx + (j + 0.5) * CELL_SIDE), int(starty + (i + 0.5) * CELL_SIDE), 'center')
                # drawing board
                pygame.draw.rect(screen, grid_col, (int(startx + CELL_SIDE * i), int(starty + CELL_SIDE * j), CELL_SIDE, CELL_SIDE), w)
        # making every third line thicker
        for i in range(0, 3):
            for j in range(0, 3):
                pygame.draw.rect(screen, grid_col, (int(startx + 3 * CELL_SIDE * i), int(starty + 3 * CELL_SIDE * j), 3 * CELL_SIDE, 3 * CELL_SIDE), 3)
        
def draw(screen, grid, i, j):
    """
    Draw logic.
    """
    screen.fill([*BG_COL])
    GRID_START_X = WIDTH / 2 - 4.5 * CELL_SIDE
    GRID_START_Y = HEIGHT / 2 - 4.5 * CELL_SIDE
    grid.draw_grid(screen, grid.grid_data, i, j, GRID_START_X, GRID_START_Y)
    pygame.display.update()

pygame.init()
MY_FONT = pygame.font.SysFont('Mono', FONT_SIZE)
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Sudoku Solver')
running = True
grid = Grid(original_grid)
solve_and_show(screen, grid)
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            # sys.exit(0)