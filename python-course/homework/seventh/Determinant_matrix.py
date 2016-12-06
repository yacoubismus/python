'''
Created on 06.12.2016

@author: yacoub
'''
import numpy as np
from copy import copy, deepcopy
def determinant_matrix(m):
    det = 0
    for x in list(range(len(m))):
        det += m[0][x] * (-1)**(2+x) * determinant_matrix(matrix_get_submatrix(m,x,x))
    


def matrix_get_submatrix(m,i,j):
    submat = deepcopy(m)
    del submat[0] #Delete first row
    for b in list(range(len(matrix))): #Delete column i
        del submat[b][i]
#     submat = np.delete(submat, i, axis=0)
#     submat = np.delete(submat, j, axis= 1)
    return submat


if __name__ == "__main__":
    a = np.array([[1,2,3],[4,5,6],[7,8,9]],dtype=int)
    print(determinant_matrix(a))
#     print(a)
#     mm = matrix_get_submatrix(a,2,2)
#     print(mm)
#     print(a)