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
    for letter in secretWord:
        if letter not in lettersGuessed:
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
    lettersCorrect = ''
    for letter in secretWord:
        if letter in lettersGuessed:
            lettersCorrect += letter
        else:
            lettersCorrect += '_ '
    return lettersCorrect


def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    # FILL IN YOUR CODE HERE...
    import string
    alpha = string.ascii_lowercase
    for letter in lettersGuessed:
        alpha = alpha.replace(letter, "")
    return alpha
    #return ''.join(set(string.ascii_letters) - set(lettersGuessed))

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
    ## intro to thegame
    print("Welcome to the game, Hangman!")
    print("I am thinking of a word that is " + str(len(secretWord)) + " letters long.")
    print("- - - - - - - - - - - - - - -")
    
    ## setup the variable to store all the guesses
    ## and the variable to check how many more turns the user has
    lettersGuessed = []
    mistakesMade = 0
    
    ## loop until the user is out of guesses
    while mistakesMade < 8:
        ## provide some info to the user, then ask them to guess a letter
        ## convert the letter to lowercase
        print("You have " + str(8 - mistakesMade) + " guesses left")
        print("Available letters: " + getAvailableLetters(lettersGuessed))
        guess = input("Please guess a letter: ").lower()
        
        ## check if the user already guessed the letter
        if guess in lettersGuessed:
            print("Oops! You've already guessed that letter: " + getGuessedWord(secretWord, lettersGuessed))
        ## check if the guessed letter is in the secretWord
        elif guess in secretWord:
            lettersGuessed.append(guess)
            print("Good guess: " + getGuessedWord(secretWord, lettersGuessed))
        ## assume that the letter isn't in the secretWord
        ## increase the number of mistakes the user has made so their remaining
        ## turns decrements by one
        else:
            lettersGuessed.append(guess)
            print("Oops! That letter is not in my word: " + getGuessedWord(secretWord, lettersGuessed))
            mistakesMade += 1
        print("- - - - - - - - - - - - - - -")

        ## check if the word has been fully guessed
        ## if so then end the game
        if isWordGuessed(secretWord, lettersGuessed):
            print("Congratulations, you won!")
            
    ## check if the used up all his guesses  
    if mistakesMade > 7:
        print("Sorry, you ran out of guesses. The word was " + secretWord + ".")

# When you've completed your hangman function, uncomment these two lines
# and run this file to test! (hint: you might want to pick your own
# secretWord while you're testing)

secretWord = chooseWord(wordlist).lower()
hangman(secretWord)
