"""

Given an array of integers (positive and negative) find the largest continuous sum

"""
# we look for points of inflexion when the numbers are negative, to check if it is worthy starting a new series

def largest_cont_sumV1(arr):
    sum = arr[0] # already setting first element as the first sum
    max_sum = sum
    for e in arr[1:]:
        if (e < 0) and (abs(e) >= sum): # reset and start a new series sum
            sum = 0
        else: # we continue with the series
            sum += e

        if (sum > max_sum):
            max_sum = sum

    return max_sum


'''
Udemy Version Solution
'''

def largest_cont_sumV2(arr):

    # edge case check
    if len(arr)==0:
        return 0

    max_sum = current_sum = arr[0]

    for num in arr[1:]:
        current_sum = max(current_sum+num, num)

        max_sum = max(current_sum, max_sum)

    return max_sum