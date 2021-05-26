from os import read
import string
from typing import List
from words import choose_word
from images import IMAGES
'''
Important instruction
* function and variable name snake_case -> is_prime
* contant variable upper case PI
'''

def is_word_guessed(secret_word: str, letters_guessed: list) -> bool:
    '''
    secret_word: word guess by the user
    letters_guessed: list hold all the word guess by the user
    returns: 
      return True (if user guess the world correctly )
      return False (wrong selection)
    '''
    index = 0
    guessed_word = ""
    while (index < len(secret_word)):
        if secret_word[index] in letters_guessed:
            guessed_word += secret_word[index]
            if guessed_word == secret_word:
                return True
        index += 1
    return False

# if you want to test this function please call function -> get_guessed_word("kindness", [k, n, d])


def get_guessed_word(secret_word: str, letters_guessed: list) -> str:
    '''
    secret_word: word guess by the user
    letters_guessed: list hold all the word guess by the user
    returns: 
      return string which contain all the right guessed characters
      Example :- 
      if secret_word -> "kindness" and letters_guessed = [k, n, s]
      return "k_n_n_ss"
    '''
    index = 0
    guessed_word = ""
    while (index < len(secret_word)):
        if secret_word[index] in letters_guessed:
            guessed_word += secret_word[index]
        else:
            guessed_word += "_"
        index += 1
    return guessed_word


def get_available_letters(letters_guessed: list) -> str:
    '''
    letters_guessed: list contains all guessed characters
    returns: 
      it return string which contains all characters except guessed letters
    Example :-
      letters_guessed = ['e', 'a'] then    
      return sting is -> `bcdfghijklmnopqrstuvwxyz`
    '''
    letters_left = ''.join(i for i in string.ascii_lowercase if i not in letters_guessed)
    return letters_left

def isValid(inputChar):
    return len(inputChar) == 1 and inputChar in string.ascii_lowercase

def hint(secret_word: str, letters_guessed: list) -> None:
    for i in secret_word:
        if i not in letters_guessed:
            print(f"Here's your hint 😉 : {i}")
            break
    
def hangman(secret_word):
    '''
    secret_word (string) : secret word to guessed by the user.

    Steps to start Hangman:

    * In the beginning of the game user will know about the total characters in the secret_word    

    * In each round user will guess one character 

    * After each character give feedback to the user
      * right or wrong

    * Display partial word guessed by the user and use underscore in place of not guess word    
    '''
    print("Welcome to the game, Hangman!")
    print("I am thinking of a word that is {} letters long.".format(
        str(len(secret_word))), end='\n\n')

    remaining_lives = 8
    hintTaken = False
    letters_guessed = []

    while remaining_lives:
        available_letters = get_available_letters(letters_guessed)
        print(f"Your Lives: {remaining_lives} | Available letters: {available_letters}")

        # Last life left alert
        if remaining_lives == 1:    print("\n ** Be careful, this is your last life! ** \n")

        guess = input("Please guess a letter: ")
        letter = guess.lower()
        
        if not isValid(letter):
            if letter == "hint":
                if not hintTaken:
                    hint(secret_word, letters_guessed);
                    hintTaken = True;
                else:   print("Sorry! You've already used 1 hint");
            else:
                print("Please, enter only one character from a to z. Try again!\n")
            continue

        if letter in secret_word:
            letters_guessed.append(letter)
            print("Good guess: {} ".format(
                get_guessed_word(secret_word, letters_guessed)))
            if is_word_guessed(secret_word, letters_guessed):
                print(" * * Congratulations, you won! * * ", end='\n\n')
                break
        else:
            remaining_lives -= 1
            if remaining_lives == 0:
                print(IMAGES[7])
                print("Sorry buddy, the man's hanged! 😐");
                break;
            print("Oops! That letter is not in my word: {} \n".format(
                get_guessed_word(secret_word, letters_guessed)))
            print(IMAGES[7-remaining_lives])
            letters_guessed.append(letter)


# Loaded the list of words into the variable wordlist
# So that it can be accessed from anywhere in the program
secret_word = choose_word()
hangman(secret_word)
