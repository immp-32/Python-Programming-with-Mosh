
# # triple quotes for writing email
# course = '''
# Hey John
# This is first email to you.
#
# Thank you for your support.
# '''
# print(course)
#
# title = '   Python Course for Beginners'
# print(title.strip())

 # copy the content of one variable to another variable
# title = 'Python Course for Beginners'
# another = title[:] #copy all the content from title variable
# print(another)

#check the word in string
'''
txt = "The best thing in life are free."
print("mahesh" in txt)

if "free" in txt:
    print("yes it is present in txt")
else:
    print("no it is not present in txt")


# String Slicing
txt ="Hello, World"
print(txt[-5:-1])

# TO upper and lower case
print(txt.upper())
print(txt.lower())

# replace the string
print(txt.replace("H","M"))

# split the string
print(txt.split(","))

#concatenation
txt1 ="Hello"
txt2 ="World"
print(txt1 + " " + txt2)
'''

# find the index of the character
title ="Python for Beginners"
print(title.find('H')) # will show error cause its case sensitive
