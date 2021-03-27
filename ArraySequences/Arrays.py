
# we import the system modul to know the bytes size that the computer is holding in memory
import sys
import ctypes

# example of dynamic arrays
# the real size in bytes for that array is greater than tha one used or the same
# python increases the byte space available by "chunk increments" that embrace different ranges
# the chunks added are greater, the longer the array already is
def behaviour_dyn_arrays(n):
    data=[]

    for i in range(n):
        #Number of elements
        a = len(data)

        #Real Size in Bytes
        b = sys.getsizeof(data)

        print('Lenght: {0:3d}; Size in bytes: {1:4d} '.format(a, b))

        #increase length by one
        data.append(n)

# implementation of a Dynamic Array

class DynamicArray(object):
    """
    Dynamic Array Class ( similar to Python lists)
    """

    def __init__(self):
        self.n = 0 # count of current number of elements(default is 0)
        self.capacity = 1 # default capacity
        self.A = self.make_array(self.capacity)

    """
    __specialMethod__
    __double_leading_and_trailing_underscore__
    This convention is used for special variables or methods (so-called “magic method”) such as__init__, __len__. 
    These methods provides special syntactic features or does special things. For example, __file__ indicates the location of Python file, __eq__ is executed when a == b expression is excuted. 
    A user of course can make custom special method, it is very rare case, but often might modify the some built-in special methods. (e.g. You should initialize the class with __init__ that will be executed at first when a instance of class is created.)
    """

    def __len__(self): # special methods
        """
        Return number of elements sorted in array
        """
        return self.n

    def __getitem__(self, k):
        """
        Return element at index "k"
        """
        if not 0 <= k < self.n:
            return IndexError("k index is out of bounds!") #exeption implementation

        return self.A[k]

    def append(self, element):
        """
        Add elements to the end of that array.
        In case array already full, capacity of that array is increased before adding that element
        """
        if self.n == self.capacity:
            self._resize(2*self.capacity) # we double the capacity always when there is not enough room

        self.A[self.n] = element # we add the element at the end of the array in the case we had still space
        self.n += 1 # we increase the number of elements of that array

    """
    _nameMethod means "private method" 
    """
    def _resize(self, new_cap): # private method --> user will not need to use that method, "it will be used in the background" and to implements other methods
        B = self.make_array(new_cap) # an array with room of "new_cap" and empty is created.

        for k in range(self.n): # new array is filled with the content of the previous array
            B[k] = self.A[k]

        self.A = B # Call A the new bigger array
        self.capacity = new_cap # set the new capacity

    def make_array(self, capacitiy):
        """
        return a new array with that capacity
        ctypes to create a "raw array" holder
        """
        return(capacitiy * ctypes.py_object)()

    def print_whole_array(self):
        for i in range(self.n):
            print(self.A[i])
        return


def behaviour_DynamicArrayClass(n):
    data = DynamicArray()
    for i in range(n):
        #Number of elements
        a = len(data)

        #Real Size in Bytes
        b = sys.getsizeof(data)

        print('Lenght: {0:3d}; Size in bytes: {1:4d} '.format(a, b))

        #increase length by one
        data.append(n)

def Test_DynamicArray_Class():
    arr = DynamicArray() # mehtod __init__ is activated
    arr.append(1)
    arr.append(3)
    arr.append(123133)
    arr.print_whole_array()
    print(len(arr))
    print(arr[343]) # triggering an exception
    print("Test of the Array Behaviour by increasing up to 100 elements: ")
    behaviour_DynamicArrayClass(100)