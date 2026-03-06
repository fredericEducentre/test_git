import random

def play_game():
    secret_number = random.randint(1, 10)
    attempts = 0
    
    print("--- Welcome to the Guessing Game! ---")
    print("I'm thinking of a number between 1 and 10.")

    while True:
        try:
            guess = int(input("Enter your guess: "))
            attempts += 1

            if guess < secret_number:
                print("Too low! Try again.")
            elif guess > secret_number:
                print("Too high! Try again.")
            else:
                print(f"🎉 Correct! You found it in {attempts} tries.")
                break
        except ValueError:
            print("Please enter a valid number.")

if __name__ == "__main__":
    play_game()