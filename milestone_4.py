import random

word_list = ["apple", "pear", "orange", "blueberry", "banana"]

class Hangman:

    def __init__(self, word_list, num_lives=5):
        self.word_list = word_list
        self.num_lives = num_lives
        self.word = random.choice(word_list)
        self.word_guessed = ['_' for _ in range(len(self.word))]  # underscores for each letter
        self.num_letters = len(set(self.word))
        self.list_of_guesses = []

    def ask_for_input(self):
        while self.num_lives > 0 and self.num_letters > 0:
            guess = input("Guess a letter: ")
            if not guess.isalpha() or len(guess) != 1:
                print("Invalid letter. Please, enter a single alphabetical character.")
            elif guess in self.list_of_guesses:
                print("You already tried that letter!")
            else:
                self.check_guess(guess)
                self.list_of_guesses.append(guess)
                print("Word guessed so far:", ' '.join(self.word_guessed))  # Print the word guessed so far

        if self.num_letters == 0:
            print("Congratulations! You've guessed the word:", ''.join(self.word_guessed))
        else:
            print("Out of lives. The word was:", self.word)

    def check_guess(self, guess):
        guess = guess.lower()
        if guess in self.word:
            print(f"Good guess! {guess} is in the word")

            for i in range(len(self.word)):
                if self.word[i].lower() == guess:
                    self.word_guessed[i] = self.word[i]  # Replace underscore with the guessed letter
            self.num_letters -= 1

        else:
            self.num_lives -= 1
            print(f"Sorry, {guess} is not in the word")
            print(f"You have {self.num_lives} lives left")
    
def play_game(word_list):
    num_lives = 5
    game = Hangman(word_list, num_lives)

    while True:
        if game.num_lives == 0:
            print("You lost!")
            break
        elif game.num_letters > 0:
            game.ask_for_input()
        else:
            print("Congratulations. You won the game!")
            break


play_game(word_list)

