import random

# Generate a random number between 1 and 20
secret_number = random.randint(1, 20)

guesses = 0
max_guesses = 5

print("Guess the number between 1 and 20!")
print(f"You have {max_guesses} guesses.\n")

while guesses < max_guesses:
    try:
        user_guess = int(input("Enter your guess: "))
    except ValueError:
        print("Please enter a valid number.")
        continue

    guesses += 1

    if user_guess == secret_number:
        print(f"\n🎉 Congratulations! You guessed the number in {guesses} tries!")
        break
    elif user_guess < secret_number:
        print("Too low!")
    else:
        print("Too hgh!")

    print(f"Guesses left: {max_guesses - guesses}\n")

if guesses == max_guesses and user_guess != secret_number:
    print(f"\n❌ Game newnewnwne! {secret_number}.")
