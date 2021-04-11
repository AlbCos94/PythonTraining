"""
Given two strings, check to see if there are anagrams. An anagram is when the two strings can be written using the exact same letters
so you can rearrange the letters to get different phrase or word
Example

"public relations" and "crap built on lies" --> true
"clint eastwood" and "old west action"

note: spaces and capitalizations can be ignored
"""

"""
diagramV1:
used of ordered list of the characters of the strings to check if strings are anagrams
"""
def diagramV1(s1,s2):
    # first we remove spaces (spaces can be ignored)
    s1 = s1.replace(" ", "")
    s2 = s2.replace(" ", "")
    # we remove capital letters (capitaliyatuibs can be ignored)
    s1 = s1.lower()
    s2 = s2.lower()

    #print(s1)
    #print(s2)

    # if length of both is not the same, we return directly False
    if len(s1) != len(s2):
        return False

    #convert string to a list of characters
    l1 = list(s1)
    l2 = list(s2)

    #the list is sorted
    l1.sort()
    l2.sort()

    # we loop through the list
    index = 0

    for element in l1:
        if l2[index] != element:
            return False
        index += 1

    return True

"""
diagramV2:
used of dictionaries to check if strings are anagrams
we are gonna build a dictionary from one of the strings such as:
    key --> character
    value --> number of times that character appears
once we got that dictionary, we will compare it with the other string
"""

def diagramV2(s1,s2):
    # first we remove spaces (spaces can be ignored)
    s1 = s1.replace(" ", "")
    s2 = s2.replace(" ", "")
    # we remove capital letters (capitaliyatuibs can be ignored)
    s1 = s1.lower()
    s2 = s2.lower()

    # if length of both is not the same, we return directly False
    if len(s1) != len(s2):
        return False

    # comparison using a dictionary
    dict_s1 = {}

    # building up the dictionary of ocurrences for characters
    for character in s1:
        if character not in dict_s1:
            dict_s1[character] = 1
        else:
            dict_s1[character] += 1

    # comparing the dictionary of ocurrences with the string 2
    for character in s2:
        if character in dict_s1:
            if dict_s1[character] != 0:
                dict_s1[character] -= 1
            else:
                return False
        else:
            return False

    return True


