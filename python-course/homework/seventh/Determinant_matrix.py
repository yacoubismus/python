import numpy as np
from copy import copy, deepcopy
det = 0
def matrix_scalar_mul(a, c):

   m = len(a)     # number of rows of A
   n = len(a[0])  # number of cols of A
   return [[c * a[i][j] for j in range(n)] for i in range(m)]

def determinant_matrix(m):
    global det
    for x in list(range(len(m))):
        #det += m[0][x] * (-1) ** (2 + x) * determinant_matrix(matrix_get_submatrix(m, x, x))
        det += (-1) * matrix_scalar_mul(determinant_matrix(matrix_get_submatrix(m, x, x)),m[0][x])
        print("determinant:", det)
    return det

def matrix_get_submatrix(m, i, j):
    submat = deepcopy(m)
    submat = np.delete(submat, i, axis=0)
    submat = np.delete(submat, j, axis= 1)
    return submat


if __name__ == "__main__":
     a = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]], dtype=int)
     print(matrix_get_submatrix(a,0,1))
     print(a)
     determinant_matrix(a)