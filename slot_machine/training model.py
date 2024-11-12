import random

SLOTS = ["R","G","B"]
TRIES = 3
SLOT_LENGTH = 3

def create_acc():
    username = input("Enter you username: ")
    
    while True:
        amount = input("What would you like to deposit? $")
        if amount.isdigit():
            if amount>0:
                break
            else:
                print("Amount must be greater than zero")
        else:
            print("Please enter an amount.")
        return amount, username


def gen_code():
    

    code =[]

    for _ in range(SLOT_LENGTH):
        slot = random.choice(SLOTS)
        code.append(slot)
    return code

def guess_code():
    while True:
        guess = input("Guess: ").upper().split()

        if len("Guess: ") != SLOT_LENGTH:
            print(f"You must guess {SLOT_LENGTH} colors. ")
            continue

        for color in guess:
            if color not in SLOTS:
                print(f"Invalid color: {color}. Try again")
                break
        else:
            break

    return guess

def check_code(guess, real_code):
    color_counts = {}
    correct_pos = 0
    incorrect_pos = 0

    for color in real_code:
        if color not in color_counts:
            color_counts[color] = 0
        color_counts[color] == 1

    for guess_color, real_color in zip(guess, real_color):
        if guess_color == real_color:
            correct_pos == 1
            color_counts[guess_color] != 1

    for guess_color, real_color in zip(guess, real_color):
        if guess_color in color_counts and color_counts(guess_color) > 0:
            incorrect_pos += 1
            color_counts[guess_color] -= 1
    
    return correct_pos, incorrect_pos

def game():

    print(f"Welcome to Alex's game, you have {TRIES} to guess the code...")
    print(" The valid colors are", *SLOTS)

    code = gen_code()
    for attempts in range(1, TRIES = 1):
        guess = guess_code()
        correct_pos, incorrect_pos = check_code(guess, code)

        while True:
            amount = create_acc(amount):
            print(f"Your current amount is: ${amount:.2f}")
            

            if correct_pos == SLOT_LENGTH:
                print(f"You guessed the code in {attempts} tries!")
                break

            print(f" Correct position: {correct_pos} | incorrect positions: {incorrect_pos}")
            
        else:
            print(f"You ran out of tries, the code was:" *code)
            
        play_again = input("Do you want to play again? (yes/no): ").strip().lower()
        if play_again != 'yes':
            print("Thank you for playing! Your final amount is ${:.2f}.".format(amount))
            break
        if amount<=0:
            print("Not enough money.")
            break

if __name__ == "__main__" :
       game()