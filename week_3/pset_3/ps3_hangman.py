# Hangman game

import random
import string

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


def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    for char in secretWord:
        if char not in lettersGuessed:
            return False
    return True


def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    guessedString = ''
    for char in secretWord:
        if char in lettersGuessed:
            guessedString += char + ' '
        else:
            guessedString += '_ '
    return guessedString


def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    availableLetters = ''
    for alphabet in string.ascii_lowercase:
        if alphabet not in lettersGuessed:
            availableLetters += alphabet
    return availableLetters


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
    print("Welcome to the game, Hangman!")
    print("I am thinking of a word that is",str(len(secretWord)),"letters long.")
    print("-------------")

    guessesAvailable = 8
    lettersGuessed = []

    while guessesAvailable > 0:
        print("You have",str(guessesAvailable),"left")
        print("Available letters:",getAvailableLetters(lettersGuessed))
        guess = (input("Please guess a letter: ")).lower()
        if guess not in lettersGuessed:
            lettersGuessed.append(guess)
            if guess in secretWord:
                print("Good guess:",getGuessedWord(secretWord,lettersGuessed))
            else:
                print("Oops! That letter is not in my word:",getGuessedWord(secretWord,lettersGuessed))
                guessesAvailable -= 1
        else:
            print("Oops! You've already guessed that letter:",getGuessedWord(secretWord,lettersGuessed))
        print("-------------")
        if isWordGuessed(secretWord,lettersGuessed):
            print("Congratulations, you won!")
            return None

    print("Sorry, you ran out of guesses. The word was else. ")
    return None


wordlist = loadWords()
secretWord = chooseWord(wordlist).lower()
hangman(secretWord)
