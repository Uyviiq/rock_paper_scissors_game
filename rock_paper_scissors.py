
import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''
paper = '''
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
'''
Scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
game = [rock, Scissors, paper ]
print("What do you choose? Type 0 for rock, 1 for scissors, 2 for paper")
user_decisions = int(input(""))
computer_decisions = random.randint(0,2)
if user_decisions == computer_decisions:
    print("you chose")
    print(game[user_decisions])
    print("computer chose")
    print(game[computer_decisions])
    print("It's a draw\n")
elif user_decisions > computer_decisions:
    print("you chose")
    print(game[user_decisions])
    print("computer chose")
    print(game[computer_decisions])
    print("you won")
elif computer_decisions > user_decisions:
    print("you chose")
    print(game[user_decisions])
    print("computer chose")
    print(game[computer_decisions])
    print("you lost")
else:
    print("you typed an invalid choice")

