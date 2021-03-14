# reverse a List of elements that are pointing among them

# a -> b -> c -> d -> None
# d -> b -> c -> a -> None

#class of the input Linked List
class LinkeList:
    def __init__(self, value):
        self.value = value
        self.next = None # next element of the class LinkeList

# None -> a -> b -> c -> d -> None
# None -> d/ -> c -> b -> a -> None

def ReverseLinkedList(head):
    current = head #a
    previous_member = None
    while (current.next != None ): #current --> d

        next_member_old = current.next #d
        current.next = previous_member #b
        # preparation for the next one
        previous_member = current # c
        current = next_member_old # d

    current.next = previous_member
    return


