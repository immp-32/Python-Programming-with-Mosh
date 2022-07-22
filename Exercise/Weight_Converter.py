while True:
    weight = int(input("Enter your weight: "))
    weight_measure = input("(L)bs or (K)g: ")

    if weight_measure.casefold() == "L".casefold():
        total_weight = weight * 0.45
        print(f"Your weight is : {total_weight} kilogram")

    else:
        total_weight = weight / 0.45
        print(f"Your weight is : {total_weight} pounds")

    user_input = input("\nDo you want to run again\n Press 'y' for yes and 'n' for no: ")
    if user_input.casefold() == "y".casefold():
        continue
    else:
        exit()