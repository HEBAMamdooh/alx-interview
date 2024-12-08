#!/usr/bin/python3
"""
Island Perimeter
"""


def island_perimeter(grid):
    """
    Returns the perimeter of the island described in grid.
    """
    perimeter = 0
    rows = len(grid)
    cols = len(grid[0])

    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 1:  # If the cell is land
                perimeter += 4  # Add 4 for the land cell

                # Check the cell above
                if i > 0 and grid[i - 1][j] == 1:
                    perimeter -= 2  # Reduce 2 for shared edge

                # Check the cell to the left
                if j > 0 and grid[i][j - 1] == 1:
                    perimeter -= 2  # Reduce 2 for shared edge

    return perimeter
