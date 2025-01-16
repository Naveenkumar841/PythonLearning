#Python - Slicing Strings
#Slicing
#You can return a range of characters by using the slice syntax.
#Specify the start index and the end index, separated by a colon, to return a part of the string.

a = "Hello, World!"
print(a[0:8])


b = "Naveen Balani"
print(b[0:13])

#Note: The first character has index 0.

#-----------Start--------------

#Slice From the Start
#By leaving out the start index, the range will start at the first character:

c = "Start From"
print(c[:4])


#-----------END--------------

#-----------Start--------------
#Slice To the End
#By leaving out the end index, the range will go to the end:
c = "From End"
print(c[4:])

#-----------END--------------


#-----------Start--------------
#Negative Indexing
#Use negative indexes to start the slice from the end of the string:
"""
Example Get the characters:
From: "o" in "World!" (position -5)
To, but not included: "d" in "World!" (position -2):

"""

d = "Hello, World!"
print(d[-5:-2])

#-----------END--------------





