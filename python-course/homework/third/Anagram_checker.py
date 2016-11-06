def anagram_checker(input1, input2):
    assert type(input1) is str and type(input2) is str , "input values should be string"
    input1 = input1.replace(" ", "").lower()
    input2 = input2.replace(" ", "").lower()

    if (len(input1) != len(input2)):
        return False
    input2_as_list = list(input2)
    for letter in input1:
        if letter  in input2:
            input2_as_list.remove(letter)
        else:
            return False

    return len(input2_as_list)== 0



print (anagram_checker("William Shakespeare", "I am a weakish speller"))

print (anagram_checker("aa a a", "AAAA"))

print (anagram_checker("aa", "aaa"))