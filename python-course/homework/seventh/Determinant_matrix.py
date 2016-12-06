'''
Created on 06.12.2016

@author: yacoub
'''
import numpy as np
from copy import copy, deepcopy
def Determinant_matrix():
    pass


def matrix_get_submatrix(m,i,j):
    submat = deepcopy(m)
    submat = np.delete(submat, i, axis=0)
    submat = np.delete(submat, j, axis= 1)
    return submat


if __name__ == "__main__":
    a = np.array([[1,2,3],[4,5,6],[7,8,9]],dtype=int)
    print(a)
    mm = matrix_get_submatrix(a,2,2)
    print(mm)
    print(a)