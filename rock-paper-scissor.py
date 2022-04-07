import random

print("This is a Rock, Paper, Scissor game! How good are you in this game? ")
print("In order to play, write rock, paper or scissors")

computer_role = random.choice(["rock","paper","scissors"])

user_role = input("Write here: ")
user_role = user_role.lower().replace(" ","")

if(user_role != "rock" and user_role != "paper" and user_role != "scissors"):
    print("I'm sorry, you typed something wrong. The input must be rock, paper or scissors")


while(computer_role == "rock"):
    if(user_role == "rock"):
        print("The computer also chosed rock, so it's even. Try again!")
        user_role = input("Write here: ")
    if(user_role == "paper"):
        print()





