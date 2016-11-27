'''
Created on 27.11.2016

@author: Jacob
'''
def matrix_id(d):
    matrix = list([0]*d for i in range(d))
    
    for i in range(d):
        matrix [i][i] = 1
    return matrix
print (matrix_id(4))    