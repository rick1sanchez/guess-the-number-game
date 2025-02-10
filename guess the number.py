import random

def guess_the_number():
    print("Welcome to 'Guess the Number'!")
    print("I have picked a number between 1 and 100. Can you guess it?")
    
    # Generate a random number between 1 and 100
    target_number = random.randint(1, 100)
    attempts = 0
    guessed_correctly = False

    while not guessed_correctly:
        try:
            # Ask the user for their guess
            guess = int(input("Enter your guess: "))
            attempts += 1
            
            if guess < target_number:
                print("Too low! Try again.")
            elif guess > target_number:
                print("Too high! Try again.")
            else:
                print(f"Congratulations! You guessed the number in {attempts} attempts.")
                guessed_correctly = True

        except ValueError:
            print("Invalid input. Please enter a number.")

# Run the game
if __name__ == "__main__":
    guess_the_number()
