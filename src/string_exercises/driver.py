from src.common_library import helper_functions as hf
import string_exercises.exercises as s1
import string_exercises.exercises_02 as s2
import string_exercises.exercises_03 as s3
import string_exercises.exercises_04 as s4

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

        print()
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

        print()
        print("#####################################################")
        print("String Exercises - 11 through 20")
        print("#####################################################")
        results = s2.exercise_11_prefix_suffix_check()
        results = s2.exercise_12_swap_case()
        results = s2.exercise_13_remove_whitespace()
        results = s2.exercise_14_character_removal()
        results = s2.exercise_15_string_partition_test()
        results = s2.exercise_16_extract_file_extension()
        results = s2.exercise_17_sort_lower_case_and_upper_case()
        results = s2.exercise_18_count_letters_digits_symbols()
        results = s2.exercise_19_alternating_characters()
        results = s2.exercise_20_calculate_sums_and_averages()

        print()
        print("#####################################################")
        print("String Exercises - 21 through 30")
        print("#####################################################")

        results = s3.exercise_21_count_occurrences()
        results = s3.exercise_22_remove_empty_strings()
        results = s3.exercise_23_remove_special_symbols()
        results = s3.exercise_24_keep_only_integers()
        results = s3.exercise_25_find_words_with_letters_and_numbers()
        results = s3.exercise_26_replace_symbols()
        results = s3.exercise_27_palindrome_check()
        results = s3.exercise_28_anagram_detector()
        results = s3.exercise_29_unique_character_check()
        results = s3.exercise_30_title_case_logic()

        print()
        print("#####################################################")
        print("String Exercises - 31 through 40")
        print("#####################################################")
        results = s4.exercise_31_remove_duplicate_characters()
        results = s4.exercise_32_word_reversal()
        results = s4.exercise_33_character_interleaving()
        results = s4.exercise_34_longest_word()
        results = s4.exercise_35_acronym_generator()
        results = s4.exercise_36_word_frequency()
        results = s4.exercise_37_first_non_repeating_character()
        results = s4.exercise_38_string_rotation_check()
