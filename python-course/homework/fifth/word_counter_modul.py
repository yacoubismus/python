'''
Created on 21.11.2016

@author: yacoub
'''
# First step make list of the words in the lines which starts with 'o'.
# All words low case. some chars have to be deleted like ('.', ',', '"', ''' etc)
import itertools
from collections import Counter
def text_lines (file_name):
    with open(file_name) as f:
        return f

def word_counter (file_name):
    words_list = []
    with open(file_name) as f:
        for line in f:
            if test_line_prefix(line):
                line = replace_some_chars(line)
                words_list.append(line.split(' '))
    merged = list(itertools.chain(*words_list))     # merge all lists in one list.   
    return Counter (merged)



def word_counter_printer (counter):
    for key, value in counter.items():
         print (key + " : " + str(value))


# Testing first letter in the line after removing '"'
# by True another chars have to be removed.
def test_line_prefix(line): 
    line = line.lower() 
    first_word_in_line =  line.split(' ', 1)[0]
    if first_word_in_line.startswith('"'):
        line = line.replace('"','')
    if line.startswith('o'):
        return True
    else :
        return False 
# replacing     
def replace_some_chars (line): 
    line = line.replace('"','')
    line = line.replace('.' , ' ')
    line = line.replace(',','')
    line = line.replace('?','')
    return line

if __name__ == "__main__":
    print(word_counter("sherlock.txt"))    
    print (word_counter_printer(word_counter("sherlock.txt")))
           

    