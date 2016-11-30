'''
Created on 28.11.2016

@author: yacoub
'''
'''
This 
'''

# Iterative factorial with for loop
def fact2(n):
    factorial = 1
    for i in range(2,n+1): # start with 2
        factorial = factorial * i
        
    return factorial    
        
'''
I am not sure if this faster. I think we will come in the end to the same number of loops
'''

# recursive to calculate the right side.
def fact3(n):
    if n == 1 or n == 0 :
        return 1
    else :
        mid = n // 2
        return fact_util(mid, n) * fact3(mid - 1) # exclusive mid
        
        
# Function to calculate the left side    
def fact_util (start, end):
    factorial = 1
    for i in range(start, end + 1): # inclusive end
        factorial = factorial * i
        
    return factorial    
            


if __name__ == "__main__": 
    print(fact3(1)) 
            