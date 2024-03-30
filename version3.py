import tkinter as tk
from tkinter import messagebox
import random

# Hangman graphics for different stages of the game
HANGMAN_GRAPHICS = ['''
  +---+
      |
      |
      |
     ===''', '''
  +---+
  O   |
      |
      |
     ===''', '''
  +---+
  O   |
  |   |
      |
     ===''', '''
  +---+
  O   |
 /|   |
      |
     ===''', '''
  +---+
  O   |
 /|\\  |
      |
     ===''', '''
  +---+
  O   |
 /|\\  |
 /    |
     ===''', '''
  +---+
  O   |
 /|\\  |
 / \\  |
     ===''']

# List of words for the game
word_list = ['cat', 'dog', 'fish', 'bird', 'frog', 'lion', 'duck', 'bear', 'deer', 'wolf', 'snake']

# Hangman game class
class HangmanGame:
    def __init__(self, master):
        self.master = master
        self.master.title("Hangman Game")

        # Initialize game variables
        self.missed_letters = ''
        self.correct_letters = ''
        self.secret_word = ''
        self.game_over = False
        self.attempts_left = len(HANGMAN_GRAPHICS) - 1
        self.score = 0

        # Create canvas for graphics
        self.canvas = tk.Canvas(master, width=400, height=400, bg="lightblue")
        self.canvas.pack()

        # Start/reset the game
        self.reset_game()

    # Reset the game
    def reset_game(self):
        self.missed_letters = ''
        self.correct_letters = ''
        self.secret_word = self.choose_random_word(word_list)
        self.game_over = False
        self.attempts_left = len(HANGMAN_GRAPHICS) - 1
        self.draw_hangman(0)
        self.display_word()

    # Choose a random word from the word list
    def choose_random_word(self, words):
        return random.choice(words)

    # Draw hangman graphics
    def draw_hangman(self, missed_attempts):
        self.canvas.delete("hangman")
        self.canvas.create_text(200, 50, text="Hangman", font=("Helvetica", 24), fill="black", tag="hangman")
        self.canvas.create_text(200, 350, text="Attempts Left: " + str(self.attempts_left), font=("Helvetica", 14), fill="black", tag="hangman")
        self.canvas.create_text(200, 380, text="Missed Letters: " + " ".join(self.missed_letters), font=("Helvetica", 14), fill="black", tag="hangman")
        self.canvas.create_text(200, 200, text=HANGMAN_GRAPHICS[missed_attempts], font=("Courier", 24), fill="black", tag="hangman")

    # Display the word with correct guesses
    def display_word(self):
        displayed_word = ''
        for letter in self.secret_word:
            if letter in self.correct_letters:
                displayed_word += letter + ' '
            else:
                displayed_word += '_ '
        self.canvas.create_text(200, 300, text=displayed_word, font=("Helvetica", 24), fill="black", tag="hangman")

    # Check game state for win/lose
    def check_game_state(self):
        if all(letter in self.correct_letters for letter in self.secret_word):
            self.score += 1
            messagebox.showinfo("Hangman", "You guessed it!\nThe secret word is '{}'. You win!\nScore: {}".format(self.secret_word, self.score))
            self.game_over = True
        elif self.attempts_left == 0:
            messagebox.showinfo("Hangman", "You have run out of attempts!\nThe word was '{}'. Try again!".format(self.secret_word))
            self.game_over = True

    # Make a guess
    def make_guess(self, letter):
        if letter in self.correct_letters or letter in self.missed_letters:
            messagebox.showinfo("Hangman", "You've already guessed this letter!")
        elif letter in self.secret_word:
            self.correct_letters += letter
        else:
            self.missed_letters += letter
            self.attempts_left -= 1

        self.draw_hangman(len(self.missed_letters))
        self.display_word()
        self.check_game_state()

    # Provide a hint
    def provide_hint(self):
        messagebox.showinfo("Hangman", "Using the hint won't affect your score or the number of attempts left.")
        # Find the first letter in the secret word that hasn't been guessed yet
        for letter in self.secret_word:
            if letter not in self.correct_letters:
                # Display this letter as a hint
                self.correct_letters += letter
                break
        # Update display
        self.display_word()

# Start the game
def start_game():
    root = tk.Tk()
    game = HangmanGame(root)

    # Handle user guesses
    def handle_guess():
        guess = entry_guess.get().lower()
        if guess.isalpha() and len(guess) == 1:
            game.make_guess(guess)
        else:
            messagebox.showinfo("Hangman", "Please enter a single letter.")

        entry_guess.delete(0, tk.END)

    # Handle hint button click
    def handle_hint():
        game.provide_hint()

    # GUI setup
    frame = tk.Frame(root, bg="lightblue")
    frame.pack(pady=20)

    label_guess = tk.Label(frame, text="Enter a letter:", bg="lightblue", font=("Helvetica", 12))
    label_guess.pack(side=tk.LEFT)

    entry_guess = tk.Entry(frame, font=("Helvetica", 12))
    entry_guess.pack(side=tk.LEFT)

    button_guess = tk.Button(frame, text="Guess", command=handle_guess, font=("Helvetica", 12))
    button_guess.pack(side=tk.LEFT)

    button_hint = tk.Button(frame, text="Hint", command=handle_hint, font=("Helvetica", 12))
    button_hint.pack(side=tk.LEFT)

    button_reset = tk.Button(frame, text="Reset", command=game.reset_game, font=("Helvetica", 12))
    button_reset.pack(side=tk.LEFT)

    root.mainloop()

# Start the game when script is run
start_game()

