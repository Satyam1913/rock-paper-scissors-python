import random
import os

# ANSI color codes
GREEN = '\033[92m'
RED = '\033[91m'
YELLOW = '\033[93m'
CYAN = '\033[96m'
RESET = '\033[0m'

# Emojis
EMOJIS = {
    "rock": "🪨",
    "paper": "📄",
    "scissors": "✂️"
}

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def get_user_choice():
    print(CYAN + "\nChoose your weapon: Rock 🪨, Paper 📄, or Scissors ✂️" + RESET)
    user_input = input("Your choice: ").lower()
    if user_input not in ["rock", "paper", "scissors"]:
        print(RED + "Invalid choice. Try again." + RESET)
        return get_user_choice()
    return user_input

def get_computer_choice():
    return random.choice(["rock", "paper", "scissors"])

def determine_winner(user, computer):
    if user == computer:
        return "draw"
    elif (user == "rock" and computer == "scissors") or \
         (user == "paper" and computer == "rock") or \
         (user == "scissors" and computer == "paper"):
        return "win"
    else:
        return "lose"

def play_game():
    clear_screen()
    print(YELLOW + "🎮 Welcome to Rock-Paper-Scissors Game!" + RESET)

    user_score = 0
    comp_score = 0
    round_num = 1

    while True:
        print(f"\n---------- ROUND {round_num} ----------")
        user_choice = get_user_choice()
        computer_choice = get_computer_choice()

        print(f"\nYou chose: {EMOJIS[user_choice]} {user_choice}")
        print(f"Computer chose: {EMOJIS[computer_choice]} {computer_choice}")

        result = determine_winner(user_choice, computer_choice)
        if result == "draw":
            print(YELLOW + "\nIt's a draw! 🤝" + RESET)
        elif result == "win":
            print(GREEN + "\nYou win this round! 🎉" + RESET)
            user_score += 1
        else:
            print(RED + "\nYou lose this round! 😢" + RESET)
            comp_score += 1

        print(f"\nScoreboard: You {user_score} - {comp_score} Computer")

        again = input("\nDo you want to play another round? (yes/no): ").lower()
        if again != "yes":
            print("\nFinal Score:")
            print(f"You: {user_score} | Computer: {comp_score}")
            if user_score > comp_score:
                print(GREEN + "🏆 You win the game!" + RESET)
            elif user_score < comp_score:
                print(RED + "💔 You lose the game!" + RESET)
            else:
                print(YELLOW + "🤝 It's a tie!" + RESET)
            print(CYAN + "\nThanks for playing! 👋\n" + RESET)
            break
        round_num += 1

# Start the game
play_game()
    
