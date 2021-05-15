"""
implementation of a Queue Class

"""

class Queue(object):


    # cosntructor
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        # insert --> inserts an object before the given index
        self.items.insert(0, item)

    def dequeue(self):
        """
        first_queue = self.items[-1]
        self.items = self.items[0:-2]
        return first_queue
        """
        # better to use the build-in method for lists --> pop() , to remove the last element
        return self.items.pop()

    def isEmpty(self):
        return self.items == []

    def size(self):
        return self.items.size()

    def print_elements(self):
        for e in self.items:
            print(e)