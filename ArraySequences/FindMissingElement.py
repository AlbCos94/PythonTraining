"""
Consider an array of non-negative integers.
A second array is formed by shuffling the elements of the first array and deleting a random element
Given these two array, find which element is missing in the second array

"""
import _collections



# NOT USE OF SET --> they cannot contain duplicates
# Use of a hash-table
def finderV1(arr1, arr2):

    if ( len(arr1) != ( len(arr2)+1 ) ):
        print("ERROR: Conditions are not accomplished")

    dicc1 = {}

    # dictionary array1 creation
    for e in arr1:
        if e in dicc1.keys():
            dicc1[e] += 1
        else:
            dicc1[e] = 1
    # dictionary array1 extraction regarding array2
    for e in arr2:
        if e in dicc1.keys():
            if dicc1[e] > 0:
                dicc1[e] -= 1
        else:
            print("ERROR second array")

    # check dictionary values, which element was not cleaned out
    for key_i in dicc1.keys():
        if dicc1[key_i] > 0:
            return key_i

    print("not found missing element")
    return

    # we return the only element remaining
    return set1.pop()


# Version number 2
# the complexity is O(NlogN)
def finderV2(arr1, arr2):

    #checking lenght of the arrays
    if ( len(arr1) != ( len(arr2)+1 ) ):
        print("ERROR: Conditions are not accomplished")

    #sort of the arrays
    arr1.sort()
    arr2.sort()

    # iterate along the elements of array 2
    for i in range(len(arr2)): # taking as a reference the shortest one:
        if arr1[i] != arr2[i]:
            return arr1[i]

    return arr1[-1] # not found discrepancies, then we return the last element of the array arr1, whoch was not checked


# Udemy Version of the Solution
def finderV3(arr1, arr2):

    #checking lenght of the arrays
    if ( len(arr1) != ( len(arr2)+1 ) ):
        print("ERROR: Conditions are not accomplished")

    #sort of the arrays
    arr1.sort()
    arr2.sort()

    # use of "zip" to pair elements of two lists in tuples
    """
    zip([1,2,3],[4,5,6])
    [(1, 4), (2, 5), (3, 6)]
    """
    for num1, num2 in zip(arr1, arr2):
        if num1 != num2:
            return num1
    return arr1[-1]


# second version of Udemy soplution
# Use of Colection as a Hash table to track the number of appearances
def finderV4(arr1, arr2):

    # collection --> default dictionary but when adding a key that doesnt exist, intead of arising an error it just add that new key
    d = _collections.defaultdict(int)


    for num in arr2: # by using "collection" we save creating the case when the key in the dictionary doesnt exist
        d[num] += 1

    for num in arr1:
        if d[num] == 0:
            return num
        else:
            d[num] -= 1

# third version of Udemy solution
# sum elements of each list --> the difference is the number missing
# clever one.. but could arise problems of overflow when lists are too long
def finderV5(arr1, arr2):

    num_list1 = sum(arr1)
    num_list2 = sum(arr2)

    return num_list1-num_list2

