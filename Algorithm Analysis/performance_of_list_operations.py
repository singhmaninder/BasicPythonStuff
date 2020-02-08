# In this program we are determine the performance
# of various list operations

# Let us look at four different ways we might generate a list of n numbers starting with 0. First
# we will try a for loop and create the list by concatenation, then we will use append rather
# than concatenation. Next, we will try creating the list using list comprehension and finally,
# and perhaps the most obvious way, using the range function wrapped by a call to the list
# constructor. The following code shows making our list in four different ways.

from timeit import Timer

def test1():
    l = []
    for i in range(1000):
        l = l + [i]

def test2():
    l = []
    for i in range(1000):
        l.append(i)

def test3():
    l = [i for i in range(1000)]

def test4():
    l = list(range(1000))

def test5():
    pass
    
t1 = Timer("test1()", "from __main__ import test1")
print("concat ", t1.timeit(number=1000), "milliseconds")

t2 = Timer("test2()", "from __main__ import test2")
print("append ", t2.timeit(number=1000), "milliseconds")

t3 = Timer("test3()", "from __main__ import test3")
print("Comprehension ", t3.timeit(number=1000), "milliseconds")

t4 = Timer("test4()", "from __main__ import test4")
print("list range ", t4.timeit(number=1000), "milliseconds")

t5 = Timer("test5()", "from __main__ import test5")
print("Empty function ", t5.timeit(number=1000), "milliseconds")

# Output: concat  1.80392530618 milliseconds
# append  0.0968858552769 milliseconds
# Comprehension  0.040939684134 milliseconds
# list range  0.0106607617765 milliseconds
# Empty function  0.00011566279729 milliseconds

# Let us see performance of pop operation

pop_zero = Timer("x.pop(0)", "from __main__ import x")
pop_end = Timer("x.pop()", "from __main__ import x")

x = list(range(2000000))
print('pop zero ', pop_zero.timeit(number=1000))

x = list(range(2000000))
print('pop end ', pop_end.timeit(number=1000))

# Output: pop zero  0.884143163149
# pop end  0.000138490980965