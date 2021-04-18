"""
Consider an array of non-negative integers.
A second array is formed by shuffling the elements of the first array and deleting a random element
Given these two array, find which element is missing in the second array

"""
# NOT USE OF SET --> they cannot contain duplicates
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

