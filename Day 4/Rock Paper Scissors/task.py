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

assets = {
    "ROCK": rock,
    "PAPER": paper,
    "SCISSORS": scissors
}

print("Welcome to Rock, Paper, Scissors!")
user_choice = input("What do you choose? ROCK, PAPER or SCISSORS: ").upper()
if user_choice not in assets:
    print("Invalid choice. You lose!")
else:
    print("Your choice:")
    print(assets[user_choice])

    computer_choice = random.choice(list(assets.keys()))
    print(f"Your opponent's choice:")
    print(assets[computer_choice])

    if user_choice == computer_choice:
        print("It's a draw!")
    elif user_choice == "ROCK" and computer_choice == "SCISSORS":
        print("You win!")
    elif user_choice == "PAPER" and computer_choice == "ROCK":
        print("You win!")
    elif user_choice == "SCISSORS" and computer_choice == "PAPER":
        print("You win!")
    else:
        print("You lose!")

