"""

Given an array of integers (positive and negative) find the largest continuous sum

"""
# we look for points of inflexion when the numbers are negative, to check if it is worthy starting a new series

def largest_cont_sumV1(arr):
    max_sum = -999999
    sum = 0
    for e in arr:
        if e < 0 and abs(e) >= sum: # reset and start a new series sum
            sum = 0
        else: # we continue with the series
            sum += e

        if (sum > max_sum):
            max_sum = sum

    return max_sum