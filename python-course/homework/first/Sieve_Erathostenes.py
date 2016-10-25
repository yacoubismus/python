'''
Created on 25.10.2016

@author: yacoub
'''
def sieve_erathostens(max):
    primaries = [2,3]
    for number in range(4,max):
        flag = True
        for num in range(2, number):
            
            if(number % num == 0):
                flag = False
                break
            
            
        if(flag):
           primaries.append(number) 
           
    set(primaries)
    return sorted(primaries) 




print(sieve_erathostens(150))