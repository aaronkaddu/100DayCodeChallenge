# Rock Paper Scissors ASCII Art
import random

print("!!! WELCOME TO THE GAME !!!")

user = int(input("What do you choose?  Type 0 for Rock, 1 for Paper or 2 for Scissors"))
# Rock
if user == 0:

    print("""
        _______
    ---'   ____)
          (_____)
          (_____)
          (____)
    ---.__(___)
    """)

elif user == 1:
    # Paper
    print("""
         _______
    ---'    ____)____
               ______)
              _______)
             _______)
    ---.__________)
    """)
elif user == 2:
    # Scissors
    print("""
        _______
    ---'   ____)____
              ______)
           __________)
          (____)
    ---.__(___)
    """)
else:
    print("Invalid Entry, Try Again")


computer_player = random.randint(0,2)
print("Computer Chose")
# Rock
if computer_player == 0:
    print("""
        _______
    ---'   ____)
          (_____)
          (_____)
          (____)
    ---.__(___)
    """)

elif computer_player == 1:
    # Paper
    print("""
         _______
    ---'    ____)____
               ______)
              _______)
             _______)
    ---.__________)
    """)
elif computer_player == 2:
    # Scissors
    print("""
        _______
    ---'   ____)____
              ______)
           __________)
          (____)
    ---.__(___)
    """)
else:
    print("Invalid Entry, Try Again")


if user == 0 and computer_player == 2:
    print("You Win")
elif user == 2 and computer_player == 1:
    print("You Win")
elif user == 1 and computer_player == 0:
    print("You Win")
elif user == computer_player:
    print("That was a Draw")
else:
    print("Computer Wins")


