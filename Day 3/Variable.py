#Variables
#Variables are containers for storing data values.

#Creating Variables
#Python has no command for declaring a variable.
#A variable is created the moment you first assign a value to it

x = 5
y = "John"
print(x)
print(y)


#Variables do not need to be declared with any particular type, and can even change type after they have been set.

a = 4
a = "Sally"
print(a)


#Casting
#If you want to specify the data type of a variable, this can be done with casting.

#Get the Type
#You can get the data type of a variable with the type() function.

b = 5
c = "John"
print(type(b))
print(type(c))

#You will learn more about data types and casting later in this tutorial.

#Python Variables - Assign Multiple Values
#Many Values to Multiple Variables
#Python allows you to assign values to multiple variables in one line:

d, e, f = "Orange", "Banana", "Cherry"

print(d)
print(e)
print(f)

#Note: Make sure the number of variables matches the number of values, or else you will get an error.


myvar = "1 Naveen Balani"
MYVAR = "2 Mehtab"
Myvar = "3 Balani"
myVar = "4 Ritik"
my_var = "5 Sufyan"
myva_r = "6 Tushar"
My_var = "7 John"
#MYVAR = "8 Suneel"

print(myvar)
print(MYVAR)
print(Myvar)
print(myVar)
print(my_var)
print(myva_r)
print(My_var)
print(myvar)
#print(MYVAR)

#One Value to Multiple Variables
#And you can assign the same value to multiple variables in one line:
g = h = i = "Orange"

print(g)
print(h)
print(i)

#Unpack a Collection
#If you have a collection of values in a list, tuple etc. Python allows you to extract the values into variables. This is called unpacking.
fruits = ["apple", "banana", "cherry"]
j, k, l = fruits

print(j)
print(k)
print(l)

#Python - Output Variables
#The Python print() function is often used to output variables.
m = "Python is awesome"
print(m)

#In the print() function, you output multiple variables, separated by a comma:

n = "Python"
o = "is"
p = "awesome"
print(n, o, p)


#You can also use the + operator to output multiple variables:

q = "Python "
r = "is "
s = "awesome"
print(q + r + s)

#Notice the space character after "Python " and "is ", without them the result would be "Pythonisawesome".

