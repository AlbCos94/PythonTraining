from pair_numbers import pair_numbers as pn # from "Folder" where it is, import file as abreviation
from ReverseLinkedList import reverse_list as rl # from Folder where it is, import file
from BigO import run_0_analysis as run_0
from ArraySequences import Arrays as ar
from ArraySequences import AnagramCheck as ac
from ArraySequences import ArrayPairSum as aps

#from ReverseLinkedList import LinkeList


def main ():
    import doctest
    #doctest.testfile("pair_numbers/doctest_pair_numbers")
    #doctest.testfile("ReverseLinkedList/doctest_reverse_list")
    #run_0.run_BigO_DataStructures_analysis()
    #ar.behaviour_dyn_arrays(100)
    #ar.Test_DynamicArray_Class()
    #ac.anagramV1("HOLA Rohit DADSsss","asdsa WESD")
    #doctest.testfile("ArraySequences/doctest_AnagramCheck")
    #doctest.testfile("ArraySequences/doctest_ArrayPairSum")
    #doctest.testfile("ArraySequences/doctest_finder_missing")
    doctest.testfile("ArraySequences/doctest_largest_cont_sum")

if __name__ == '__main__':
    main()
