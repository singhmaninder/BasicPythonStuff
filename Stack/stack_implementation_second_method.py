# In our first method of implementation we are using a list where the top is 
# at beginning instead of the end. In this case the previous pop and append
# methods would no longer work and we would have to index position 0 (the
# first item in the list) explicitly using pop and insert. The performance
# of this implementation is suffer in that the insert(0) and pop(0) operations
# will both require O(n) for a stack of size n. The implementation is below. 


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
        self.items.insert(0, item)
    
    def pop(self):
        """ This method remove an item from the
            top of the stack.
        """
        if self.items:
            return self.items.pop(0)
        else:
            return 'Stack is empty.'
    
    def peek(self):
        """ This method returns the item which is on
            the top of the stack.
        """
        return self.items[0]
    
    def size(self):
        """ This method returns the total size
            of the stack.
        """
        return len(self.items)


if __name__ == '__main__':
    s = Stack()
    print(s.is_empty())
    s.push(4)
    s.push('Maninder')
    print(s.peek())
    s.push(True)
    print(s.size())
    print(s.is_empty())
    s.push(8.4)
    print(s.pop())
    print(s.pop())
    print(s.size())

    print(s.items)

# Output: True
# Maninder
# 3
# False
# 8.4
# True
# 2
# ['Maninder', 4]