#Python Strings

#--------Start---------

#Strings in python are surrounded by either single quotation marks, or double quotation marks.
#'hello' is the same as "hello".
#You can display a string literal with the print() function

#You can use double or single quotes:

print("Double or Single quotes")

print("Hello I am Naveen")
print("Naveen's Code ")
print('My name is "Naveen"')
print("'This is Naveen Kumar'")


#Quotes Inside Quotes
#You can use quotes inside a string, as long as they don't match the quotes surrounding the string:

#--------END----------

#--------Start---------

#Assign String to a Variable
#Assigning a string to a variable is done with the variable name followed by an equal sign and the string:

print("Assign String to a Variable")

a = "Hello"
print(a)

#--------END----------

#--------Start---------

#Multiline Strings
#You can assign a multiline string to a variable by using three quotes:

print("Multiline Strings")

b = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(b)

#Or three single quotes:
print("Or three single quotes:")

c = '''Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua.'''
print(c)

#Note: in the result, the line breaks are inserted at the same position as in the code.

#--------END----------

#--------Start----------

#Strings are Arrays
#Like many other popular programming languages, strings in Python are arrays of bytes representing unicode characters.
#However, Python does not have a character data type, a single character is simply a string with a length of 1.
#Square brackets can be used to access elements of the string.

#Example
#Get the character at position 1 (remember that the first character has the position 0):

print("Strings are Arrays")

d = "Hello, World!"
print(d[0])

#--------END----------

#--------Start----------

#Looping Through a String
#Since strings are arrays, we can loop through the characters in a string, with a for loop.

#Example = Loop through the letters in the word "Naveen":

print("Looping Through a String")
for e in "Naveen":
 print(e)
#--------END----------


#--------Start----------
#String Length
#To get the length of a string, use the len() function.
#Example The len() function returns the length of a string:
print("String Length")
f = "Balani"

print(len(f))
#--------END----------


#--------Start----------
#Check String
#To check if a certain phrase or character is present in a string, we can use the keyword in.
#Example Check if "free" is present in the following text:

Text = "The best things in life are free!"
print("free" in Text)
#--------END----------


#--------Start----------

#Use it in an if statement:
text = "this is laptop"
if "laptop" in text:
    print("The Laptop is present")

#Check if NOT
#To check if a certain phrase or character is NOT present in a string, we can use the keyword not in.
#Example Check if "Mobile" is NOT present in the following text:

txt = "Where is Mobile"
print("I have a Mobile" not in txt)

Txt = "Where is Mobile"
print("Where is Mobile" not in Txt)

#Use it in an if statement:

te_xt = "The best thigs in life are Expensive"
if "Expensive" not in te_xt:
 print("NO 'Expensive' in not present")
else:
    print("yes Expensive is available")
#--------END----------

#--------Start----------
#Python - Slicing Strings
#Slicing
#You can return a range of characters by using the slice syntax.
#Specify the start index and the end index, separated by a colon, to return a part of the string.
#Example = Get the characters from position 2 to position 5 (not included):



#--------END----------


#--------Start----------


#--------END----------


#--------Start----------


#--------END----------


#--------Start----------


#--------END----------