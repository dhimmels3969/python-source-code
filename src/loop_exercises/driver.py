
from src.common_library import helper_functions as hf
import loop_exercises.exercises as l1
import loop_exercises.exercises_02 as l2
import loop_exercises.exercises_03 as l3
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
        print("#####################################################")
        print("Loop Exercises - 1 through 10")
        print("#####################################################")

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

        print("")
        print("#####################################################")
        print("Loop Exercises - 11 through 20")
        print("#####################################################")
        results = l2.exercise_11_reverse_string()
        results = l2.exercise_12_count_vowels_consonants()
        print("")
        results = l2.exercise_13_count_total_digits(75869)
        results = l2.exercise_13_count_total_digits(100000)
        results = l2.exercise_13_count_total_digits(1000000)
        print("")
        results = l2.exercise_14_reverse_integer_number()
        results = l2.exercise_14_reverse_integer_number(15876)
        results = l2.exercise_15_find_largest_smallest()
        results = l2.exercise_16_check_for_palindrome(12321)
        results = l2.exercise_16_check_for_palindrome(8675309)
        results = l2.exercise_17_find_factorial()
        results = l2.exercise_18_collatz_conjecture()
        results = l2.exercise_19_armstrong_number_check()
        results = l2.exercise_20_print_number_pattern()

        print("")
        print("#####################################################")
        print("Loop Exercises - 21 through 30")
        print("#####################################################")
        results = l3.exercise_21_reverse_number_pattern()
        results = l3.exercise_22_alternate_numbers_pattern()
        results = l3.exercise_23_alphabet_pyramid_pattern()
        # results = l3.exercise_23_alphabet_pyramid_pattern(11)
        results = l3.exercise_24_hollow_square_pattern()
        results = l3.exercise_25_pyramid_star_pattern()
        results = l3.exercise_26_full_multiplication_table()
        results = l3.exercise_27_list_cumulative_sums()
        results = l3.exercise_28_filter_dictionary()
        results = l3.exercise_29_identify_common_elements()
        results = l3.exercise_30_remove_duplicates()

        print("")
        print("#####################################################")
        print("Loop Exercises - 31 through 40")
        print("#####################################################")

        results = l4.exercise_31_segregate_items_in_list()
        results = l4.exercise_32_list_rotation()
        results = l4.exercise_33_word_frequency_counter()
        results = l4.exercise_34_fibonacci_series()
        results = l4.exercise_35_perfect_number_check()
        results = l4.exercise_36_binary_decimal_conversion()
        results = l4.exercise_37_display_prime_numbers()
        results = l4.exercise_38_find_sum_of_series()
        results = l4.exercise_39_flatten_list()
        results = l4.exercise_40_nested_list_search()

        print("\nLoop Exercises - end")
        pass