import random
import time
import os
import sys


def print_grid(grid):
    """Take a 2D list of 0's and 1's, and print a grid with empty and solid squares substituted"""
    for x in range(grid_size):
        for y in range(grid_size):
            if grid[x][y]:
                print("■", end="")
            else:
                print("□", end="")
        print()


def count_neighbors(grid, x, y):
    """Count the nuymber of neighbouring cells with a value of 1"""
    neighbors = 0
    for x_diff in [-1, 0, 1]:
        if (x + x_diff) < 0 or (x + x_diff) > (grid_size - 1):
            continue
        for y_diff in [-1, 0, 1]:
            if (y + y_diff) < 0 or (y + y_diff) > (grid_size - 1):
                continue
            if x_diff == 0 and y_diff == 0:
                continue
            if grid[x + x_diff][y + y_diff]:
                neighbors += 1
    return neighbors


def dead_or_alive(grid, x, y):
    """Calculate if each cell will be dead or alive next iteration"""
    current_cell = grid[x][y]
    neighbors = count_neighbors(grid, x, y)
    if current_cell:
        if neighbors < 2:
            return 0
        elif 2 <= neighbors <= 3:
            return 1
        elif neighbors > 3:
            return 0
    else:
        if neighbors == 3:
            return 1
        else:
            return 0


def iterate(grid):
    """Iterate the grid to the next configuration"""
    return [
        [dead_or_alive(grid, x, y) for y in range(grid_size)] for x in range(grid_size)
    ]


def clear_screen():
    """Clear the screen for the next iteration"""
    os.system("cls" if os.name == "nt" else "clear")


grid_size = int(sys.argv[1])
grid = [[random.choice([0, 1]) for y in range(grid_size)] for x in range(grid_size)]
iterations = int(sys.argv[2])

for x in range(iterations):
    clear_screen()
    print("\r")
    grid = iterate(grid)
    print_grid(grid)
    print("\n")
    time.sleep(0.1)
