import random

SLOTS = ["R", "G", "B"]
TRIES = 3
SLOT_LENGTH = 3

def create_acc():
    username = input("Enter your username: ")
    
    while True:
        amount = input("What would you like to deposit? $")
        if amount.isdigit():
            amount = float(amount)  # Convert amount to float for monetary value
            if amount > 0:
                return amount, username
            else:
                print("Amount must be greater than zero.")
        else:
            print("Please enter a valid amount.")

def gen_code():
    code = random.choices(SLOTS, k=SLOT_LENGTH)  # generate a random code
    return code

def guess_code():
    while True:
        guess = input("Guess (3 colors separated by space): ").upper().split()

        if len(guess) != SLOT_LENGTH:
            print(f"You must guess {SLOT_LENGTH} colors.")
            continue

        if all(color in SLOTS for color in guess):
            return guess  # Return the valid guess
        else:
            print("Invalid colors found. Please use R, G, or B.")

def check_code(guess, real_code):
    correct_pos = sum(g == r for g, r in zip(guess, real_code))  # Count correct positions
    incorrect_pos = sum(min(guess.count(c), real_code.count(c)) for c in SLOTS) - correct_pos  # Count colors in wrong positions
    return correct_pos, incorrect_pos

def game():
    amount, username = create_acc()  # Create account and get amount and username
    print(f"Welcome to Alex's game, {username}! You have ${amount:.2f} to play with and {TRIES} tries to guess the code...")
    print("The valid colors are:", *SLOTS)

    while True:
        code = gen_code()
        for attempts in range(1, TRIES + 1):
            guess = guess_code()
            correct_pos, incorrect_pos = check_code(guess, code)

            print(f"Attempt {attempts}: Correct position: {correct_pos} | Incorrect positions: {incorrect_pos}")

            if correct_pos == SLOT_LENGTH:
                print(f"You guessed the code in {attempts} tries!")
                break
        else:
            print(f"You ran out of tries, the code was: {''.join(code)}")
        
        play_again = input("Do you want to play again? (yes/no): ").strip().lower()
        if play_again != 'yes':
            print(f"Thank you for playing! Your final amount is ${amount:.2f}.")
            break

if __name__ == "__main__":  # Corrected the name check
    game()