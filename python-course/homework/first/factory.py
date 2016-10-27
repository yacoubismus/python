def fact(n):
    if(n == 1):
        return 1
    elif (n <= 0):
        return "Invalid"
    else:
        return n * fact(n-1)


print(fact(6))
print(fact(-1))