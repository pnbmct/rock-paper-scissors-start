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
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
row1 = ["it's a draw","you lose","you win"]
row2 = ["you win","it's a draw","you lose"]
row3 = ["you lose","you win","it's a draw"]

map = [row1,row2,row3]
images = [rock,paper,scissors]

selection_human = int(input("What do you choose? 0 for Rock, 1 for Paper or 2 for Scissors."))
if selection_human >= 3 or selection_human < 0:
  print("you enter a wrong number: You lose")
else:
  selection_computer = random.randint(0,2)
  print(images[selection_human])
  print(f"computer choose: {images[selection_computer]}")
  print(map[selection_human][selection_computer])

