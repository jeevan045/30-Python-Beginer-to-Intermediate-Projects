import random


class NumberGuessGame:
    def __init__(self, max_attempts=5, lower=1, upper=100):
        self.lower = lower
        self.upper = upper
        self.max_attempts = max_attempts
        self.reset_game()
        self.score = 0

    def reset_game(self):
        self.number_to_guess = random.randint(self.lower, self.upper)
        self.attempts_left = self.max_attempts
        print(f"\nNew Game Started! Guess a number between {self.lower} and {self.upper}")
        print(f"You have {self.attempts_left} attempts.\n")

    def make_guess(self, guess):
        if self.attempts_left <= 0:
            return "No attempts left! Game over."

        self.attempts_left -= 1

        if guess == self.number_to_guess:
            points = self.attempts_left * 10
            self.score += points
            return f"Correct! The number was {self.number_to_guess}. You earned {points} points."

        if abs(guess - self.number_to_guess) <= 5:
            hint = "Very close!"
        elif guess < self.number_to_guess:
            hint = "Too low!"
        else:
            hint = "Too high!"

        return f"{hint} Attempts left: {self.attempts_left}"

    def has_attempts(self):
        return self.attempts_left > 0


def choose_difficulty():
    print("Select Difficulty Level:")
    print("1. Easy (1-50, 10 attempts)")
    print("2. Medium (1-100, 7 attempts)")
    print("3. Hard (1-200, 5 attempts)")

    choice = input("Enter choice (1/2/3): ")
    if choice == "1":
        return NumberGuessGame(max_attempts=10, lower=1, upper=50)
    elif choice == "3":
        return NumberGuessGame(max_attempts=5, lower=1, upper=200)
    else:
        return NumberGuessGame(max_attempts=7, lower=1, upper=100)


if __name__ == "__main__":
    while True:
        game = choose_difficulty()

        while game.has_attempts():
            try:
                guess = int(input("Enter your guess: "))
                result = game.make_guess(guess)
                print(result)

                if "Correct" in result:
                    break
            except ValueError:
                print("Please enter a valid number.")

        if not game.has_attempts():
            print(f"Out of attempts! The number was {game.number_to_guess}.")

        print(f"Your current score: {game.score}")
        again = input("Do you want to play again? (y/n): ")
        if again.lower() != "y":
            print("Thanks for playing! Final Score:", game.score)
            break
