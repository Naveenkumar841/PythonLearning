import random

#Random Number
#Python does not have a random() function to make a random number, but Python has a built-in module called random that can be used to make random numbers:
"""
Python Random Module
Python has a built-in module that you can use to make random numbers.

Method	Description
seed()	Initialize the random number generator
getstate()	Returns the current internal state of the random number generator
setstate()	Restores the internal state of the random number generator
getrandbits()	Returns a number representing the random bits
randrange()	Returns a random number between the given range
randint()	Returns a random number between the given range
choice()	Returns a random element from the given sequence
choices()	Returns a list with a random selection from the given sequence
shuffle()	Takes a sequence and returns the sequence in a random order
sample()	Returns a given sample of a sequence
random()	Returns a random float number between 0 and 1
uniform()	Returns a random float number between two given parameters
triangular()	Returns a random float number between two given parameters, you can also set a mode parameter to specify the midpoint between the two other parameters
betavariate()	Returns a random float number between 0 and 1 based on the Beta distribution (used in statistics)
expovariate()	Returns a random float number based on the Exponential distribution (used in statistics)
gammavariate()	Returns a random float number based on the Gamma distribution (used in statistics)
gauss()	Returns a random float number based on the Gaussian distribution (used in probability theories)
lognormvariate()	Returns a random float number based on a log-normal distribution (used in probability theories)
normalvariate()	Returns a random float number based on the normal distribution (used in probability theories)
vonmisesvariate()	Returns a random float number based on the von Mises distribution (used in directional statistics)
paretovariate()	Returns a random float number based on the Pareto distribution (used in probability theories)
weibullvariate()	Returns a random float number based on the Weibull distribution (used in statistics)

The random module has a set of methods:
    """
#Example
#Import the random module, and display a random number between 1 and 9:

print(random.randrange(1,10))


"""
Definition and Usage
The randrange() method returns a randomly selected element from the specified range.

Syntax
random.randrange(start, stop, step)

Parameter Values

Parameter	Description
start	    Optional. An integer specifying at which position to start.
            Default 0
stop	    Required. An integer specifying at which position to end.
step	    Optional. An integer specifying the incrementation.
            Default 1
"""

#seed()

"""
Definition and Usage
The seed() method is used to initialize the random number generator.

The random number generator needs a number to start with (a seed value), to be able to generate a random number.
"""
#By default the random number generator uses the current system time.
#Use the seed() method to customize the start number of the random number generator.
#Note: If you use the same seed value twice you will get the same random number twice. See example below

#----Start-----

random.seed(10)
print(random.random())

random.seed(10)
print(random.random())

#the generator creates a random number based on the seed value, so if the seed value is 10, you will always get 0.5714025946899135 as the first random number.
"""
Syntax
random.seed(a, version)

Parameter  Values

Parameter	Description
"a"	Optional. The seed value needed to generate a random number.
If it is an integer it is used directly, if not it has to be converted into an integer.
Default value is None, and if None, the generator uses the current system time.

"version"	An integer specifying how to convert the a parameter into a integer.
Default value is 2
"""

#----END-----

#----Start-----

#Python Random getstate() Method

#a = random.getstate()
#print(a)

"""
Definition and Usage
The getstate() method returns an object with the current state of the random number generator.

Use this method to capture the state, and use the setstate() method, with the captured state, to restore the state

Syntax
random.getstate()

Parameter Values
No parameter values


"""

#----END-----

#----Start-----

#Python Random setstate() Method

""" Capture and restore the state of the random number generator: """
#print a random number:
print(random.random())

#capture the state:
state = random.getstate()

#print another random number:
print(random.random())

#restore the state:
random.setstate(state)

#and the next random number should be the same as when you captured the state:
print(random.random())

""" 
Definition and Usage
The setstate() method is used to restore the state of the random number generator back to the specified state
Use the getstate() method to capture the state

Syntax
random.setstate(state)

Parameter Values

Parameter	Description
state   	Required. A state object. the setstate() method will restore the state of  the random number generator back to this sate.

"""

#----END-----

#----Start-----

#Python Random getrandbits() Method
#Example = Return an 8 bits sized integer

import random 
print(random.getrandbits(4))

#Definition and Usage
#The getrandbits() method returns an integer in the specified size (in bits

""" Syntax
random.getrandbits(n)

Parameter Values
Parameter	Description
n	        Required. A number specifying the size, in bits, of the returned integer.
"""
#----END-----

#----Start-----

#Python Random randint() Method

#Example = Return a number between 3 and 9 (both included):

print(random.randint(3, 9),"'randint'")

#returns a number between 3 and 9 (both included

""" 
Definition and Usage
The randint() method returns an integer number selected element from the specified range.
Note: This method is an alias for randrange(start, stop+1).

Syntax
random.randint(start, stop)

Parameter Values
Parameter	Description
start	    Required. An integer specifying at which position to start.
stop	    Required. An integer specifying at which position to end.

"""

#----END-----

#----Start-----

#Python Random choice() Method

import random

mylist = ["Laptop", "Computer", "Mobile"]

print(random.choice(mylist))

name = "Naveen"

print(random.choice(name))
"""
Definition and Usage
The choice() method returns a randomly selected element from the specified sequence.

The sequence can be a string, a range, a list, a tuple or any other kind of sequence.
Syntax
random.choice(sequence)
    
Parameter   Values
Parameter	Description
sequence	Required. A sequence like a list, a tuple, a range of numbers etc.
    """

#----END-----

#----Start-----

#Python Random choices() Method
#Example
#Return a list with 14 items.
#The list should contain a randomly selection of the values from a specified list, and there should be 10 times higher possibility to select "apple" than the other two:

import random

mylist = ["Naveen", "Mehtab", "Sohail"]

print(random.choices(mylist, weights = [2, 2, 2 ], k = 14))

"""
Syntax
random.choices(sequence, weights=None, cum_weights=None, k=1)

Parameter Values
Parameter	Description
sequence	Required. A sequence like a list, a tuple, a range of numbers etc.

weights	    Optional. A list were you can weigh the possibility for each value.
            Default None
            
cum_weights	Optional. A list were you can weigh the possibility for each value, only this time the possibility is accumulated.
            Example: normal weights list: [2, 1, 1] is the same as this cum_weights list; [2, 3, 4].
            Default None
            
k	        Optional. An integer defining the length of the returned list
"""
#----END-----

#----Start-----

#----END-----