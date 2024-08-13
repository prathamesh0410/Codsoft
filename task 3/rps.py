import random

def get_computer_choice():
    return random.choice(["rock", "paper", "scissors"])

def get_user_choice():
    choice = input("Enter your choice (rock, paper, or scissors): ").lower()
    while choice not in ["rock", "paper", "scissors"]:
        print("Invalid choice! Please choose 'rock', 'paper', or 'scissors'.")
        choice = input("Enter your choice (rock, paper, or scissors): ").lower()
    return choice

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "tie"
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "scissors" and computer_choice == "paper") or \
         (user_choice == "paper" and computer_choice == "rock"):
        return "user"
    else:
        return "computer"

def display_result(user_choice, computer_choice, winner):
    print(f"\nYou chose: {user_choice}")
    print(f"Computer chose: {computer_choice}")
    if winner == "tie":
        print("It's a tie!")
    elif winner == "user":
        print("You win!")
    else:
        print("You lose!")

def play_again():
    return input("Do you want to play again? (yes/no): ").lower().startswith('y')

def main():
    user_score = 0
    computer_score = 0

    print("Welcome to Rock-Paper-Scissors!")

    while True:
        user_choice = get_user_choice()
        computer_choice = get_computer_choice()
        winner = determine_winner(user_choice, computer_choice)
        
        if winner == "user":
            user_score += 1
        elif winner == "computer":
            computer_score += 1

        display_result(user_choice, computer_choice, winner)
        print(f"Score -> You: {user_score} | Computer: {computer_score}\n")

        if not play_again():
            print("Thanks for playing! Final Score -> You: {} | Computer: {}".format(user_score, computer_score))
            break

if __name__ == "__main__":
    main()
