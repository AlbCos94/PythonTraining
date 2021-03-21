# compare different operations performed on a data structure


#Examples to construct a list that is [0,1,2,....10000]
def method1(n):
    l = []
    for num in range(n):
        l = l +[num]
    return l

def method2(n):
     l = []
     for num in range(n):
         l.append(n)
     return l

def method3(n):
    l = [num for num in range(n)]
    return l

# built in functions are always the most efficient methods
def method4(n):
    l = range(n)
    return l