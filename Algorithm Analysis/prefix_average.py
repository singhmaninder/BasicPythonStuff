""" Prefix Average basically averages all the previous values.
It is used to find the prefix average for every location in
an array. Prefix average is very useful in financial applications."""

def prefix_average1(S):
    """Quadratic-Time Algorithm"""
    n = len(S)        # This statemement executes in constant time.
    A = [0] * n       # This runs in O(n) time.

    for j in range(n):   # The outer for loop runs in O(n) time.
        total = 0
        for i in range(j + 1):  # The inner for loop contributes O(n2) time.
            total += S[i]
        A[j] = total / (j + 1)
    
    return A

""" Output
>>> prefix_average1([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
[1.0, 1.5, 2.0, 2.5, 3.0, 3.5, 4.0, 4.5, 5.0, 5.5]

The running time of algorithm is O(n2).
"""

def prefix_average2(S):
    """Liner-Time Algorithm"""
    n = len(S)        # This statemement executes in constant time.
    A = [0] * n       # This runs in O(n) time.

    total = 0
    for i in range(n):  # This runs in O(n) time.
        total += S[i]   # O(1)
        A[i] = total / (i + 1) # O(1)
 
    return A

""" Output
>>> prefix_average2([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
[1.0, 1.5, 2.0, 2.5, 3.0, 3.5, 4.0, 4.5, 5.0, 5.5]

The running time of algorithm is O(n).
"""
