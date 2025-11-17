import random

# list of possible choices
choices = ["rock", "paper", "scissors"]

print("🎮 Rock Paper Scissors Game 🎮")
print("-------------------------------")

while True:
    user_choice = input("Enter rock, paper, or scissors (or 'q' to quit): ").lower()

    if user_choice == 'q':
        print("Thanks for playing! 👋")
        break

    if user_choice not in choices:
        print("Invalid choice. Try again.\n")
        continue

    computer_choice = random.choice(choices)

    print(f"\nYou chose: {user_choice}")
    print(f"Computer chose: {computer_choice}")

    # decide winner
    if user_choice == computer_choice:
        print("It's a draw! 😐\n")
    elif user_choice == "rock" and computer_choice == "scissors":
        print("You win! 🎉\n")
    elif user_choice == "paper" and computer_choice == "rock":
        print("You win! 🎉\n")
    elif user_choice == "scissors" and computer_choice == "paper":
        print("You win! 🎉\n")
    else:
        print("Computer wins! 💻\n")
