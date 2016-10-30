def max (x):
    if(not x):
        return None
    flag = True
    for number in x:

        if(flag):
            flag = False
            biggest = number
        if(number > biggest):
            biggest = number
    return  biggest


list = [1,4,6,8,3,10]
list1 =[]

print(max(list))
print(list1)



