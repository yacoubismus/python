'''
Created on 23.11.2016

@author: yacoub
'''
def edit_distance(first_str, second_str):
    # if first string shorter. make it diverse
    if len(first_str) < len(second_str):
        return edit_distance(second_str, first_str)

    # if second string empty. all letter will be placed
    if len(second_str) == 0:
        return len(first_str)
    # else 
    last_row = range(len(second_str) + 1)
    for i, c_first in enumerate(first_str):
        current_row = [i + 1]
        for j, c_second in enumerate(second_str):
            insertion = last_row[j + 1] + 1 
            deletion = current_row[j] + 1       
            substitution = last_row[j] + (c_first != c_second)
            current_row.append(min(insertion, deletion, substitution))
        last_row = current_row
    
    return last_row[-1]

if __name__ == "__main__":
    print(edit_distance("Hi", "asda"))
    

