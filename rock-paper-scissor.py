import random

print("This is a Rock, Paper, Scissor game! How good are you in this game? ")
print("In order to play, write rock, paper or scissors")

computer_role = random.choice(["rock","paper","scissor"])

user_role = input("Write here: ")
user_role = user_role.lower().replace(" ","")







