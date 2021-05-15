"""

Given a string, determine if it is compreised of all unique characters.
For example, the string "abcde" has all unique characters and should return True.
The string "aabcde" contains duplicate characters and should return False

"""


"""
my solution
"""
def uni_char(s):
    # corner case
    if len(s) <= 1:
        return True

    dict_count = {}

    for character in s:
        if character not in dict_count.keys():
            dict_count[character] = 1
        else:
            # we already found  a character countained by the dicctionary that tracks the count of characters
            return False

    return True

"""
built-in Udemy Solution
"""
def uni_charV2(s):
    return len(set(s)) == len(s)

"""
Udemy Solution using set()
"""
def uni_charV3(s):
    chars = set()

    for let in s:
        if let in chars:
            return False
        else:
            chars.add(let)

    return True