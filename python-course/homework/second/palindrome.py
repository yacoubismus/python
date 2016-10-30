import re

def palindrome_checker(input):

    # delete all whitespaces from input
    input = re.sub(r"\s+", "", input)
    # To small letters
    input = input.lower()
    # start stp step to build reverse
    reverse_input = input[::-1]

    return input == reverse_input


print(palindrome_checker('Step on no pets'))


