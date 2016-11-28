'''
Created on 28.11.2016

@author: yacoub
'''
def fact2(n):
    factorial = 1
    for i in range(2,n+1):
        factorial = factorial * i
        
    return factorial    
        


def fact3(n):
    if n == 1:
        return 1
    if (n % 2 == 0):
        fact3(n/2)
        
    
            
def util (start, end):
    number = 1
    for i in range(start, end):
        number = number * i
        
    return number

           