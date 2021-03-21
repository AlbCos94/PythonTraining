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

# O(n) Liniear order
def func_lin(list): # executes as many elements as its input
    l_output = []
    for val in list:
        l_output.append(val)

# O(2n) --> O(n) -_> Liniear order (still) --> it can be consider to have the same effect as a linear function.. since if we do the asimptotic limit the constant "2" of 2xLinear drops
def func_2lin(list): # executes as many elements as its input
    l_output_1 = []
    l_output_2 = []
    for val in list:
        l_output_1.append(val)
    for val in list:
        l_output_2.append(val)

def combinationOrder(list):
    list_output = [0] # O(1) "operation"  -> constant

    mid_point = round(len(list)/2) # O(n/2) --> O(1/2 * n) --> linear (the constants drop when we do limit to infinit)
    for val in list[:mid_point]:
        list_output.append(val)

    for x in range(10): # O(10) --> constant
        list_output.append(x)

    # in total we have --> O(1 + n/2 + 10) --> linear

# O(n^2) Quadratic
def func_quad(list): # for n elements we will have to execute n*n operations
    l_output = []
    for item_1 in list:
        for item_2 in list:
            l_output.append((item_1, item_2))

# linear O(n) --> in this next function we should consider the worst case scenario, which would be having to loop around the whole list, since no one mathces or the last one was a match
# the best case scenarios would be., to match in the first element
def matcher(list, match):
    for item in list:
        if item == match:
            return True
        else:
            return False

# difference between space complexity and time complexity
# time complexity  --> order n
# memory complexity --> order O(1)
def fix_value(n):
    value = 1
    for x in range(n):
        value = n+value
    return value


# we check how much time takes to execute these two functions X times
# if we check with 100000 times, the second one takes 1/6 of the time of the first one
# we use a funtion that gets as argument a 1 argument function
def checkTimeFunc1Arg_Xtimes(func_1_arg, func_arg, num_times):
    i_time = time.time()

    for i in range(num_times):
        func_1_arg(func_arg)

    time_diff = time.time() - i_time

    return time_diff

def checkTimeFunc2Arg_Xtimes(func_2_arg, func_arg_1, func_arg_2, num_times):
    i_time = time.time()

    for i in range(num_times):
        func_2_arg(func_arg_1,func_arg_2)

    time_diff = time.time() - i_time

    return time_diff

