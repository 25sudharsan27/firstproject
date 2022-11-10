import random

top_range = input("Enter a number: ")
if top_range.isdigit():
    top_range=int(top_range)
    if top_range<=0:
        print("Enter a number larger than  0 next time.")
        quit()
else:
    print('Please type a number next time.')
    quit()
random_number = random.randint(0,top_range)


while True:
    guess=input("Enter your guess: ")
    if guess.isdigit():
        guess=int(guess)
    else:
        print("Please type a number next time.")
        continue

    if guess==random_number:
        print("You got it!!!")
        break
    else:
        print("You got it wrong")


