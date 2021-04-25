"""
Given a string in the form "AAAABBBBCCCCCDDEEEE" compress it to become "A4B4C5D2E4".
"""

"""
my solution
"""
def compressV1(s):
    previous_char = s[0]
    new_string = ''
    char_repetitions = 1

    for i in range(1,len(s)):
        letter = s[i]
        if i == (len(s)-1):
            #we reached the last character
            char_repetitions += 1
            new_string += previous_char + str(char_repetitions)
        elif letter == previous_char:
            # the chain of letters continue
            char_repetitions += 1
            previous_char = letter
        else:
            # letter found, is different to the previous one
            new_string += previous_char + str(char_repetitions)
            # reset next character count
            char_repetitions = 1
            previous_char = letter

    return new_string


