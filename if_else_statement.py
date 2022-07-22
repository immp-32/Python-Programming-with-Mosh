'''
user_input = input("How is the weather of today: ")

#casefold() is used for case insensitive
if user_input.casefold() == "Hot".casefold():
    print("It's a hot day\n"
          "Drink plenty of water")

elif user_input.casefold() == "Cold".casefold():
    print("It's a cold day\n"
          "Wear warm clothes")

else:
    print("It's a lovely Day")
'''

# Exercise---------------------------------
'''
price of a house is $1M.
If buyer has good credit,
    they need to put down 10%
otherwise 
    they need to put down 20%
print the down payment
'''
price = 1000000
has_good_credit = True

if has_good_credit:
    down_payment = (0.1) * 1000000

else :
    down_payment = (0.2) * 1000000

print(f"Down Payment = ${down_payment}")