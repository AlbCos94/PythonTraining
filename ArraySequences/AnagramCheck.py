"""
Given two strings, check to see if there are anagrams. An anagram is when the two strings can be written using the exact same letters
so you can rearrange the letters to get different phrase or word
Example

"public relations" and "crap built on lies" --> true
"clint eastwood" and "old west action"

note: spaces and capitalizations can be ignored
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