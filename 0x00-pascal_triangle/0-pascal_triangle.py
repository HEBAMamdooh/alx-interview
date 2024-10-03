#!/usr/bin/python3
"""
Pascal's Triangle
"""


def pascal_triangle(n):
    """
         returns a list of lists of
         integers representing
          the Pascal’s triangle of n
         Returns an empty list if n <= 0
    """
    try:
        # Ensure the input is an integer and non-negative
        if not isinstance(n, int):
            raise TypeError("Input must be an integer")
        if n <= 0:
            return []

        triangle = [[1]]  # First row is always [1]

        for i in range(1, n):
            row = [1]  # First element of each row is always 1
            prev_row = triangle[i - 1]

            # Calculate the middle elements of the row
            for j in range(1, i):
                row.append(prev_row[j - 1] + prev_row[j])

            row.append(1)  # Last element of each row is always 1
            triangle.append(row)

        return triangle

    except TypeError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
