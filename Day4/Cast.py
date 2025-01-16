#Python Casting

#Specify a Variable Type
"""
There may be times when you want to specify a type on to a variable. This can be done with casting. Python is an object-orientated language, and as such it uses classes to define data types, including its primitive types.

Casting in python is therefore done using constructor functions:

int() - constructs an integer number from an integer literal, a float literal (by removing all decimals), or a string literal (providing the string represents a whole number)
float() - constructs a float number from an integer literal, a float literal or a string literal (providing the string represents a float or an integer)
str() - constructs a string from a wide variety of data types, including strings, integer literals and float literals

"""
print("This integer")

a = int(1)
b = int(2.8)
c = int("3")
print(a)
print(b)
print(c)

#-------------
print("This Float")
d = float(1)
e = float(2.8)
f = float("3")
print(d)
print(e)
print(f)

#-------------
print("This String")

g = str(1)
h = str(2.8)
i = str("3")
print(g)
print(h)
print(i)

