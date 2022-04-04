# Guess a number
import random

random_number = random.randint(1,10)

print("This is a guessing game. Write a number ranging from 1 to 10")


user_number = input("Write here:")

while(int(user_number) != random_number):
    print("That's wrong :( Try again")
    user_number = input("Write here: ")
    
else:
    print("You won :)")
    
