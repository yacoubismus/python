'''
some usefull utils for complement_dna functions
'''

# letter converter
def complement_converter (letter):
    if letter == 'A':
        letter = 'T'
    elif letter == 'T':
        letter = 'A'
    elif letter == 'C':
        letter = 'G'
    elif letter == 'G':
        letter = 'C'
    return letter

# Letter value checker
def check_letter(letter , valid_values):
    flag = False
    try:
        if not letter in valid_values:
            raise ValueError('The letter %s is not a valid value' % letter)
        else:
            flag = True
            return flag
    except ValueError as error:
        print repr(error)
        return flag

