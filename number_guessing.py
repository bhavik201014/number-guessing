import random
num=random.randint(1,9)
chances=0
print("guess a number (between 1 and 9):")
while chances<5:
    guess=int(input("enter your guess:-"))
    if guess==num:
        print("CONGRATULATIONS,YOU WON")
        break
    elif guess<num:
        print("your number was way too high then", guess)
    else:
        print("your number is way too low than",guess)
    chances=chances+1
if not chances<5:
    print("you lose!! the you had to guess was ", num)            