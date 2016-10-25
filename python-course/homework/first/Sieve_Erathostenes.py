'''
Created on 25.10.2016

@author: yacoub
'''
def sieve_erathostens(max):
    primaries = [2]
    for number in range(max):
        
        for num in range(3, number):
            flag = True
            if(number % num == 0):
                flag = False
                break
            else:
                primaries.append(number)
            
        
