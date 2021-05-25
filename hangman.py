import string
from images import IMAGES
from words import choose_word


def is_word_guessed(secret_word, my_word):
    if secret_word==my_word:
        return True
    return False

def get_guessed_word(secret_word, letters_guessed):
    index = 0
    guessed_word = ""
    while (index < len(secret_word)):
        if secret_word[index] in letters_guessed:
            guessed_word += secret_word[index]
        else:
            guessed_word += "_"
        index += 1
    return guessed_word


def get_available_letters(letters_guessed):
    letters_left = string.ascii_lowercase
    for i in letters_guessed:
        if i in letters_left:
            letters_left = letters_left.replace(i,'')
    return letters_left


def hangman(secret_word):
    print("Welcome to the game, Hangman!")
    print("I am thinking of a word that is {} letters long.".format(
        str(len(secret_word))), end='\n\n')

    letters_guessed = []
    life = 8
    n = 0
    while life:
        available_letters = get_available_letters(letters_guessed)
        print("Available letters: {} ".format(available_letters))


        guess = input("Please guess a letter: ")
        letter = guess.lower()

        if letter in secret_word:
            letters_guessed.append(letter)
            my_word = get_guessed_word(secret_word, letters_guessed)
            print("Good guess: {} ".format(my_word))
            if is_word_guessed(secret_word, my_word) == True:
                print(" * * Congratulations, you won! * * ", end='\n\n')
        else:
            print("Oops! That letter is not in my word: {} ".format(
                get_guessed_word(secret_word, letters_guessed)))
            letters_guessed.append(letter)
            print("")
            print(IMAGES[n])
            n += 1
            life -= 1
    if life ==0:
        print("The correct word was {secret_word}")
secret_word = choose_word()
hangman(secret_word)