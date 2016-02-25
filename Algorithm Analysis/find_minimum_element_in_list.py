# This program is used to find minimum number in a list.
# There are two methods to do this. First method have 
# complexity O(n2) and second method have complexity O(n)

class FindMinimumListNumber(object):
    """ This class provides two methods to find
        the minimum number in the list.
    """
    
    def find_minimum_number_with_high_complexity(self, num_list):
        """ This method returns the minimum number in 
            the list having complexity O(n2).
        """
        # We use bubble sort algorithm here
        for num in range(len(num_list) - 1, 0, -1):
            for n in range(num):
                if num_list[n] > num_list[n+1]:
                    num_list[n], num_list[n+1] = num_list[n+1], num_list[n]
        
        # Now our list is sort in ascending order. So first number is 
        # the minimum number in the list
        
        minimum_number = num_list[0]
        
        return minimum_number
    
    def find_minimum_number(self, num_list):
        """ This method returns the minimum number in
            the list having complexity O(n).
        """
        minimum_number = num_list[0] if num_list else []
        
        for num in num_list[1:]:
            if num < minimum_number:
                minimum_number = num
        
        return minimum_number


find_min_num = FindMinimumListNumber()
num_list = [54,26,93,17,77,31,44,55,20,150]
min_num_high_complexity = find_min_num.find_minimum_number_with_high_complexity(num_list)
min_num = find_min_num.find_minimum_number(num_list)

print 'min_num_high_complexity', min_num_high_complexity
print 'min_num', min_num