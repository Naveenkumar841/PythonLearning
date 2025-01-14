"""
x = str(3)
y = int(3)
z = float(3)

print(x,y,z)
"""
#Data Types
"""
a = "Hello World"	#str	
b = 20	#int	
c = 20.5	#float	
d = 1j	#complex	
e = ["apple", "banana", "cherry"]	#list	
f = ("apple", "banana", "cherry")	#tuple	
g = range(6)	#range	
h = {"name" : "John", "age" : 36}	#dict	
i = {"apple", "banana", "cherry"}	#set	
j = frozenset({"apple", "banana", "cherry"})	#frozenset	
k = True	#bool	
l = b"Hello"	#bytes	
m = bytearray(5)	#bytearray	
n = memoryview(bytes(5))	#memoryview	
o = None	#NoneType

print(type(a)) 
print(type(b))
print(type(c)) 
print(type(d))
print(type(e)) 
print(type(f))

#another pattern
print("Another Pattern")
print(type(g),type(h),type(i),type(j),type(k)) 
print(type(h))
print(type(i)) 
print(type(j))
print(type(k)) 
print(type(l))
print(type(m)) 
print(type(n))
print(type(o))
"""

#Unpack Collection 

"""
Pakistan = ["Sindh", "Punjab", "Balochistan", "KPK"]

a,b,c,d = Pakistan
print(a,b,c,d)
"""

#Global Varraibles 

"""
b = "Superb"

def myfunc():
    print("Python is " + b)

myfunc()
"""
#hasdbj

#A variable inside a function, with the same name as the global variable
"""
firstname = "Naveen"

def myfunc():
    lastname = " Kumar"
    print("My Name is " + firstname + lastname)

myfunc()
print(firstname + " Balani")
"""

#The global Keyword

#----------
"""
def myfunc():
    global c   
    c = "Fantastic"

myfunc()
print("Python is " + c)
   """ 
 
#-------------Quotes Inside Quotes
"""  
a = ' "Kumar" ' 
print(a)
"""

#------------Strings are Arrays
#----Get the character at position 1 (remember that the first character has the position 0):
"""
a = "Hello, World!"
print(a[0],(a[1]),(a[2]),(a[3]),(a[4])) 
"""

#----------Looping Through a String


"""
for x in "Naveen":
    print(x)
    
"""
#Since strings are arrays, we can loop through the characters in a string, with a for loop.

#Python For Loops

"""
Fruits = ["Mango", "Apple", "Banana"]

for a in Fruits:
    print(a)
    
"""
#A for loop is used for iterating over a sequence (that is either a list, a tuple, a dictionary, a set, or a string).
#This is less like the for keyword in other programming languages, and works more like an iterator method as found in other object-orientated programming languages. 
#With the for loop we can execute a set of statements, once for each item in a list, tuple, set etc.


#-----------String Length
"""
h= "Hello World"
print(len(h))
"""
#To get the length of a string, use the len() function.


#Check String


"""
txt = "The best things in life are Free!"
print("free" in txt)
#-----

txt = "The best things in life are free!"
print("free" in txt)
"""
##Use it in an if statement:
"""
Txt = "The best things in life are free!"
if "free!" in Txt:
    print("Yes " 'Free, is Present.')
#-------

Txt = "The best things in life are free!"
if "free!" in Txt:
    print("Yes " 'Free, is Present.')
"""
#To check if a certain phrase or character is present in a string, we can use the keyword in.

#--Check if NOT
"""
Txt = "The best things in life are free!"
print("Expensive " not in Txt)

#if Statement
Txt = "The best things in life are free!"
if "Expensive" not in Txt:
 print("No 'Expensive 'is NOT Present")
 """
#----------

#-----------Python - Slicing Strings
#Slicing
#You can return a range of characters by using the slice syntax.
#Specify the start index and the end index, separated by a colon, to return a part of the string.
"""
b = "Hello,World!"
print(b[2:5])

#Slice From the Start
b = "Hello,World!"
print(b[4])
#Slice From the Start
b = "Hello,World!"
print(b[3:])
"""

#Negative Indexing
#Use negative indexes to start the slice from the end of the string:
#Example
#Get the characters:
#From: "o" in "World!" (position -5)
#To, but not included: "d" in "World!" (position -2):
"""
b = "Hello,World!"
print(b[-7:-1])
"""

#Python - Modify Strings
"""
a= "Hello, World!"
print(a.upper())
"""

#Remove Whitespace
#Whitespace is the space before and/or after the actual text, and very often you want to remove this space.
#Example
#The strip() method removes any whitespace from the beginning or the end:

"""
a= "Hello, World!"
print(a.strip())
"""
"""
a= "Hello, World!"
print(a.replace("H","K"))
"""

#Split String
#The split() method returns a list where the text between the specified separator becomes the list items.
#Example
#The split() method splits the string into substrings if it finds instances of the separator:
"""
a = "Hello, World!"
print(a.split(","))
"""
#Python - String Concatenation

#String Concatenation
#To concatenate, or combine, two strings you can use the + operator.
#Merge variable a with variable b into variable c:
"""
a = "Naveen"
b = "Balani"
c = a + b
print(c)
"""

#Example
#To add a space between them, add a " ":
"""a = "Naveen"
b = "Balani"
c = a + " " + b
print(c)
"""

#Python - Format - Strings
#F-Strings
#F-String was introduced in Python 3.6, and is now the preferred way of formatting strings.
#To specify a string as an f-string, simply put an f in front of the string literal, and add curly brackets {} as placeholders for variables and other operations.

"""
age = 25
txt = f"My name is Naveen, I am  {age}"
print(txt)
"""
#Placeholders and Modifiers
#A placeholder can contain variables, operations, functions, and modifiers to format the value.
#Example
#Add a placeholder for the price variable:
"""
price = 69
txt = f"The Price is {price} dollars"
print(txt)
"""
#A placeholder can include a modifier to format the value.
#A modifier is included by adding a colon : followed by a legal formatting type, like .2f which means fixed point number with 2 decimals:
#Display the price with 2 decimals:

"""
price = 69
txt = f"The Price is {price:.2f} dollars"
print(txt)
"""

"""
txt = f"The Price is {20 * 59} Dollars"
print(txt)
"""

#Python - Escape Characters
#Escape Character
#To insert characters that are illegal in a string, use an escape character.
#An escape character is a backslash \ followed by the character you want to insert.
#An example of an illegal character is a double quote inside a string that is surrounded by double quotes:


#------------------

#Boolean Values
#In programming you often need to know if an expression is True or False.
#You can evaluate any expression in Python, and get one of two answers, True or False.
#When you compare two values, the expression is evaluated and Python returns the Boolean answer:
"""
print(10>9)
print(10==9)
print(10<9)
"""

#Example
#rint a message based on whether the condition is True or False:
"""
a = 223
b = 544

if b > a: 
 print("B is Greater than A")
else: 
 print("B is not greater than A")
 """
"""
print(bool("hello"))
print(bool("15"))
"""

#Some Values are False
#In fact, there are not many values that evaluate to False, except empty values, such as (), [], {}, "", the number 0, and the value None. And of course the value False evaluates to False.

#One more value, or object in this case, evaluates to False, and that is if you have an object that is made from a class with a __len__ function that returns 0 or False:
"""
class myclass():
    def __len__(self):
        return 65 
myobj = myclass ()
print(bool(myobj))
"""