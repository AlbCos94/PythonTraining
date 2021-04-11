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
def anagramV1(s1,s2):
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

    # we check if both list are the same
    if l1 == l2:
        return True
    else:
        return False

"""
diagramV2:
used of dictionaries to check if strings are anagrams
we are gonna build a dictionary from one of the strings such as:
    key --> character
    value --> number of times that character appears
once we got that dictionary, we will compare it with the other string
"""

def anagramV2(s1,s2):
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

    # building up the dictionary of ocurrences for characters --> add counts for each letter
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

"""
diagramV3:
Udemy Solution 1 --> not the optimal way!!
"""
def anagramV3(s1, s2):
    s1 = s1.replace(' ','').lower()
    s2 = s2.replace(' ','').lower()

    return sorted(s1) == sorted(s2)

"""
diagramV4:
Udemy Solution 2 --> use of dictionary
( the same as diagram V2 )
"""
def anagramV4(s1, s2):
    s1 = s1.replace(' ','').lower()
    s2 = s2.replace(' ','').lower()

    # Edge case Check --> do both have the same number of letters?
    if len(s1) != len(s2):
        return False

    #create a counting dictionary --> substract counts for each letter

    count = {}

    for letter in s1:
        if letter in count:
            count[letter] += 1
        else:
            count[letter] = 1

    for letter in s2:
        if letter in count:
            count[letter] -= 1
        else:
            count[letter] = 1

    for k in count:
        if count[k] != 0:
            return False

    return True
