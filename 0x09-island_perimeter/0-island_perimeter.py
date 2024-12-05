#!/usr/bin/python3
"""
A module that returns the perimeter of the island described in grid.
"""


def island_perimeter(grid):
    """
    Calculate the perimeter of the island described in grid.

    Args:
        grid (list of list of int):
        2D grid representing the island and water.
        1 reps land,
        0 reps water.

    Returns:
        integer: The perimeter of the island.
    """
    perimeter = 0
    rows = len(grid)
    cols = len(grid[0])

    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 1:
                perimeter += 4

                if i > 0 and grid[i-1][j] == 1:
                    perimeter -= 1
                if i < rows - 1 and grid[i+1][j] == 1:
                    perimeter -= 1
                if j > 0 and grid[i][j-1] == 1:
                    perimeter -= 1
                if j < cols - 1 and grid[i][j+1] == 1:
                    perimeter -= 1

    return perimeter
