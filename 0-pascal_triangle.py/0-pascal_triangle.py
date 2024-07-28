def pascal_triangle(n):
  """
  Generates a list of lists representing Pascal's triangle of size n.

  Args:
      n: An integer representing the number of rows in the triangle.

  Returns:
      A list of lists containing the Pascal's triangle values.
  """
  if n <= 0:
    return []

  triangle = []
  triangle.append([1])

  for i in range(1, n):
    row = []
    row.append(1)
    for j in range(1, i):
      current_value = triangle[i-1][j-1] + triangle[i-1][j]
      row.append(current_value)
    row.append(1)
    triangle.append(row)

  return triangle
