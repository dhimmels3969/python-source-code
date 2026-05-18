# Wordle in Python... pass #3

import random as r
import os
from pathlib import Path
from src.common_library import helper_functions as hf


##############################################################################
def word_list(root_dir):
    """
    Implement a function word_list() that reads the 5_letter_words.txt file
        and returns a list of the words in the file.
    :return:   list of 5-letter words copied from external file.
    :rtype:    list
    """
    my_word_list = []
    file_path = hf.build_file_name(root_dir, "data/wordle", "5_letter_words.txt")
    with open(file_path, "r") as file:
        # read file in one go
        for line in file:
            line = line.strip()
            my_word_list.append(line)
    return my_word_list


##############################################################################
def random_word(the_word_list):
    """
    Implement a function random_word() that takes a list of words as a parameter
        and returns a random word from this list.
    :param the_word_list:
    :type the_word_list:
    :return:
    :rtype:
    """
    index = r.randint(0, len(the_word_list) - 1)
    word_to_guess = the_word_list[index]
    return word_to_guess


##############################################################################
def is_real_word(guess, the_word_list):
    """
    Implement a function is_real_word() that takes two parameters, a guess
        and a word list and returns True if the word is in the word list
        and False otherwise.
    :param guess:
    :type guess:
    :param the_word_list:
    :type the_word_list:
    :return:
    :rtype:
    """
    return guess in the_word_list


##############################################################################
def check_guess(guess, answer):
    """
    Implement a function check_guess()that takes two parameters. The first
        is the guessed word and the second is the word the user has to find.
        check_guess() returns a string containing the following characters:
        If a letter is used twice in the guessed word and exists only once in
        the word to be found, then only one letter in the return string is
        marked. In case one of the two letters is positioned correctly, then
        this letter is marked with an X in the return string. For example,
        check_guess("carat", "train") should return _OO_O. Another example,
        check_guess("taunt", "train") should return XO_O_
    :param guess:
    :type guess:
    :param answer:
    :type answer:
    :return:
    :rtype:
    """
    results = ""
    letters_used = []
    answer_as_list = list(answer)
    guess_as_list = list(guess)
    letter_status = list("NNNNN")
    for i in range(0, len(guess_as_list)):
        if guess_as_list[i] == answer_as_list[i]:
            results += "X"
            letter_status[i] = "Y"
        elif guess_as_list[i] not in answer_as_list:
            results += "_"
        else:
            #### iterate through answer_as_list checking the letter_status at each location
            letter_found = False
            for j in range(0, len(answer_as_list)):
                if guess_as_list[i] == answer_as_list[j] and letter_status[j] == "N":
                    results += "O"
                    letter_status[j] = "Y"
                    letter_found = True
                    break
            if not letter_found:
                results += "_"
        letters_used.append(guess_as_list[i])
    return results


##############################################################################
def next_guess(the_word_list):
    """
    Implement a function next_guess() that takes a word list as a parameter. The
        function asks the user for a guess, converts the guess to lower case and
        checks if the guess is in the word list. If this is the case, the
        guess is returned. Otherwise, the function asks the user for
        another guess.
    :param the_word_list:   complete word list used in the game
    :type the_word_list:    list
    :return:  the word entered by the user in lower case
    :rtype:   str
    """
    valid_word_not_provided = True
    while valid_word_not_provided:
        your_guess = input("Please enter a guess: ")
        your_guessL = your_guess.lower()
        if is_real_word(your_guessL, the_word_list):
            valid_word_not_provided = False
        else:
            print("That's not a real word!")
    return your_guessL


##############################################################################
def play(root_dir):
    """
    Implement a function play() that:
        Uses the functions word_list and random_word to select a random 5 letter word.
        Asks the user for a guess using the next_guess function.
        Checks each guess using the check_guess function and shows the result to the user.
        Checks if the users guessed the right word with six guesses or less.
        If yes, the user wins and the function prints You won!.
        Otherwise the user loses and the function prints You lost!
            as well as The word was: followed by word the user had to find.
    :param root_dir:
    :type root_dir:
    :return: None
    :rtype:  None
    """
    max_guesses = 6
    word_not_guessed = True
    wordle_word_list = word_list(root_dir)
    word_to_guess = random_word(wordle_word_list)
    #     print(word_to_guess)
    number_of_guesses = 0
    while number_of_guesses < max_guesses and word_not_guessed:
        your_guess = next_guess(wordle_word_list)
        # check the guess here...
        guess_check = check_guess(your_guess.lower(), word_to_guess)
        print(guess_check)
        if guess_check == "XXXXX":
            word_not_guessed = False
        number_of_guesses += 1

    if not word_not_guessed:
        print("You won!")
    else:
        print("You lost!")
        print(f"The word was: {word_to_guess}")

    return ""

##############################################################################
class wordle():
    def __init__(self, root):
        self.root = root

    def play(self):
        def display_message(message):
            print(80*"=")
            print(message)
            print(80*"=")
            print()

        exit_not_selected = True
        display_message("Welcome to Wordle!")
        while exit_not_selected:
            choice = input("Enter 99 to quit, any other key to play another game: ")
            if choice == "99":
                exit_not_selected = False
                display_message("Thanks for playing Wordle!")
                break
            else:
                play(self.root)
                print()
                continue
