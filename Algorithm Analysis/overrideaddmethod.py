""" 
we are going to learn about how to override __add__  method while adding two objects in Python.

In Python when we perform sum operation like:

x + y

then what actually happened is that __add__  method of object x is called in following way:

x.__add__(y)

If any exception comes during add operation, then reverse add operation take place in following way:

y.__radd__(x)

It means that we can customise the __add__ methods according to requirements.

Let us understand this with the help of following simple example.
"""

class Hospital(object):
    """ This class contains number of patients that visits the Hospital in a day
    """
    def __init__(self, patients):
        self.number_of_patients = patients

    def __add__(self, other_instance):
        total_number_of_patients = self.number_of_patients + other_instance.number_of_patients
        return Hospital(total_number_of_patients)
    
    def __radd__(self, other_instance):
        if other_instance == 0:
            return self
        else:
            return self.__add__(other_instance)

    def __repr__(self):
        return "Number of patients: {0}".format(self.number_of_patients)


if __name__ == "__main__":
    first_day = Hospital(20)
    second_day = Hospital(30)

    print(first_day)
    print(second_day)
    third_day = first_day + second_day

    print(third_day)

    fourth_day = sum([first_day, second_day, third_day])

    print(fourth_day)
	
# output is below:
# Number of patients: 20
# Number of patients: 30
# Number of patients: 50
# Number of patients: 100

