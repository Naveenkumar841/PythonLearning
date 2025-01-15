#Python - Global Variables
#Global Variables
#Variables that are created outside of a function (as in all of the examples in the previous pages) are known as global variables.
#Global variables can be used by everyone, both inside of functions and outside.

#Create a variable outside of a function, and use it inside the function
a = "awesome"

def myfunc():
  print("Python is " + a)

myfunc()

#If you create a variable with the same name inside a function, this variable will be local, and can only be used inside the function. The global variable with the same name will remain as it was, global and with the original value.
c = "Super"

def myfunc2():
  print("Python is " + c)


d = "Good"

def myfunc3():
    
    
    print("Python is "+ d)
    myfunc2()
myfunc3()

#-----------

e = "Excellent"

def myfunc():
  f = "fantastic"
  print("Python is " + f)

myfunc()

print("Python is " + e)
