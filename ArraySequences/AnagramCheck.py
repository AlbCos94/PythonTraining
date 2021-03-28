"""
Given two strings, check to see if there are anagrams. An anagram is when the two strings can be written using the exact same letters
so you can rearrange the letters to get different phrase or word
Example

"public relations" and "crap built on lies" --> true
"clint eastwood" and "old west action"

note: spaces and capitalizations can be ignored
"""

def diagramV1(s1,s2):
    # first we remove spaces
    s1=s1.replace(" ", "")
    s2=s2.replace(" ", "")
    # we remove capital letters
    s1=s1.lower()
    s2=s2.lower()

    print(s1)
    print(s2)

    seen = []

    for letter in s1:




    return False