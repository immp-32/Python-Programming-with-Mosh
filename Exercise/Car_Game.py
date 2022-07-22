started = False  #not started
while True:
    user_input = input(">")
    if user_input.casefold() == "help".casefold():
        print("start - to start the car\n"
              "stop - to stop the car\n"
              "quit - to exit\n")

    elif user_input.casefold() == "start".casefold():
        if started:   # if already started
            print("Car is already started..")
        else:
            started = True    # if not started
            print("Car started... ready to go!")

    elif user_input.casefold() == "stop".casefold():
        if not started:   # means it is stopped
            print("Car is already stopped..")

        else:
           started = False
           print("Car Stopped!")

    elif user_input.casefold() == "quit".casefold():
        break

    else:
        print("Sorry I don't understand that..")

