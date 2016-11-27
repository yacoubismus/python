def matrix_transpose(m):
    l1 = []
    for i in range(len(m[0])):
        l2 = []
        for j in range(len(m)):
            temp = m[j][i]
            l2.append(temp)
            
        l1.append(l2)
    return l1



m = [[1,2,3,4],[5,6,7,8]]    

print(matrix_transpose(m))    