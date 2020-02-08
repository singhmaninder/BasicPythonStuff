# One string is an anagram of another if the second is simply
# a rearrangement of the first. For example, 'heart' and 'earth'
# are anagrams.

class AnagramSolver(object):
    """ This class provides methods to solve anagram
        with different approaches.
    """
    
    def anagram_solution1(self, s1, s2):
        """ This solution will check to see that each character 
            in the first string actually occurs in the second.
        """
        # First check length of both strings, if length is not
        # equal then strings are not anagram.
        
        if len(s1) != len(s2):
            return 'Length of both strings is not equal.'
        
        a_list = list(s2)
        
        pos1 = 0
        is_anagram = True
        
        while pos1 < len(s1) and is_anagram:
            pos2 = 0
            found = False
            while pos2 < len(a_list) and not found:
                if s1[pos1] == a_list[pos2]:
                    found = True
                else:
                    pos2 = pos2 + 1
            
            if found:
                a_list[pos2] = None
            else:
                is_anagram = False
            
            pos1 += 1
        
        return is_anagram
    
    def anagram_solution2(self, s1, s2):
        """ This method implements sort and compare method
            to find that two strings are anagram.
        """
        a_list1 = list(s1)
        a_list2 = list(s2)
        
        a_list1.sort()
        a_list2.sort()
        
        pos = 0
        matches = True
        
        while pos < len(s1) and matches:
            if a_list1[pos] == a_list2[pos]:
                pos += 1
            else:
                matches = False
                
        return matches
    
    def anagram_solution3(self, s1, s2):
        """ This method implements count and compare algorithm
            to find that two strings are anagram.
        """
        c1 = [0] * 26
        c2 = [0] * 26
        
        for i in range(len(s1)):
            pos = ord(s1[i]) - ord('a')
            c1[pos] = c1[pos] + 1
        
        for i in range(len(s2)):
            pos = ord(s1[i]) - ord('a')
            c2[pos] = c2[pos] + 1
        
        
        j = 0
        still_ok = True
        while j < 26 and still_ok:
            if c1[j] == c2[j]:
                j = j + 1
            else:
                still_ok = False
        
        return still_ok

anagram_solver = AnagramSolver()
print(anagram_solver.anagram_solution1('heart', 'earth'))
print(anagram_solver.anagram_solution2('abcd', 'cbad'))
print(anagram_solver.anagram_solution3('apple', 'pleap'))

