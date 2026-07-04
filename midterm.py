print("HELLO PLAYER!")

# imports

import time
import random

player = input("What is your name?")

print("Welcome", player, "to this game of life and death!") 
print("This is a game of rock, paper, and scissors which will decide if you win the lottery of 1 million dollars.")
time.sleep(2)
print()

# Round 1

valid_choice = False

# Checking Validity of input
while not valid_choice:
  player_choice = input("You are paired up against a random opponent. The game is best of 3 rounds. It is your turn. Please type in rock, paper, or scissors.")
  if player_choice.capitalize() != "Rock" and player_choice.capitalize(
  ) != "Paper" and player_choice.capitalize() != "Scissors":
    type("\n")
    type("Not a valid choice. Type either Rock, Paper or Scissors!\n\n")
  else:
    valid_choice = True


print("For round 1, you chose", player_choice)


print("Your opponent chose...")
time.sleep(3)

if player_choice == "rock":
    print("paper. You lost the first round.")
elif player_choice == "scissors":
    print("rock. You lost the first round.")
else:
    print("scissors. You lost the first round.")

print()

# Round 2

valid_choice = False

# Checking for validity of input
while not valid_choice:
  player_choice2 = input("This is the second round. It is your turn. Please type in rock, paper, or scissors.")
  if player_choice.capitalize() != "Rock" and player_choice.capitalize(
  ) != "Paper" and player_choice.capitalize() != "Scissors":
    type("\n")
    type("Not a valid choice. Type either Rock, Paper or Scissors!\n\n")
  else:
    valid_choice = True

print("For round 2, you chose", player_choice2)

print("Your opponent chose...")
time.sleep(3)

if player_choice2 == "rock":
    print("paper. You lost the second round.")
elif player_choice2 == "scissors":
    print("rock. You lost the second round.")
else:
    print("scissors. You lost the second round.")

print()
print("You have sadly lost your chance of winning the lottery because your opponent beat you in a best of three game.")
print("Better luck next time!")

print()
print("THE END!")
print("THE END!")
print("THE END!")
