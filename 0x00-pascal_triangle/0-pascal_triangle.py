#!/usr/bin/env python3
"""Pascal triangle challenge"""


def pascal_triangle(n):
    """Generate Pascal's Triangle as a list of lists.

    Args:
        n (int): Number of rows in Pascal's Triangle.

    Returns:
        list: A list of lists representing Pascal's Triangle.
    """
    if n <= 0:
        return []

    triangle = [[1]]  # The first row is always [1]

    for i in range(1, n):  # Start from the second row
        prev_row = triangle[-1]  # Get the last row in the triangle
        # Create the new row by summing pairs from the previous row
        new_row = [1] + [prev_row[j] + prev_row[j + 1]
                         for j in range(len(prev_row) - 1)] + [1]
        triangle.append(new_row)  # Add the new row to the triangle

    return triangle
