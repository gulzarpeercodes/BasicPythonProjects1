rock = ('''    
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
''')

paper = ('''    
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
''')

scissors = ('''    
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
''')

import random
print("Welcome to game of Rock, Paper and Scissors!")

rock_paper_scissors = [rock, paper, scissors]
random_rock_paper_scissors = random.choice(rock_paper_scissors)
user_choice = int(input("What do you choose? Type 1 for Rock, 2 for Paper or 3 for Scissors.\n"))

if random_rock_paper_scissors == rock and user_choice == 1:
    print(f"You chose:\n{rock}")
    print(f"Computer chose:\n{rock}")
    print("Draw!")
elif random_rock_paper_scissors == paper and user_choice == 2:
    print(f"You chose:\n{paper}")
    print(f"Computer chose:\n{paper}")
    print("Draw!")
elif random_rock_paper_scissors == scissors and user_choice == 3:
    print(f"You chose:\n{scissors}")
    print(f"Computer chose:\n{scissors}")
    print("Draw!")

elif random_rock_paper_scissors == rock and user_choice == 2:
    print(f"You chose:\n{paper}")
    print(f"Computer chose:\n{rock}")
    print("You Win!")
elif random_rock_paper_scissors == rock and user_choice == 3:
    print(f"You chose:\n{scissors}")
    print(f"Computer chose:\n{rock}")
    print("You Loose!")

elif random_rock_paper_scissors == paper and user_choice == 1:
    print(f"You chose:\n{rock}")
    print(f"Computer chose:\n{paper}")
    print("You Loose!")
elif random_rock_paper_scissors == paper and user_choice == 3:
    print(f"You chose:\n{scissors}")
    print(f"Computer chose:\n{paper}")
    print("You Win!")

elif random_rock_paper_scissors == scissors and user_choice == 1:
    print(f"You chose:\n{rock}")
    print(f"Computer chose:\n{scissors}")
    print("You Win!")
elif random_rock_paper_scissors == scissors and user_choice == 2:
    print(f"You chose:\n{paper}")
    print(f"Computer chose:\n{scissors}")
    print("You Loose!")
else:
    print("You chose a wrong number!!")
