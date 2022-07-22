# Q.N 1 Create a Vehicle class with max_speed and mileage instance attributes.
'''
class Vehicle:
    def __init__(self, max_speed, mileage):
        # Instance variable
        self.max_speed = max_speed
        self.mileage = mileage
        print(f"Total max_speed is {max_speed} and mileage is {mileage}")

Scorpio = Vehicle(120, 45)
print(Scorpio.max_speed, Scorpio.mileage)
Mercedes = Vehicle(220, 40)


# Exercise 2: Create a Vehicle class without any variables and methods
class Vehicle:
    pass
'''

