# program to find the sum of N integers.
import time

class SumOfIntegers(object):
    """ This class provide implementation of sum of N numbers.
    """
    
    def __init__(self, number):
        self.number = number
    
    def sum_of_numbers(self):
        """ This method use Mathematics formula to calculate sum
            of N numbers
        """
        start = time.time()
        sum_of_nums = self.number * (self.number + 1)/2
        
        end = time.time()
        
        return sum_of_nums, end-start
    
    def sum_of_numbers_using_loop(self):
        """ This method use for loop to calucuate sum
            of N numbers
        """
        start = time.time()
    
        the_sum = 0
        for number in range(1, self.number+1):
            the_sum = the_sum + number
        
        end = time.time()
 
        return the_sum, end-start

#sum_of_intergers = SumOfIntegers(100000000000000)
sum_of_intergers = SumOfIntegers(10000000)
#print sum_of_intergers.sum_of_numbers()
#print sum_of_intergers.sum_of_numbers_using_loop() 
for i in range(5):
    print("Sum is %d required %10.7f seconds" % sum_of_intergers.sum_of_numbers_using_loop())
#for i in range(5):
    #print("Sum is %d required %10.7f seconds" % sum_of_intergers.sum_of_numbers()) 