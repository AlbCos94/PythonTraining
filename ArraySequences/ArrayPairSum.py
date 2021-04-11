"""

Given an integer array, output all the unique pairs that sum up to a specific value k

so the input
    pair_sum([1,3,2,2],4)
would return 2 pairs:
    (1,3)
    (2,2)

"""

"""
personal solution
"""

def pair_sumV1(arr, k):
    list_pairs = []

    for index in range(len(arr)):
        complement = k - arr[index]

        if complement in arr[(index+1):]:
            pair = (arr[index], complement)
            pair = sorted(pair)

            if pair not in list_pairs: # we want only unique pairs
                list_pairs = list_pairs + [pair]

    """ 
    for pair in list_pairs:
        print(pair)
    """

    return len(list_pairs)

"""
Udemy Solution

O(N) -> linear pass from the beginning and for each element we check weather k-element is in the set of seen numbers.
if it is, then we found a pair of sum k and add it to the output. if not, this element doesnt belong to a pair yet, and we add it to the set of seen elements
"""

def pair_sumV2(arr, k):

    # Edge Case check
    if len(arr)<2:
        return "Array not long enough"

    # Sets for tracking
    seen = set()
    output = set() # set of tuples that we are gonna build up and which sum "k"

    for num in arr:
        target = k-num #complementary number --> what we want to find to consider it a pair

        if target not in seen:
            seen.add(num)

        else:
            output.add( (min(num,target), max(num,target) ) )# we add the pair to the output set and we order it from min to max)

    return len(output) # we return the number of tuples that we found summing "k"