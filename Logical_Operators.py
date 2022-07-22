
'''
If the applicants has the high income and good credit
is eligible for the loan
'''
while True:
    income = int(input("Enter your Income: "))
    credit = int(input("Enter your credit amounts : "))

    if income >= 50000 and credit >= 20000:
        print("Congrates You are eligible for the loan..")

    else:
        print("Sorry you are not eligible for the loan...")

    user_input = input("\nDo you want to run again\n Press 'Y' for yes and 'N' for no: ")
    if user_input == "Y":
        continue
    else:
        exit()