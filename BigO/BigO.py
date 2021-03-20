# script to work with Big O analysis
# Big O Notation is usefull to have an objective mesurement (not depending on your computer ) to know time and memory efficient is an algorithm

import time

#example of the sum of all the numbers that are behing in the range of a certain number

def sum1(n):
    final_sum = 0

    for x in range (n+1):
        final_sum += x

    return final_sum

def sum2(n):
    return (n*(n+1))/2


# we check how much time takes to execute these two functions X times
# if we check with 100000 times, the second one takes 1/6 of the time of the first one
def checkTimeSum1_Xtimes(n, num_times):
    i_time = time.time()

    for i in range(num_times):
        sum1(n)

    time_diff = time.time() - i_time

    return time_diff


def checkTimeSum2_Xtimes(n, num_times):
    i_time = time.time()
    for i in range(num_times):
        sum2(n)

    time_diff = time.time() - i_time
    return time_diff