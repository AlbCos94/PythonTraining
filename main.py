from pair_numbers import pair_numbers as pn # from "Folder" where it is, import file as abreviation
from ReverseLinkedList import reverse_list as rl # from Folder where it is, import file
from BigO import BigO as bo

#from ReverseLinkedList import LinkeList


def main ():
    import doctest
    #doctest.testfile("pair_numbers/doctest_pair_numbers")
    #doctest.testfile("ReverseLinkedList/doctest_reverse_list")
    sum = bo.sum1(10)
    sum2 = bo.sum2(10)
    print (sum)
    print( "time first function = ")
    print(bo.checkTimeSum1_Xtimes(10,100000))
    print( "time second function = "  )
    print(bo.checkTimeSum2_Xtimes(10,100000))
    print(sum2)

if __name__ == '__main__':
    main()
