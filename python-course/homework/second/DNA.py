def dna_into_rna (input):
    #valid chars
    valid_values = ['A','C','G','T']
    #output as list of chars
    output = []
    for letter in input:
        # only valid chars take seriously
        if letter in valid_values:
            #from T make U
            if letter == 'T' :
                output.append('U')

            else:
                output.append(letter)
    # join Chars to string
    return ''.join(output)

print(dna_into_rna("TACGAWER"))