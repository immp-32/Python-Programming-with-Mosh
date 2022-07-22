
class SmartPhone:
    def Music(self):
        print("Music playing..")

    def Camera(self):
        print("Click Photos..")

    def Call(self):
        print("Calling...")


class Redmi(SmartPhone):
    def poweroff_sound(self):
        print("tin tin tin tin")

class Nokia(SmartPhone):
    def poweroff_sound(self):
        print("tuuuuu tuuuu dhisss")

    def Battery(self):
        print("5000 mah")


redmi = Redmi()
redmi.Call()
redmi.poweroff_sound()
redmi.Music()
redmi.Camera()
print("\n")
nokia = Nokia()
nokia.Music()
nokia.Camera()
nokia.Call()
nokia.poweroff_sound()
nokia.Battery()
