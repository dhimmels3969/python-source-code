from src.common_library import helper_functions as hf
import string_exercises.exercises as s1
import string_exercises.exercises_02 as s2

class Driver():

    """
    Driver Class

    Implements run function which executes multiple functions in the loop_exercises folder.

    TODO:
        Set up a dictionary to control which function gets executed and which functions get bypassed.
    """
    def __init__(self):
        pass

    def run(self):
        print("#####################################################")
        print("String Exercises - 1 through 10")
        print("#####################################################")
        results = s1.exercise_01_grab_first_middle_last_character()
        results = s1.exercise_02_grab_middle_three_characters()
        results = s1.exercise_03_insert_data_in_middle_of_string()
        results = s1.exercise_04_create_new_string()
        results = s1.exercise_05_reverse_a_string()
        results = s1.exercise_06_find_last_occurrence()
        results = s1.exercise_07_split_string_using_delimiter()
        results = s1.exercise_08_find_all_occurrences()
        results = s1.exercise_09_balanced_strings_check()
        results = s1.exercise_10_vowel_counter()

        print("#####################################################")
        print("String Exercises - 11 through 20")
        print("#####################################################")

        print("#####################################################")
        print("String Exercises - 21 through 30")
        print("#####################################################")

        print("#####################################################")
        print("String Exercises - 31 through 40")
        print("#####################################################")