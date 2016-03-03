# Completed implementation of a stack Abstract Data Type (ADT)
# In this implementation we are using a list where the top is at
# beginning instead of the end. The append() and pop() operations 
# were both O(1). This means that this implementation will perform
# push and pop operation in constant time no matter how many items
# are on the stack.

class Stack(object):
    """ This class provides complete implementation
        of stack data structure.
    """
    
    def __init__(self):
        self.items = []
    
    def is_empty(self):
        """ This method check that whether the 
            stack is empty or not.
        """
        return self.items == []
    
    def push(self, item):
        """ This method insert an item at the end
            of the stack.
        """
        self.items.append(item)
    
    def pop(self):
        """ This method remove an item from the
            top of the stack.
        """
        if self.items:
            return self.items.pop()
        else:
            return 'Stack is empty.'
    
    def peek(self):
        """ This method returns the item which is on
            the top of the stack.
        """
        return self.items[len(self.items) - 1]
    
    def size(self):
        """ This method returns the total size
            of the stack.
        """
        return len(self.items)


if __name__ == '__main__':
    s = Stack()
    print s.is_empty()
    s.push(4)
    s.push('Maninder')
    print s.peek()
    s.push(True)
    print s.size()
    print s.is_empty()
    s.push(8.4)
    print s.pop()
    print s.pop()
    print s.size()

    print s.items

# Output: True
# Maninder
# 3
# False
# 8.4
# True
# 2
# [4, 'Maninder']