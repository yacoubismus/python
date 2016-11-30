'''
Created on 29.11.2016

@author: yacoub
'''
import string







def base(n):  
    bases_list = list(string.digits + string.ascii_uppercase)  #  36 Elements 0 - 9 + A - Z
    
    #print(bases_list)
    return bases_list[n]

def base_convert(n,b):
    modulus_list = []
    # Testing Type
    assert type(b) is not string , "%r is not a string " % b
    b = int (b)
    # Testing base
    if (b < 2 ) or (b > 36) :
        return "invalid Base. Base should be bigger than 2 or smaller than 37"
    while n > 0 :
        
        modulus = base(int(n % b)) # without int i get float number. it make everything messy
        modulus_list.append(modulus)
        n = n // b # floor division
    modulus_list = modulus_list[::-1] # reverse list 
    return ''.join(modulus_list) # join list elements
    

if __name__ == "__main__": 
    
    #print(base(9))
    print(base_convert(15,"16"))
    
