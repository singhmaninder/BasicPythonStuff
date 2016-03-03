from stack_implementation_second_method import Stack

class ReverseString(object):
    """ This class provides implementation of reverse
        a string
    """
    
    def reverse_string(self, input_string):
        """ This method reverse the string using Stack.
        """
        # create an object of Stack class.
        s = Stack()
        if input_string:
            for char in input_string:
                s.push(char)
    
            return ''.join(s.items)
        else:
            return 'String is empty.'


if __name__ == '__main__':
    r1 = ReverseString()
    print r1.reverse_string('Maninder Singh')
    print r1.reverse_string('Once there was a crow')

# Output: hgniS redninaM
# worc a saw ereht ecnO