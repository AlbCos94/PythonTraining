"""
# Given a collection of numbers, you should find a matching pair that it is equal to a given sum
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


# linear implementation / middle implementation
def pair_numbers2(list_num, sum):
    list_comp = [] # list of complementary number to get the "sum" number

    for num in list_num:
        if num in list_comp:
            return True
        list_comp.append(sum-num)
    return False