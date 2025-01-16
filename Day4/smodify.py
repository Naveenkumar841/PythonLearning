#Python - Modify Strings

#-----------Start--------------
#Python has a set of built-in methods that you can use on strings.

#Upper Case
#Example
#The upper() method returns the string in upper case:

a = "Hello World!"
print(a.upper())

#-----------END--------------


#-----------Start--------------

#Lower Case
#Example
#The lower() method returns the string in lower case:
    
b = "Hello World!"
print(b.lower())

#-----------END--------------


#-----------Start--------------

#Remove Whitespace
#Whitespace is the space before and/or after the actual text, and very often you want to remove this space.

#Example
#The strip() method removes any whitespace from the beginning or the end
c = "Hello World!"
print(c.strip())

#-----------END--------------


#-----------Start--------------
#Replace String
#Example The replace() method replaces a string with another string:
d = "Hello, World!"
print(d.replace("H", "j"))
#-----------END--------------


#-----------Start--------------

#Split String
#The split() method returns a list where the text between the specified separator becomes the list items.
#Example The split() method splits the string into substrings if it finds instances of the separator:
e = "Hello, World!"
print(e.split(","))

#Learn more about Lists in our Python Lists chapter.

#String Methods
#Learn more about String Methods with our String Methods Reference
#https://www.w3schools.com/python/python_ref_string.asp
#-----------END--------------


#-----------Start--------------

#Python - String Concatenation

#String Concatenation
#To concatenate, or combine, two strings you can use the + operator.

f = "Hello"
g = "World"
h = f + g
print(h)

i = "Hello "
j = "World"
k = i + j
print(k)


#Example
#To add a space between them, add a " ":

l = "Hello,"
m = "World"
n = l + " " + m
print(n)

#-----------END--------------

#-----------Start--------------

#Python - Format - Strings
#String Format
#As we learned in the Python Variables chapter, we cannot combine strings and numbers like this:
"""
age = 36
txt = "My name is John, I am " + age
print(txt) 
"""
#But we can combine strings and numbers by using f-strings or the format() method!

#F-Strings
#F-String was introduced in Python 3.6, and is now the preferred way of formatting strings.
#To specify a string as an f-string, simply put an f in front of the string literal, and add curly brackets {} as placeholders for variables and other operations.

#Example
#Create an f-string:
age1 = 36
txt1 = f"My name is John, I am {age1}"
print(txt1)

#Example
#Create two f-string:

Name = "Naveen kumar"
Phone = 3133254772
Age = 25
Address = "PECHS Karachi"

text = Name ,f"{Phone}",f"{Age}", Address
print(text) 


#Placeholders and Modifiers
#A placeholder can contain variables, operations, functions, and modifiers to format the value.

#Example Add a placeholder for the price variable:

Model = "Samsung S22"
Storage = "8 GB RAM" " 256GB ROM"
Battery = 3700
Screen = 6.1
Processor = "Qualcomm" 
Price = 194,999 
Pwords = "Rupees"

Mobile = Model,Storage, f"{Battery}" , f"{Screen}", Processor, f"{Price}" , Pwords
print(Mobile)




#-----------END--------------

#-----------Start--------------
#A placeholder can include a modifier to format the value.
#A modifier is included by adding a colon : followed by a legal formatting type, like .2f which means fixed point number with 2 decimals:

Laptop = "HP Intel(R) Core(TM) i5-4300U CPU @ 1.90GHz   2.50 GHz"
Aaras = "Rs."
Rs = 60000
Ram = "8GB"
ssd = "256 GB"

Lap = Laptop, Aaras,f"{Rs:.2f}",Ram,ssd
print(Lap)

#-----------END--------------

#-----------Start--------------

#A placeholder can contain Python code, like math operations:

Add = f"Addition '10+15' = {10 + 15} is that "
print(Add)

Subs = f"Subtraction '55-25' = {55 - 25} is that "
print(Subs)

multi = f"Multiplication '5*3' =  {5 * 3} is that "
print(multi)

Div = f"Division '100/4' = {100 / 4} is that "
print(Div)

Mod = f"Modulus '1%6' = {1 % 6} is that "
print(Mod)

Expon = f"Exponentiation '2**5' = { 2 ** 5} is that " #same as 2*2*2*2*2
print(Expon)

Floordiv = f"Floor division '15//2' = {15 // 2} is that"
print(Floordiv)

#the floor division // rounds the result down to the nearest whole number

#-----------END--------------

#-----------Start--------------
#Python - Escape Characters
#Escape Character
#To insert characters that are illegal in a string, use an escape character.
#An escape character is a backslash \ followed by the character you want to insert.
#An example of an illegal character is a double quote inside a string that is surrounded by double quotes:

"""
txt = "We are the so-called "Vikings" from the north."
#You will get an error if you use double quotes inside a string that are surrounded by double quotes:
"""

vik = "We are the so-called \"Vikings\" from the north."
print(vik) 

#Escape Characters
#Other escape characters used in Python:


#Code	Result	
##\'	    Single Quote	
#	    Backslash	
#\n	    New Line	
#\r	    Carriage Return	
#\t	    Tab	
#\b	    Backspace	
#\f	    Form Feed	
#\ooo	Octal value	
#\xhh	Hex value	

print("Backslash and \\'")
alright = 'It\'s alright.'
print(alright) 

#-----------
print("when you add double (backslash it will show single backslah")
Dobback = "This will insert one \\ (backslash)."
print(Dobback)

#----------- 

print("whenever you want to add a new line kindly add backslah and simple type with it n next word will be on new line")
New = "Naveen\nBalani"
print(New) 

#-----------

print("Carriage Return it is will work like new line ")
Carret = "Hello\rWorld!"
print(Carret)

#-----------

print("backslash with t it will add space like tab ")
Tab = "Hello\tWorld!"
print(Tab)  

#-----------

#This example erases one character (backspace):
backsp = "Hello  \bWorld!"
print(backsp) 

#-----------

#A backslash followed by three integers will result in a octal value:
octval = "\110\145\154\154\157"
print(octval) 

#-----------

#A backslash followed by an 'x' and a hex number represents a hex value:
hexval = "\x48\x65\x6c\x6c\x6f"
print(hexval) 

#-----------END--------------