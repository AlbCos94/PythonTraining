"""
Given a string of words, reverse all the words.
For example:
    Given: "This is the best"
    Return: "best the is This"

(Remove all leading and trailing whitespaces)
"   space here " --> "space here"

"""

"""
my solution
"""
def rev_wordV1(s):
    # remove leading spaces, newline and tab characters using "lstrip()"
    s.lstrip()
    # we create a list of words using the split() operator
    list_words = s.split()
    number_words = len(list_words)
    new_s = ""

    # we move along the list of words starting at the end
    for i in reversed(range(0, number_words)):
        new_s += list_words[i]

        # we add blank spaces as along as we don`t reach the last word of the sentence
        if i != 0:
            new_s += " "

    return new_s


"""
Udemys Solution
built in python solution
"""
def rev_wordV2(s):
    return " ".join(reversed(s.split()))

"""
Udemys Solution
manual python solution
"""
def rev_wordV3(s):
    words = []
    length = len(s)
    spaces = [' ']

    i = 0

    # split the strin into a list of words
    while i < length:
        if s[i] not in spaces:

            word_start = i

            while i < length and s[i] not in spaces:
                i += 1

            words.append(s[word_start:i]) # we add the word (set of string characters not containing spaces) to the list
        i += 1

        # we use blank space to join the words  of the list into a string -> " ".join
    return " ".join(reversed(words))