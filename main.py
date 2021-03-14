from pair_numbers import pair_numbers as pn # from "Folder" where it is, import file as abreviation
from ReverseLinkedList import reverse_list as rl # from Folder where it is, import file
#from ReverseLinkedList import LinkeList


def main ():
    import doctest
    #doctest.testfile("pair_numbers/doctest_pair_numbers")
    doctest.testfile("ReverseLinkedList/doctest_reverse_list")

    """ 
    a = rl.LinkeList(3)
    b = rl.LinkeList(4)
    c = rl.LinkeList(5)
    d = rl.LinkeList(6)

    a.next = b #head_list
    b.next = c
    c.next = d
    d.next = None
    #a -> b -> c -> d
    rl.ReverseLinkedList(a)
    #d -> c -> b -> a

    print(a.next)
    print(b.next.value)
    print(c.next.value)
"""

if __name__ == '__main__':
    main()
