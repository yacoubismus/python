'''
Created on 27.11.2016

@author: Jacob
'''

def matrix_scalar_mul(m,c):
    #create a matrix like orginal. All element are 0.
    matrix = list([0]*len(m) for i in range(len(m[0])))
    for i in range(len(m)):
        for j in range(len(m[0])):
            matrix[i][j] = c * m [i][j]
    
    return matrix
                
                   
if __name__ == "__main__":     
    m = [[1,2,3],[4,5,6],[7,8,9]]            

    print(matrix_scalar_mul(m, 4))               
   
           