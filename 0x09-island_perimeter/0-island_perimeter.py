#!/usr/bin/python3

def island_perimeter(grid):
    """
    Calculates the perimeter of the island described in grid.
    """
    perimeter = 0

    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 1:  # If current cell is land
                perimeter += 4  # Start with assuming 4 sides

                # Check adjacent cells
                if i > 0 and grid[i - 1][j] == 1:
                    perimeter -= 2  # Deduct 2 if there's land above
                if j > 0 and grid[i][j - 1] == 1:
                    perimeter -= 2  # Deduct 2 if there's land to the left

    return perimeter


# Example usage:
grid = [
    [0, 1, 0, 0],
    [1, 1, 1, 0],
    [0, 1, 0, 0],
    [1, 1, 0, 0]
]
print(island_perimeter(grid))  # Output should be 12
