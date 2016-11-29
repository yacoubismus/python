'''
Created on 29.11.2016

@author: yacoub
'''
import string
from test.test_xml_etree import ElementSlicingTest

CHAR_LOOKUP = list(string.digits + string.ascii_uppercase)

def numeral(n):
    global CHAR_LOOKUP
    return CHAR_LOOKUP[n]

def convert_base(number, base):
    if base < 2 or base > 36:
        return False
    mods = []
    while number > 0:
        mods.append(numeral(number % base))
        number //= base
    mods.reverse()
    return ''.join(mods)
def base(n):  
    bases_list = list(string.digits + string.ascii_uppercase)  # only 35 ElementSlicingTest 0 - 9 + A - Z
    
    #print(bases_list)
    return bases_list[n]

def base_convert(n,b):
    modulus_list = []
    assert type(b) is string , "Its not astring: %r" % b
    if b < 2 or b > 36 :
        return "invalid Base. Base should be bigger than 2 or smaller than 37"
    while n > 0 :
        
        modulus = base(n % b)
        modulus_list.append(modulus)
        n = n / b
    modulus_list = modulus_list[::-1]    
    return modulus_list
    

if __name__ == "__main__": 
    
    print(base(9))
    
