# Hangman game
#

# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)

import random

WORDLIST_FILENAME = "words.txt"

def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist

def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code
# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = loadWords()

def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    # FILL IN YOUR CODE HERE...
    for letter_secret in secretWord:
        if letter_secret not in lettersGuessed:
            return False
    return True



def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    # FILL IN YOUR CODE HERE...
    guessed_word = ""
    for letter_secret in secretWord:
        if letter_secret in lettersGuessed:
            guessed_word += (letter_secret + " ")
        else:
            guessed_word += "_ "
    return guessed_word



def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    # FILL IN YOUR CODE HERE...
    available = list("abcdefghijklmnopqrstuvwxyz")
    for letter in lettersGuessed:
        available.remove(letter)
    return "".join(available)
    


def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many 
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the 
      partially guessed word so far, as well as letters that the 
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE...
    print("Welcome to the game, Hangman!")
    num_letters = len(secretWord)
    print("I am thinking of a word that is", str(num_letters), "letters long.")

    letters_guessed = []
    mistakes_made = 0
    num_guesses = 8
    available_letters = getAvailableLetters(letters_guessed)
    won = False
    lost = False
    
    while not won and not lost:
        print("----------------------------")
        print("You have", str(num_guesses - mistakes_made), "guesses left.")
        print("Available letters:", available_letters)
        guess = (input("Please guess a letter: ")).lower()
        if guess not in letters_guessed:
            letters_guessed.append(guess)
            available_letters = getAvailableLetters(letters_guessed)
            if guess in secretWord:
                print("Good guess:", getGuessedWord(secretWord, letters_guessed))
                if isWordGuessed(secretWord, letters_guessed):
                    won = True
                    continue
            else:
                print("Oops! That letter is not in my word:", getGuessedWord(secretWord, letters_guessed))
                mistakes_made += 1
                if mistakes_made >= num_guesses:
                    lost = True
                    continue
        else:
            print("Oops! You've already guessed that letter:", getGuessedWord(secretWord, letters_guessed))
            continue
    print("----------------------------")
    if won:
        print("Congratulations, you won!")
    elif lost:
        print("Sorry, you ran out of guesses. The word was " + secretWord + ".")




# When you've completed your hangman function, uncomment these two lines
# and run this file to test! (hint: you might want to pick your own
# secretWord while you're testing)

secretWord = chooseWord(wordlist).lower()
hangman(secretWord)
