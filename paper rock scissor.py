import random

#The pictures aren't mine, i just inverted them
rock_p = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""
rock_a = """
   _______
  (____   '---
 (_____)
 (_____)
  (____)
   (___)__.---
"""
paper_p = """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""
paper_a = """
      _______
 ____(____   '---
(______
(_______
 (_______
  (__________.---
"""
scissors_p = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""
scissors_a = """
       _______
  ____(____   '---
 (______
(__________
      (____)
       (___)__.---
"""
def player_sign():
    if player == 1:
        print(rock_p)
    elif player == 2:
        print(paper_p)
    elif player == 3:
        print(scissors_p)
def oponent_sign():
    if oponent == 1:
        print(rock_a)
    elif oponent == 2:
        print(paper_a)
    elif oponent == 3:
        print(scissors_a)

oponent = random.choice(['paper','scissors','rock'])
if oponent == 'rock':
 oponent = 1
elif oponent == 'paper':
 oponent = 2
elif oponent == 'scissors':
 oponent = 3
while True:
 while True:
  player = input(str('Choose your hand by writhing paper, scissors or rock:'))
  if player == 'rock':
     player = 1
     break
  elif player == 'paper':
    player = 2
    break
  elif player == 'scissors':
    player = 3
    break
  else:
    print('wrong input')

 player_sign()
 oponent_sign()
 if player == oponent:
    print('It\'s a draw!')
 elif player + oponent == 3:
   print('The winner is PAPER!!')
 elif player + oponent == 4 and not player == oponent:
   print('The winner is ROCK!!')
 elif player + oponent == 5:
   print('The winner is SCISSORS!!')