'''
Created on 14.11.2016

@author: yacoub
'''
# This fuction create Pascal triangle in Form of dicinary
# Key is Line number and value is list
def pascal(rows):
    lines = {}

    list = [1]

    for i in range(rows):


        lines[i] = list

        list_new = []

        list_new.append(list[0])

        for i in range(len(list) - 1):
            list_new.append(list[i] + list[i + 1])

        list_new.append(list[-1])

        list = list_new

    return lines

# begin in the middle. With new Line whitespace fewer
def create_triangle(file_name, dictionary):
    file = open(file_name ,'w')
    whitespace = len(dictionary) * 5
    counter = 2
    for key , value in dictionary.items():
        file.write("\n")
        temp_list = dictionary[key]
        only_once = True
        counter =  counter +1
        for number in temp_list:
            whitespace =  whitespace  -1
            if(only_once):
                only_once = False
                file.write(' ' * whitespace)

            file.write(str(number)+ ' ' * counter)