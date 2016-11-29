'''
Created on 29.11.2016

@author: yacoub
'''
import string

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

if __name__ == "__main__": 
    print(convert_base(11,16))