from pair_numbers import pair_numbers as pn # from "Folder" where it is, import file as abreviation
from ReverseLinkedList import reverse_list as rl # from Folder where it is, import file
from BigO import run_0_analysis as run_0

#from ReverseLinkedList import LinkeList


def main ():
    import doctest
    #doctest.testfile("pair_numbers/doctest_pair_numbers")
    #doctest.testfile("ReverseLinkedList/doctest_reverse_list")
    run_0.run_all_analysis()

if __name__ == '__main__':
    main()
