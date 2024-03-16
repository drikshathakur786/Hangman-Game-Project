import random
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

word_list = ['afghanistan', 'albania', 'algeria', 'andorra', 'angola', 'argentina', 'armenia', 'australia', 'austria', 'azerbaijan', 'bahamas', 'bahrain', 'bangladesh', 'barbados', 'belarus', 'belgium', 'belize', 'benin', 'bhutan', 'bolivia', 'bosnia', 'botswana', 'brazil', 'brunei', 'bulgaria', 'burkina', 'burundi', 'cambodia', 'cameroon', 'canada', 'cape verde', 'chad', 'chile', 'china', 'colombia', 'comoros', 'congo', 'croatia', 'cuba', 'cyprus', 'czech republic', 'denmark', 'djibouti', 'dominica', 'ecuador', 'egypt', 'el salvador', 'equatorial guinea', 'eritrea', 'estonia', 'ethiopia', 'fiji', 'finland', 'france', 'gabon', 'gambia', 'georgia', 'germany', 'ghana', 'greece', 'grenada', 'guatemala', 'guinea', 'guyana', 'haiti', 'honduras', 'hungary', 'iceland', 'india', 'indonesia', 'iran', 'iraq', 'ireland', 'israel', 'italy', 'jamaica', 'japan', 'jordan', 'kazakhstan', 'kenya', 'kiribati', 'kuwait', 'kyrgyzstan', 'laos', 'latvia', 'lebanon', 'lesotho', 'liberia', 'libya', 'liechtenstein', 'lithuania', 'luxembourg', 'macedonia', 'madagascar', 'malawi', 'malaysia', 'maldives', 'mali', 'malta', 'marshall islands', 'mauritania', 'mauritius', 'mexico', 'micronesia', 'moldova', 'monaco', 'mongolia', 'montenegro', 'morocco', 'mozambique', 'myanmar', 'namibia', 'nauru', 'nepal', 'netherlands', 'new zealand', 'nicaragua', 'niger', 'nigeria', 'north korea', 'norway', 'oman', 'pakistan', 'palau', 'panama', 'papua new guinea', 'paraguay', 'peru', 'philippines', 'poland', 'portugal', 'qatar', 'romania', 'russia', 'rwanda', 'saint kitts and nevis', 'saint lucia', 'saint vincent and the grenadines', 'samoa', 'san marino', 'sao tome and principe', 'saudi arabia', 'senegal', 'serbia', 'seychelles', 'sierra leone', 'singapore', 'slovakia', 'slovenia', 'solomon islands', 'somalia', 'south africa', 'south korea', 'south sudan', 'spain', 'sri lanka', 'sudan', 'suriname', 'swaziland', 'sweden', 'switzerland', 'syria', 'taiwan', 'tajikistan', 'tanzania', 'thailand', 'togo', 'tonga', 'trinidad and tobago', 'tunisia', 'turkey', 'turkmenistan', 'tuvalu', 'uganda', 'ukraine', 'united arab emirates', 'united kingdom', 'united states', 'uruguay', 'uzbekistan', 'vanuatu', 'venezuela', 'vietnam', 'yemen', 'zambia', 'zimbabwe']

def choose_random_word(words):
    """
    Returns a random word from the given list.
    """
    word_index = random.randint(0, len(words) - 1)
    return words[word_index]

def display_hangman(missed_attempts):
    print(HANGMAN_GRAPHICS[len(missed_attempts)])

def display_word(word, guessed_letters):
    """
    Displays the word with correctly guessed letters and underscores for missing letters.
    """
    for letter in word:
        if letter in guessed_letters:
            print(letter, end=' ')
        else:
            print('_', end=' ')
    print()

def get_guess(already_guessed):
    """
    Returns a valid single letter guess from the player.
    """
    while True:
        guess = input('Please guess a letter: ').lower()
        if len(guess) != 1:
            print('Please enter only one letter at a time.')
        elif guess not in 'abcdefghijklmnopqrstuvwxyz':
            print('Please enter a letter from the alphabet.')
        elif guess in already_guessed:
            print('You have already guessed that letter. Try again.')
        else:
            return guess

def play_again():
    """
    Asks the player if they want to play again.
    """
    return input('Would you like to play again? (yes/no): ').lower().startswith('y')

def hangman_game():
    print('|H_A_N_G_M_A_N|')

    missed_letters = ''
    correct_letters = ''
    secret_word = choose_random_word(word_list)
    game_over = False

    while True:
        display_hangman(missed_letters)
        display_word(secret_word, correct_letters)

        # Let the player guess a letter:
        guess = get_guess(missed_letters + correct_letters)

        if guess in secret_word:
            correct_letters += guess

            # Check if player has won:
            if all(letter in correct_letters for letter in secret_word):
                print('You guessed it!')
                print('The secret word is "' + secret_word + '". You win!')
                game_over = True
        else:
            missed_letters += guess

            # Check if player has lost:
            if len(missed_letters) == len(HANGMAN_GRAPHICS) - 1:
                display_hangman(missed_letters)
                print('You have run out of guesses!\nAfter ' + str(len(missed_letters)) + ' missed guesses and ' + str(len(correct_letters)) + ' correct guesses, the word was "' + secret_word + '".')
                game_over = True

        # Check if the game is over, then ask the player to play again:
        if game_over:
            if play_again():
                missed_letters = ''
                correct_letters = ''
                game_over = False
                secret_word = choose_random_word(word_list)
            else:
                break
# Start the game:
hangman_game()