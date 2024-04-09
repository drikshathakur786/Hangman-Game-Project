import random
import tkinter as tk
from tkinter import messagebox

HANGMAN_PICS = ['''
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
   /|\  |
        |
       ===''', '''
    +---+
    O   |
   /|\  |
   /    |
       ===''', '''
    +---+
    O   |
   /|\  |
   / \  |
       ===''']

words_easy = ['cat', 'dog', 'hat', 'bat', 'rat']
words_medium = ['elephant', 'giraffe', 'zebra', 'kangaroo', 'ostrich']
words_hard = ['hangman', 'xylophone', 'python', 'jazz', 'wizard']

def getRandomWord(wordList):
    """
    Returns a random string from the passed list of strings.
    """
    return random.choice(wordList)

def displayBoard(missedLetters, correctLetters, secretWord):
    """
    Displays the hangman ASCII art, missed letters, and the current state of the guessed word.
    """
    hangman_label.config(text=HANGMAN_PICS[len(missedLetters)])
    missed_label.config(text='Missed letters: ' + ' '.join(missedLetters))
    blanks = ' '.join('_' if letter not in correctLetters else letter for letter in secretWord)
    word_label.config(text=blanks)

def getGuess(alreadyGuessed):
    """
    Returns the letter the player entered.
    Ensures the player enters a single letter and nothing else.
    """
    guess = guess_entry.get().lower()
    guess_entry.delete(0, tk.END)
    if len(guess) != 1:
        messagebox.showwarning("Invalid Guess", "Only a single letter is allowed.")
        return None
    elif guess in alreadyGuessed:
        messagebox.showwarning("Invalid Guess", "You have already guessed that letter. Choose again.")
        return None
    elif guess not in 'abcdefghijklmnopqrstuvwxyz':
        messagebox.showwarning("Invalid Guess", "Please enter a letter from the alphabet.")
        return None
    else:
        return guess

def checkGameStatus(missedLetters, correctLetters, secretWord):
    """
    Checks if the game is over (win/lose).
    """
    if len(missedLetters) == len(HANGMAN_PICS) - 1:
        displayBoard(missedLetters, correctLetters, secretWord)
        messagebox.showinfo("Game Over", f"You have run out of guesses!\nAfter {len(missedLetters)} missed guesses and {len(correctLetters)} correct guesses, the word was '{secretWord}'.")
        return True
    elif all(letter in correctLetters for letter in secretWord):
        messagebox.showinfo("Congratulations!", f"You guessed it!\nThe secret word is '{secretWord}'! You win!")
        return True
    return False

def guessLetter():
    """
    Handles the guess button click event.
    """
    global missedLetters, correctLetters
    guess = getGuess(missedLetters + correctLetters)
    if guess is None:
        return
    if guess in secretWord:
        correctLetters += guess
    else:
        missedLetters += guess
    displayBoard(missedLetters, correctLetters, secretWord)
    if checkGameStatus(missedLetters, correctLetters, secretWord):
        resetGame()

def resetGame():
    """
    Resets the game state.
    """
    global missedLetters, correctLetters, secretWord
    missedLetters = ''
    correctLetters = ''
    if difficulty_var.get() == 'Easy':
        secretWord = getRandomWord(words_easy)
    elif difficulty_var.get() == 'Medium':
        secretWord = getRandomWord(words_medium)
    elif difficulty_var.get() == 'Hard':
        secretWord = getRandomWord(words_hard)
    displayBoard(missedLetters, correctLetters, secretWord)

def displayInstructions():
    """
    Displays the instructions in a message box.
    """
    instructions = """
    Welcome to Hangman Game!

    Instructions:
    1. Choose a difficulty level.
    2. Guess letters to reveal the secret word.
    3. You can only guess one letter at a time.
    4. If the letter is in the word, it will be revealed.
    5. If the letter is not in the word, a part of the hangman will be drawn.
    6. Keep guessing until you reveal the word or the hangman is complete.
    7. Enjoy the game!

    Good luck!
    """
    messagebox.showinfo("Instructions", instructions)

# Create main window
root = tk.Tk()
root.title("Hangman Game")

# Create and place widgets
hangman_label = tk.Label(root, text='')
hangman_label.grid(row=0, column=0, columnspan=2)

word_label = tk.Label(root, text='')
word_label.grid(row=1, column=0, columnspan=2)

missed_label = tk.Label(root, text='')
missed_label.grid(row=2, column=0, columnspan=2)

guess_label = tk.Label(root, text="Guess a letter:")
guess_label.grid(row=3, column=0)

guess_entry = tk.Entry(root, width=10)
guess_entry.grid(row=3, column=1)

guess_button = tk.Button(root, text="Guess", command=guessLetter)
guess_button.grid(row=4, column=0, columnspan=2)

difficulty_label = tk.Label(root, text="Select Difficulty:")
difficulty_label.grid(row=5, column=0)

difficulty_var = tk.StringVar()
difficulty_var.set('Easy')
difficulty_menu = tk.OptionMenu(root, difficulty_var, 'Easy', 'Medium', 'Hard')
difficulty_menu.grid(row=5, column=1)

reset_button = tk.Button(root, text="Reset", command=resetGame)
reset_button.grid(row=6, column=0, columnspan=2)

instruction_button = tk.Button(root, text="Instructions", command=displayInstructions)
instruction_button.grid(row=7, column=0, columnspan=2)

# Initialize game variables
missedLetters = ''
correctLetters = ''
secretWord = getRandomWord(words_easy)
displayBoard(missedLetters, correctLetters, secretWord)

root.mainloop()
