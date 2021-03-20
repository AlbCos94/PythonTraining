# script to work with Big O analysis
# Big O Notation is usefull to have an objective mesurement (not depending on your computer ) to know time and memory efficient is an algorithm
# Big-O Analysis (asimptotic analysis) --> how quickly runtime will grow relative to the input as the input get arbitrarily large
import time


#example of the sum of all the numbers that are behing in the range of a certain number

# O(n) function
def sum1(n):
    final_sum = 0

    for x in range (n+1):
        final_sum += x

    return final_sum
# function "sum1" would take always n+1 steps ( always corresponding to the input dimension )
# sum1 is O(n) --> runtime grows linearly with the input size (linear Big-O)

# 0(1) Constant
def sum2(n):
    return (n*(n+1))/2

def func_const(value): # regardless the list size we get the first element of the list
    return value[0]

# O(n) Liniear
def func_lin(list): # executes as many elements as its input
    l_output=[]
    for val in list:
        l_output.append(val)

# O(n^2) Quadratic
def func_quad(list): # for n elements we will have to execute n*n operations
    l_output = []
    for item_1 in list:
        for item_2 in list:
            l_output.append(item_2)
            l_output.append(item_1)


# we check how much time takes to execute these two functions X times
# if we check with 100000 times, the second one takes 1/6 of the time of the first one
# we use a funtion that gets as argument a 1 argument function
def checkTimeFunc1Arg_Xtimes(func_1_arg, func_arg, num_times):
    i_time = time.time()

    for i in range(num_times):
        func_1_arg(func_arg)

    time_diff = time.time() - i_time

    return time_diff

""" 
def checkTimeSum2_Xtimes(n, num_times):
    i_time = time.time()
    for i in range(num_times):
        sum2(n)

    time_diff = time.time() - i_time
    return time_diff
"""

