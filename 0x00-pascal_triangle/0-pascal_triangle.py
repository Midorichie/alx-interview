def pascal_triangle(n):
    """
    Returns a list of lists representing Pascal's triangle of n rows.
    If n <= 0, return an empty list.
    """
    if n <= 0:
        return []

    triangle = []

    for i in range(n):
        row = [1] * (i + 1)  # Initialize a row with all 1s
        for j in range(1, i):  # Calculate the values in the middle of the row
            row[j] = triangle[i - 1][j - 1] + triangle[i - 1][j]
        triangle.append(row)

    return triangle
