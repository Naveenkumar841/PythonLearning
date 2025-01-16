import random

#Python Numbers
#Python Numbers
#There are three numeric types in Python:
"""
int
float
complex

Variables of numeric types are created when you assign a value to them:

"""

a = 1
b = 2.8
c = 1j

print(type(a),a)
print(type(b),b)
print(type(c),c)

#To verify the type of any object in Python, use the type() function:

#-------------------

#Int
#Int, or integer, is a whole number, positive or negative, without decimals, of unlimited length.

d = 1
e = 35656222554887711
f = -3255522

print(type(d),d)
print(type(e),e)
print(type(f),f)


#-------------------

#Float
#Float, or "floating point number" is a number, positive or negative, containing one or more decimals.

#float
g = 1.10
h = 1.0
i = -35.59

print(type(g),g)
print(type(h),h)
print(type(i),i)
    
#-------------------
#Float can also be scientific numbers with an "e" to indicate the power of 10.

j = 35e3
k = 12E4
l = -87.7e100

print(type(j),j)
print(type(k),k)
print(type(l),l)

#-------------------

#Complex
#Complex numbers are written with a "j" as the imaginary part:

m = 3+5j
n = 5j
o = -5j

print(type(m),m)
print(type(n),n)
print(type(o),o)

#-------------------

#Type Conversion
#You can convert from one type to another with the int(), float(), and complex() methods:
    
#Example
#Convert from one type to another:

#convert from int to float:
p = float(1)

#convert from float to int:
q = int(2.8)

#convert from int to complex:
r = complex(1)

#convert from complex to int:

#s = int(1j)

print(p)
print(q)
print(r)
#print(s)

print(type(p),p)
print(type(q),q)
print(type(r),r)
#print(type(s),s)

#Note: You cannot convert complex numbers into another number type.
    
#-------------------

#Random Number
#Python does not have a random() function to make a random number, but Python has a built-in module called random that can be used to make random numbers:

#Example
#Import the random module, and display a random number between 1 and 9:

print(random.randrange(1,10))
#-------------------

#-------------------