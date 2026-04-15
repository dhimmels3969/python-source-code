
from src.common_library import helper_functions as hf
import loop_exercises.exercises as l1
import loop_exercises.exercises_02 as l2
import loop_exercises.exercises_04 as l4

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
        print("Loop Exercises - start")

        results = l1.exercise_01_print_numbers_using_while(10)
        results = l1.exercise_02_display_negative_numbers()
        results = l1.exercise_03_loop_completion_test()
        results = l1.exercise_04_calculate_sum()
        results = l1.exercise_05_multiplication_table(2, 10)
        results = l1.exercise_06_calculate_cube()
        results = l1.exercise_07_display_list_items()
        results = l1.exercise_08_count_occurrences()
        results = l1.exercise_09_odd_index_positions()
        results = l1.exercise_10_print_list_in_reverse_order()

        results = l2.exercise_11_reverse_string()
        results = l2.exercise_12_count_vowels_consonants()
        results = l2.exercise_13_count_total_digits()
        results = l2.exercise_14_reverse_integer_number()
        results = l2.exercise_15_find_largest_smallest()
        results = l2.exercise_16_check_for_palindrome()
        results = l2.exercise_17_find_factorial()
        results = l2.exercise_18_collatz_conjecture()
        results = l2.exercise_19_armstrong_number_check()
        results = l2.exercise_20_print_number_pattern()

        results = l4.exercise_39_flatten_list()
        results = l4.exercise_40_nested_list_search()

        print("\nLoop Exercises - end")
        pass