"""
Logic of game:
A-
Rock vs Rock = tie
Rock vs Paper = Paper
Rock vs Scissor = Rock

B-
Paper vs Paper = Tie
Paper vs rock = paper
Paper vs Scisoor = Scissor

C-
Scissor vs Scissor = Tie
Scissor vs rock = rock
Scissor vs paper = Scissor
"""

import random
item_list = ["Rock", "Paper", "Scissor"]

user_choice = input("Enter you move: Rock, Paper, Scissor = ")
comp_choice = random.choice(item_list)

print(f"User choice = {user_choice}, Computer choice = {comp_choice} ")

if user_choice == comp_choice:
    print("Both chooses same: Match tie")

elif user_choice == "Rock":
    if comp_choice == "Paper":
        print("Paper covers Rock = Computer Win")
    else:
        print("Rock smashes Scissor = You Win")

elif user_choice == "Paper":
    if comp_choice == "Scissor":
        print("Scissor cuts Paper = Computer Win")
    else:
        print("Paper covers Rock = You Win")

elif user_choice == "Scissor":
    if comp_choice == "Paper":
        print("Scissor cuts Paper = You Win")
    else:
        print("Rock smashes Scissor = Computer Win")