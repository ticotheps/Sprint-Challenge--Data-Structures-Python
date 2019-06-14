#-----------------------UNDERSTANDING THE PROBLEM------------------------

#  Ring Buffer:
    #  -A type of data structure
    #  -Useful for:
            #  -Storing log information
            #  -Storing history information
    #  -Fixed in size (cannot grow beyond the fixed capacity)
    #  -Information is stored with an 'expiration' date/age
    #  -Data can be overwritten once expiration date/age is reached
    
#  ASSIGNED TASK:
    #  -Create an 'append()' method in the 'RingBuffer' class that will
    #   add elements to the buffer.
            #  -It should add an element to the buffer it hasn't reached
            #   max capacity yet.
            #  -If the buffer is full, it should overwrite the oldest
            #   element in the buffer with the new element 
    #  -Create a 'get()' method in the 'RingBuffer' class that will
    #   return all the elements in the buffer list, in order.
            #  -It should NOT return any 'None' values if they exist.

#---------------------------DEVISING A PLAN------------------------------

#  append(item):
    #  Expected Input: an item (i.e. - string, int, etc.)
    #  Expected Output: None
    
    #  STEPS TO APPEND NEW ITEM:
           #  1) Assess whether or not buffer is currently full.
           #  2) If buffer is NOT full, add item to end of buffer.
           #  3) If buffer IS full, overwrite oldest item (first item)
           #     in the buffer with the new item.   
           
#  get():
    #  Expected Input: None
    #  Expected Output: an array (i.e. - ['a', 'b', 'c'])
    
    #  STEPS TO GET BUFFER:
           #  1) Create a new empty array called 'gotBufferList'.
           #  2) Loop over buffer and append all NON-'None' values to
           #     'gotBufferList' array.
           #  3) Return 'gotBufferList' array.

#  Please see commented code below, inside the 'RingBuffer' class.

#------------------------IMPLEMENTING THE PLAN---------------------------

class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = 0   #  indicates total # of current items in buffer
        self.storage = [None]*capacity

    #  Adds an item to a designated location in the buffer, depending on
    #  if buffer has reached capacity
    def append(self, item):
        #  1) If buffer IS full, overwrite oldest (1st) item with new item.
        if self.current == self.capacity:
            self.storage[self.current] = item
            self.current = (self.current + 1) % self.capacity
        #  2) If buffer is NOT full, add the element to the end of buffer.
        else:
            self.storage.append(item)
    #  Retrieves all the items in the buffer, excluding values of "None"
    def get(self):
        #  1) Creates a new empty array called 'gotBufferList'.
        #  2) Loops over buffer and appends all NON-'None' values to the
        #     'gotBufferList' array.     
        #  3) Returns modified copy of original buffer, but without 'None'
        #     values included in the copy.
        pass
      
#------------------------REFLECTION & ITERATION--------------------------