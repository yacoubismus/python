def erathostenes (number):

    primaries =[]

    max = number

    mark = [False] * number

    for i in range(2, number):

        if not mark[i]:

             primaries.append(i)

        for j in range(i*i, max, i):

         # mark all multiples of i

         mark[j] = True

    return primaries

def recursive_call(number, primaries, factories):

    for primary in primaries:

        if(number == 1):

            return factories

        elif(number % primary == 0):

                factories.append(primary)

                number =int (number / primary)

                return recursive_call(number, primaries, factories)

    return factories


def create_dictionary(item_list):
    factories = {}

    for item in item_list:

        if factories[item]:

            factories[item] = 1



        else:

            value = factories[item]

            value = value + 1

    return factories

def factorize(number):

    factories = [1]

    primaries = erathostenes(number)

    return create_dictionary(recursive_call(number, primaries, factories))

print(factorize(44))