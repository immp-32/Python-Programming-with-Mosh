'''
try - test a block of code for errors
except - handle the error
else - lets you execute code when there is no error
finally - lets you execute code regardless of try and except errors
'''
'''
try:
    age = int(input("Age: "))
    print(age)

except ValueError:
    print("Invalid value..")
'''
#----------------------------------------
'''
try :
    number = int(input("Number: "))
    income = 3000
    calculate = income / number
    print(calculate)

except ZeroDivisionError:
    print("Number cannot be zero")


# raise is used to throw the exception ---------------------------------
x= -1
if x < 0:
    raise Exception("Sorry no negative number can be greater than 0")



try:
    print("hello world")

except:
    print("Sorry variable not defined.")

else:
    print("Nothing went wrong")

finally:
    print("try except is finished")
'''

x= 21
if not type(x) is int:
    raise TypeError ("Only integer is allowed")