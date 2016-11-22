'''
Created on 21.11.2016

@author: yacoub
'''
# First step make list of the words in the lines which starts with 'o'.
# All words low case. some chars have to be deleted like ('.', ',', '"', ''' etc)

def word_counter (file_name):
    file = open(file_name, 'w')
    words = []
    for line in file:
        if test_line_prefix(line):
            
    pass        







# Testing first letter in the line after removing '"'
# by True another chars have to be removed.
def test_line_prefix(line): 
    line = line.lower() 
    first_letter_in_line =  line.split(' ', 1)[0]
    if first_letter_in_line.startswith('"'):
        line.replace('"','')
    if line.startswith('o'):
        line.replace('.' , ' ').replace()
        line.replace(',','')
        line.replace('?','')
        return True
    else :
        return False  
    
    
    