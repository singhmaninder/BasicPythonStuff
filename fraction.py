# This program implements abstract data type Fraction

class Fraction(object):
    
    def __init__(self, top, bottom):
        self.num = top
        self.den = bottom
        
    def __add__(self, other_fraction):
        """ This method add two Fraction objects
        """
        new_num = self.num * other_fraction.den + self.den * other_fraction.num
        new_den = self.den * other_fraction.den
        common = Fraction.gcd(new_num, new_den)
        return Fraction(new_num // common, new_den // common)
        #return str(new_num) + "/" + str(new_den)
    
    def __eq__(self, other):
        """ This method compare two Fraction objects
        """
        first_num = self.num * other.den
        second_num = other.num * self.den
        
        return first_num == second_num
    
    def __mul__(self, other):
        """ This method multiply two Fraction objects
        """
        num = self.num * other.num
        den = self.den * other.den
        common = Fraction.gcd(num, den)
        
        return Fraction(num // common, den //common)
    
    @staticmethod
    def gcd(m, n):
        """ This method return gcd of two numbers
        """
        while m % n != 0:
            old_m = m
            old_n = n
            
            m = old_n
            n = old_m % old_n
        return n
    
    def __str__(self):
        return str(self.num) + "/" +str(self.den)

f1 = Fraction(1, 2)
f2 = Fraction(2, 3)
f3 = Fraction(2, 3)


print f1 + f2
print f1 == f2
print f2 == f3
print f1 * f3 * f2

