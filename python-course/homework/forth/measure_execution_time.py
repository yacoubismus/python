'''
Created on 16.11.2016

@author: Jacob
'''
from factorize import *
from poly_add import *

import time

def measure_execution_time_factorizing(number):
    start =  time.time()
    factorize(number)
    endTime = time.time()
    print('Took %s seconds to calculate.' % (endTime - start))
    
 
def measure_execution_time_poly_add(list1, list2): 
    start =  time.time()
    print (poly_add(list1, list2))
    endTime = time.time()
    print('Took %s seconds to calculate.' % (endTime - start)) 



    
if __name__ == "__main__":
    measure_execution_time_factorizing(1234567) 
    list1 = [1,3,4,5,6,7,8,9,9,8,8,8,8,8,9]   
    list2 = [1,3,4,5,6,7,8,9,9,8,8,8,8,8,9] 
    measure_execution_time_poly_add(list1, list2)