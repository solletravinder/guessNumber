import random


class GuessNumber:

    def __init__(self, min_value, max_value):
        self.number = random.randint(min_value, max_value)
        self.min_value, self.max_value = min_value, max_value
        self.guesses = 0

    def get_guess(self):
        guess = input(f"Please guess a number ({self.min_value} - {self.max_value}): ")
        if self.valid_guess(guess):
            return int(guess)
        print("Please enter a valid number.")
        return self.get_guess()

    def take_range_and_continue(self):
        range_val = input("Please enter a range(hyphen separated, e.g, 0-100): ")
        if self.valid_range(range_val):
            min_value, max_value = range_val.split("-")
            return GuessNumber(int(min_value), int(max_value)).play()
        else:
            print("Please enter a valid range(hyphen separated, e.g, 0-100).")
            return self.take_range_and_continue()

    def valid_guess(self, str_number):
        try:
            number = int(str_number)
        except ValueError:
            return False
        return self.min_value <= number <= self.max_value

    def valid_range(self, range):
        try:
            min_value, max_value = range.split("-")
            min_value, max_value = int(min_value), int(max_value)
        except Exception as e:
            print(e)
            return False
        return True

    def play(self):
        while 1:
            self.guesses += 1
            guess = self.get_guess()
            if guess < self.number:
                print("Your guess was under.")
            elif guess > self.number:
                print("Your guess was over.")
            else:
                break

        print(f"You guessed it in {self.guesses} guesses.")
        if not self.play_more():
            return
        self.take_range_and_continue()

    def play_more(self):
        play_more = input("Do you wanna play more?")
        return play_more != '' and (not play_more or play_more.lower() != 'no')