#Python Data Types

#Built-in Data Types
#In programming, data type is an important concept.
#Variables can store data of different types, and different types can do different things.
#Python has the following data types built-in by default, in these categories:
"""
Text Type:	str
Numeric Types:	int, float, complex
Sequence Types:	list, tuple, range
Mapping Type:	dict
Set Types:	set, frozenset
Boolean Type:	bool
Binary Types:	bytes, bytearray, memoryview
None Type:	NoneType

"""

#Getting the Data Type
#You can get the data type of any object by using the type() function:


a = "Naveen Balani"
#display a:
print(a)
#display the data type of a:
print(type(a)) 

#------------

b = 6
#display b:
print(b)
#display the data type of b:
print(type(b)) 

#-----------

c = 20.5
#display c:
print(c)
#display the data type of c:
print(type(c)) 

#-----------

d = 1j
#display d:
print(d)
#display the data type of d:
print(type(d)) 

#-----------

e = ["apple", "banana", "cherry"]
#display e:
print(e)
#display the data type of e:
print(type(e))

#----------- 

f = ("apple", "banana", "cherry")
#display f:
print(f)
#display the data type of f:
print(type(f)) 

#----------- 

g= range(4)
#display g:
print(g)
#display the data type of g:
print(type(g))

#-----------  

h = {"name" : "John", "age" : 36}
#display h:
print(h)
#display the data type of h:
print(type(h))

#----------- 

i = {"apple", "banana", "cherry"}
#display i:
print(i)
#display the data type of i:
print(type(i)) 

#----------- 

j = frozenset({"apple", "banana", "cherry"})
#display j:
print(j)
#display the data type of j:
#Free the ist and make it unchangable 
print(type(j)) 

#----------- 

k = True
#display k:
print(k)
#display the data type of k:
print(type(k)) 

#----------- 

l = b"Hello"
#display l:
print(l)
#display the data type of l:
print(type(l)) 

#----------- 

m = bytearray(2)
#display m:
print(m)
#display the data type of m:
print(type(m)) 

#----------- 

n = memoryview(bytes(1))
#display n:
print(n)
#display the data type of n:
print(type(n)) 

#----------- 

o = None
#display o:
print(o)
#display the data type of o:
print(type(o)) 

#----------- 

#----------- 