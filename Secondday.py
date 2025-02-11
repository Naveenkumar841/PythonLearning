#Python Booleans

#Booleans represent one of two values: True or False.
#Boolean Values
#In programming you often need to know if an expression is True or False.
#You can evaluate any expression in Python, and get one of two answers, True or False.
#When you compare two values, the expression is evaluated and Python returns the Boolean answer:
"""
print(15 > 9)
print(15 == 16)
print(3 < 9 )

"""
#When you run a condition in an if statement, Python returns True or False:

#Example
#Print a message based on whether the condition is True or False:

"""
a = 203
b = 55

if b > a:
    print("B is greater than A")
else:print("B is not greater than A ")
"""

#Evaluate Values and Variables
#The bool() function allows you to evaluate any value, and give you True or False in return,
"""
print(bool("hello"))
print(bool(123))

"""
#Most Values are True
#Almost any value is evaluated to True if it has some sort of content.
#Any string is True, except empty strings.
#Any number is True, except 0.
#Any list, tuple, set, and dictionary are True, except empty ones.

"""
print(bool("Abc"))
print(bool(123))
print(bool(["Apple" , "Mango" , "Banana"]))
"""
#Some Values are False
#In fact, there are not many values that evaluate to False, except empty values, such as (), [], {}, "", the number 0, and the value None. And of course the value False evaluates to False.
"""
print(bool(False))
print(bool(0))
print(bool(""))
print(bool (None))
print(bool(()))
print(bool([]))
print(bool({}))
"""
#One more value, or object in this case, evaluates to False, and that is if you have an object that is made from a class with a __len__ function that returns 0 or False:

"""
class  myclass():
    def __len__(self):
        return 0
    
myobj = myclass()
print(bool(myobj))

#----------------

class  myclass():
    def __len__(self):
        return 0
    
myobj = myclass()
print(bool(myobj))

"""

#Functions can Return a Boolean
#You can create functions that returns a Boolean Value:

"""
def myFunction() :
    return True
print(bool(myFunction))
"""
#You can execute code based on the Boolean answer of a function:

"""
def myFunction() :
    return True
if myFunction():
    print("Yes")
else: 
    print("No")

#----------
def myFunction() :
    return False
if myFunction():
    print("Yes")
else: 
    print("No")
   """ 
#Python also has many built-in functions that return a boolean value, like the isinstance() function, which can be used to determine if an object is of a certain data type:

"""
x= 200
print(isinstance(x,int))

x= 200
print(isinstance(x,str))

x = True
print(isinstance(x, bool))
"""
