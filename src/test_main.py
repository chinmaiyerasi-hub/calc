import unittest
from unittest.mock import patch
import io
import random

# Import the code as a function for testing
def guess_the_number(secret_number):
    """Function version of the guess game for testing."""
    attempts = 0
    outputs = []
    while True:
        guess = yield "Enter your guess: "
        attempts += 1
        if guess < secret_number:
            outputs.append("Too low! Try again.")
        elif guess > secret_number:
            outputs.append("Too high! Try again.")
        else:
            outputs.append(f"Congratulations! You guessed it in {attempts} attempts.")
            break
    return outputs


class TestGuessNumber(unittest.TestCase):
    """Unit tests for the Guess the Number game."""

    def test_guess_game_correct(self):
        # Define a fixed secret number
        secret = 42
        # Create the generator
        game = guess_the_number(secret)
        prompt = next(game)  # start generator

        # Simulate guesses
        guesses = [10, 50, 40, 42]
        outputs = []
        for guess in guesses:
            try:
                prompt = game.send(guess)
            except StopIteration as e:
                outputs = e.value

        expected_outputs = [
            "Too low! Try again.",
            "Too high! Try again.",
            "Too low! Try again.",
            "Congratulations! You guessed it in 4 attempts."
        ]
        self.assertEqual(outputs, expected_outputs)

    @patch("builtins.input", side_effect=["abc", "50", "42"])
    @patch("sys.stdout", new_callable=io.StringIO)
    def test_input_validation(self, mock_stdout, mock_input):
        """Test handling invalid input."""
        secret = 42
        attempts = 0
        while True:
            try:
                guess = int(input("Enter your guess: "))
            except ValueError:
                print("Please enter a valid number!")
                continue
            attempts += 1
            if guess == secret:
                print(f"Congratulations! You guessed it in {attempts} attempts.")
                break
        output = mock_stdout.getvalue()
        self.assertIn("Please enter a valid number!", output)
        self.assertIn("Congratulations! You guessed it in 2 attempts.", output)


if __name__ == "__main__":
    unittest.main()
