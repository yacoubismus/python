def multiply_poynomials(list1, list2):
    result = []
    lenght_list1 = len(list1)
    lenght_list2 = len(list2)
    short = []
    big = []
    if lenght_list1 == lenght_list2:
        short = list1
        big = list2
    else:
        short = (list2 if lenght_list1 - lenght_list2 > 0 else list1 )
        big =(list1 if lenght_list1 - lenght_list2 > 0 else list2 )
    for number in range(len(short)):
        result.append(list1[number] + list2[number])

    for number in range(len(short),len(big)):
        result.append(big[number])
    return result



print (multiply_poynomials([1,2,4,5,6],[1,2,4,5,6]))

print (multiply_poynomials([1,2,4],[1,2,4,5,6]))

print (multiply_poynomials([1,2,4,5,6],[1,2,4]))