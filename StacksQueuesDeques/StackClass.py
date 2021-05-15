"""
implementation of a Stack Class

"""

class Stack(object):

    # cosntructor
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    # we add an element to the end of the stack
    def push(self, item):
        self.items.append(item)

    # pop method will remove the very first element of the stack
    def pop(self):
        return self.items.pop()

    # with peek we just return the last element that we added to the stack , but we dont remove it
    def peek(self):
        return self.items[len(self.items)-1]

    def size(self):
        return len(self.items)

    def print_elements(self):
        for e in self.items:
            print(e)
