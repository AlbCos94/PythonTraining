"""
Given a string in the form "AAAABBBBCCCCCDDEEEE" compress it to become "A4B4C5D2E4".
"""

"""
my solution
"""
def compressV1(s):
    # corner case --> 1 element
    if len(s) == 1:
        return s + str(1)

    # corner case --> 0 element
    if len(s) == 0:
        return s

    previous_char = s[0]
    new_string = ''
    char_repetitions = 1

    for i in range(1, len(s)):
        letter = s[i]

        if letter == previous_char:
            # the chain of letters continue
            char_repetitions += 1
            previous_char = letter
            if i == (len(s)-1):
                #we reached the last character
                new_string += previous_char + str(char_repetitions)
                break
        else:
            # letter found, is different to the previous one
            new_string += previous_char + str(char_repetitions)
            # reset next character count
            char_repetitions = 1
            previous_char = letter
            if i == (len(s) - 1):
                # we reached the last character
                new_string += previous_char + str(char_repetitions)
                break

    return new_string

"""
Udemy Solution
"""
def compressV2(s):
    r = ""
    long = len(s)

    # two edge cases

    if long == 0:
        return ""
    if long == 1:
        return s+"1"

    last = s[0]
    cnt = 1
    i = 1

    while i < long:
        if s[i] == s[i-1]:
            # series continues
            cnt += 1
        else:
            # no longer in continuos series
            r = r + s[i-1] + str(cnt)
            cnt = 1 # reset of the count
        i += 1

    r = r +s[i-1]+str(cnt)

    return r
