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
            #  -If the buffer is full, it should delete the oldest element
            #   in the buffer to create space BEFORE adding new element.
    #  -Create a 'get()' method in the 'RingBuffer' class that will
    #   return all the elements in the buffer list, in order.
            #  -It should NOT return any 'None' values if they exist.


#---------------------------DEVISING A PLAN------------------------------
#------------------------IMPLEMENTING THE PLAN---------------------------
#------------------------REFLECTION & ITERATION--------------------------

class RingBuffer:
  def __init__(self, capacity):
    self.capacity = capacity
    self.current = 0
    self.storage = [None]*capacity

  def append(self, item):
    pass

  def get(self):
    pass