'''
Created on 04.11.2016

@author: yacoub
'''

from complement_utils import *

def complement_Dna(dna_input):
    # only strings are accepted
    assert type(dna_input) is str, "input type is not string"
    # Empty strings are not allowded
    assert len(dna_input) > 0 , "Empty string is not allowded"
    result = []
    valid_alphabet = ['A','C','G','T']
    dna_input = dna_input.upper()
    for letter in dna_input:
        if check_letter(letter , valid_alphabet):
            result.append(complement_converter(letter))

        else:
            result = []
            return "Input has invalid Values. Only letters A C G T can be used"

    return ''.join(result)


#print(complement_Dna(""))
#print(complement_Dna(123))
print(complement_Dna("ttaTggcCt"))
print(complement_Dna("t"))




    