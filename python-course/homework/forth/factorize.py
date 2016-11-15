def erathostenes(number):
    primaries = []

    max = number

    mark = [False] * number

    for i in range(2, number):

        if not mark[i]:
            primaries.append(i)

        for j in range(i * i, max, i):
            # mark all multiples of i

            mark[j] = True

    return primaries  # not marked, i.e. prime


def factorize(number):
    factories = [1]

    primaries = erathostenes(number)

    return create_dictionary(recursive_call(number, primaries, factories))


def recursive_call(number, primaries, factories):
    for primary in primaries:

        if (number == 1):

            return factories

        elif (number % primary == 0):

            factories.append(primary)

            number = int(number / primary)

            return recursive_call(number, primaries, factories)

    return factories


def create_dictionary(item_list):
    factories = {}

    for item in item_list:

        if item not in factories:
            factories[item] = 1
        else:

            value = factories[item]

            factories[item] = value + 1

    return factories


print(factorize(4))