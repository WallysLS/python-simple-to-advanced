# A very simple Rock Paper Scissors game

import random

print("Hi, there! This is a Rock Paper Scissor game")

computer_role = random.choice(["rock","paper","scissors"])
user_role = input("Choose a role: ").lower()

