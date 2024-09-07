import numpy
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
def rotate90(matrix):
  rotated=numpy.rot90(matrix,3)
  return rotated

def rotate180(matrix):
  rotated=numpy.rot90(matrix,2)
  return rotated

def rotate270(matrix):
  rotated=numpy.rot90(matrix)
  return rotated


print(rotate90(matrix))