import random

print("What is your name?")
name= input("Name: ")
print("Hey, Welcome to my guessing game. I have one number in my head that I want you to guess. You have as many chances as you want to want to guess.")
print("The number that is in my head is between 2 and 245")
total_guesses=0
number=random.randrange(2,246)
print("Now you able to start guessing")
while total_guesses<=9:
    guess=int(input("Guess: "))
    total_guesses=total_guesses +1
    if guess>number:
        print("Your guess is too high")
    if guess<number:
        print("Your guess is too low")
    elif guess==number:
        print("Woo Hoo, You have figured out my number" )
        total_guesses=9
        break
    if total_guesses==9:
        print("Unfortunately, You have exceeded the total amount of guesses, please try again!")
        break

    
        
