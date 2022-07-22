'''
guess_count = 3
if guess_count > 3 "Sorry you failed!"
secret_number = 9
if secret_number =9 "You win!"
'''

print("Welcome to the Guessing Game: ")
guess_count = 0
secret_number = 9
guess_limit = 3
while guess_count < guess_limit:
    user_input = int(input("Guess: "))
    if user_input == secret_number:
        print("Congrates you win!..")
        break
    guess_count += 1

else:
    print("Sorry you failed!.")

