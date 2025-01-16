#Python - String Methods
#String Methods
#Python has a set of built-in methods that you can use on strings.

#Note: All string methods return new values. They do not change the original string.

#Method	Description
#capitalize()	Converts the first character to upper case
#casefold()	Converts string into lower case
#center()	Returns a centered string
#count()	Returns the number of times a specified value occurs in a string
#encode()	Returns an encoded version of the string
#endswith()	Returns true if the string ends with the specified value
#expandtabs()	Sets the tab size of the string
#find()	Searches the string for a specified value and returns the position of where it was found
#format()	Formats specified values in a string
#format_map()	Formats specified values in a string
#index()	Searches the string for a specified value and returns the position of where it was found
#isalnum()	Returns True if all characters in the string are alphanumeric
#isalpha()	Returns True if all characters in the string are in the alphabet
#isascii()	Returns True if all characters in the string are ascii characters
#isdecimal()	Returns True if all characters in the string are decimals
#isdigit()	Returns True if all characters in the string are digits
#isidentifier()	Returns True if the string is an identifier
#islower()	Returns True if all characters in the string are lower case
#isnumeric()	Returns True if all characters in the string are numeric
#isprintable()	Returns True if all characters in the string are printable
#isspace()	Returns True if all characters in the string are whitespaces
#istitle()	Returns True if the string follows the rules of a title
#isupper()	Returns True if all characters in the string are upper case
#join()	Joins the elements of an iterable to the end of the string
#ljust()	Returns a left justified version of the string
#lower()	Converts a string into lower case
#lstrip()	Returns a left trim version of the string
#maketrans()	Returns a translation table to be used in translations
#partition()	Returns a tuple where the string is parted into three parts
#replace()	Returns a string where a specified value is replaced with a specified value
#rfind()	Searches the string for a specified value and returns the last position of where it was found
#rindex()	Searches the string for a specified value and returns the last position of where it was found
#rjust()	Returns a right justified version of the string
#rpartition()	Returns a tuple where the string is parted into three parts
#rsplit()	Splits the string at the specified separator, and returns a list
#rstrip()	Returns a right trim version of the string
#split()	Splits the string at the specified separator, and returns a list
#splitlines()	Splits the string at line breaks and returns a list
#startswith()	Returns true if the string starts with the specified value
#strip()	Returns a trimmed version of the string
#swapcase()	Swaps cases, lower case becomes upper case and vice versa
#title()	Converts the first character of each word to upper case
#translate()	Returns a translated string
#upper()	Converts a string into upper case
#zfill()	Fills the string with a specified number of 0 values at the beginning

#------------------

#Python String capitalize() Method
#Example Upper case the first letter in this sentence:

Capt = "my name is naveen"

a = Capt.capitalize()
print(a)

#Definition and Usage
#The capitalize() method returns a string where the first character is upper case, and the rest is lower case.
"""
Syntax
string.capitalize()

Parameter Values
No parameters

"""

#More Examples 
#Example The first character is converted to upper case, and the rest are converted to lower case:

Capt1 = "python is best"
b = Capt1.capitalize()
print(b)

#Example See what happens if the first character is a number:
Capt2 = "36 is my age."

c = Capt2.capitalize()

print (c)

#------------------------------------------------------

#Python String casefold() Method
#Definition and Usage
#The casefold() method returns a string where all the characters are lower case.
#This method is similar to the lower() method, but the casefold() method is stronger, more aggressive, meaning that it will convert more characters into lower case, and will find more matches when comparing two strings and both are converted using the casefold() method.

casefol = "Hello, And Welcome To My World!"

d = casefol.casefold()

print(d)

#Syntax
#string.casefold()

#Parameter Values
#No parameters


#-------------------------------------------

#Python String center() Method
#Example Print the word "banana", taking up the space of 20 characters, with "banana" in the middle:

Cent = "banana"

e = Cent.center(100)

print(e)

#Definition and Usage
#The center() method will center align the string, using a specified character (space is default) as the fill character.
#Syntax
#string.center(length, character)


#Parameter	Description
#length  	Required. The length of the returned string
#character	Optional. The character to fill the missing space on each side. Default is " " (space)


#More Examples
#Example
#Using the letter "O" as the padding character:

Cent0 = "banana"

f = Cent0.center(20, "O")

print(f)