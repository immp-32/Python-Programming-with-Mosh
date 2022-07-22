# Class------------------------------------------
'''
class Point:
    def draw(self):
        print("Draw")

    def move(self):
        print("Move")


point = Point()
point.x =10
print(point.x)
point.draw()


# Constructor ---------------------------------
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def draw(self):
        print("Draw")

    def move(self):
        print("move")


point = Point(10,20)
point.draw()
print(point.x)
print(point.y)
'''
# Exercise--------------------------------------
'''
Create a class named person with name attribute and talk method
'''
class Person:
    def __init__(self, name):
        self.name = name

    def talk(self):
        print(f"Hey it's me {self.name} talking this side. ")

person = Person("Mahesh")
person.talk()