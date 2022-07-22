'''
print('hello mahesh how are you?')
print('soon you are going to be successful person')

#variables-----------------------
name ='Mahesh'
number = 10
price = 43.6
is_fine = True
char ='A'
d_number = 30766.443636

print(type(d_number))
print(type(price))

# Assigning the multiple values to the variable----------------------
x , y, z = "Orange", "Banana", "Mango"
print(x,y,z)

# Multiple variable and a single value
a=b=c ="Apple"
print(a,b,c)

# Unpack a collection(either from tuple or list)
names = ('Mahesh', 'Samrat', 'Ashok', 'Sandip')
p,q,r,s = names
print(p, q, r, s)

# Global Variable
g = 'Hello its me global variable\n'
def __myfunc():
    print(g)

print(g)
__myfunc()

# local variable

def __func2():
    l = "Hello its me local variable"
    print(l)
    print(g)
__func2()

'''
# global keyword
x = "Hey its me global variable"

def func():
    global x
    x = "Overidden"
    print(x)

func()
print(x)