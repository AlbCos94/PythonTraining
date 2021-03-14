"""
# Given a collection of numbers, you should find a matching pair that it is equal to a given number
# The list os already sorted from smaller to bigger
# [1,2,3,9] Sum=8 --> False
# [1,2,4,4] Sum=8 --> True
"""
# quadratic implementation / easy implementation
def pair_numbers(list_num, sum):
    for num1 in list_num:
        for num2 in list_num:
            if (num1+num2==sum):
                return True
    return False

# nlog(n) implementation / middle implementation
def pair_numbers2(list_num, sum):
    list_comp = [] # list of complementary number to get the "sum" number

    for num in list_num:
        if num in list_comp:
            return True
        list_comp.append(sum-num)
    return False

# linear implementation / scanning the list in both directions from bottom to top. calculate the sum with the extrems.
# moving the top extrem to the left if the summ of both extrems is bigger than the number ( we will make the top extrem smaller)
# moving the bottom to the right if the result is lower than the number ( we will make the bottom extrem bigger)
def pair_numbers3(list_num, sum):
    index_bottom = 0
    index_top = len(list_num)-1

    while index_bottom<index_top:
        sum_extremes = list_num[index_bottom] + list_num[index_top]
        if sum_extremes == sum:
            return True
        elif sum_extremes > sum: # that means that the index_top was too big
            index_top -= 1
        else:
            index_bottom += 1

    return False

# case in which the input list doesnt have the numbers sorted in an specific order
def pair_numbers4_list_not_sorted(list_num, sum):
    list_of_complements = []

    for num in list_num:
        complement = sum - num
        if complement in list_of_complements:
            return True
        else:
            list_of_complements.append(complement)
    return False

# creation of a hash table to have a constant time look up
# Hash tables are a type of data structure in which the address or the index value of the data element is generated from a hash function. That makes accessing the data faster as the index value behaves as a key for the data value.
# In Python, the Dictionary data types represent the implementation of hash tables.
def pair_numbers5_list_not_sorted(list_num, sum):
    dict_complements = {}

    for num in list_num:
        complement = sum - num
        if dict_complements.get(complement):
            return True
        else:
            dict_complements[complement] = num
    return False



# Computational Time / Running Time / Time Complexity
# Length of time required to perform a computational process. Computational time is proportional to the number of rule applications
# Commonly estimated by counting the number of elementary operations performed by the algorithm
# One usually focuses on the behavior of the complexity when the input size increases --> asymptotic behavior of the complexity.
# Complexity is commonly used using "big O notation" --> O(n), O(nlogn), O(n^alpha)
# O(n) --> linear time algorithm
# O(n^alpha) --> polynomial time algorithm
# O(log n) --> Logarithmic running time ( O(log n) ) essentially means that the running time grows in proportion to the logarithm of the input size -
#               as an example, if 10 items takes at most some amount of time x , and 100 items takes at most, say, 2x , and 10,000 items takes at most 4x

# Linear Method --> the time it takes increases linearly with the number of elements involved. For example, a for loop which prints the elements of an array is roughly linear:
# written as O(N) --> the time or computational effort to run the algorithm is proportional to N ( number elements that has as Input )
'''
example:
for x in range(10):
    print x
'''

# Quadratic Method --> every time you increase the number of elements, then computational effort or time will increase as the square of the number of elements
# written as O(N*N) or O(N^2)
'''
example --> 10 elements as input but it will process 10x10 = 100 elements
for x in range(10):
    for y in range(10):
        print x, y
'''