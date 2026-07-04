import logging
import concurrent.futures as futures

import constants
from src.common_library import helper_functions as hf
from src.loop_exercises import exercises as l1
from src.loop_exercises import exercises_02 as l2
from src.loop_exercises import exercises_02 as l2
from src.loop_exercises import exercises_03 as l3
from src.loop_exercises import exercises_04 as l4
from timers_and_timing_tests.driver import logger


logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

class Driver():

    """
    Driver Class

    Implements run function which executes multiple functions in the loop_exercises folder.

    TODO:
        Set up a dictionary to control which function gets executed and which functions get bypassed.
    """
    def __init__(self, userInput):
        self.parms = hf.parse_kwargs(userInput)
        pass

    def run(self, **kwargs):
        if self.parms["run"] == "False":
            logger.info("Skipping the Loop Exercises module...")
        else:
            logger.info(constants.THREE_BLANK_LINES)
            logger.info("#####################################################")
            logger.info("Loop Exercises - 1 through 10")
            logger.info("#####################################################")
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

            logger.info("")
            logger.info("#####################################################")
            logger.info("Loop Exercises - 11 through 20")
            logger.info("#####################################################")
            results = l2.exercise_11_reverse_string()
            results = l2.exercise_12_count_vowels_consonants()
            logger.info("")
            results = l2.exercise_13_count_total_digits(75869)
            results = l2.exercise_13_count_total_digits(100000)
            results = l2.exercise_13_count_total_digits(1000000)
            logger.info("")
            results = l2.exercise_14_reverse_integer_number()
            results = l2.exercise_14_reverse_integer_number(15876)
            results = l2.exercise_15_find_largest_smallest()
            results = l2.exercise_16_check_for_palindrome(12321)
            results = l2.exercise_16_check_for_palindrome(8675309)
            results = l2.exercise_17_find_factorial()
            results = l2.exercise_18_collatz_conjecture()
            results = l2.exercise_18_collatz_conjecture(100)


            results = l2.exercise_19_armstrong_number_check()
            results = l2.exercise_20_print_number_pattern()

            logger.info("")
            logger.info("#####################################################")
            logger.info("Loop Exercises - 21 through 30")
            logger.info("#####################################################")
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

            logger.info("")
            logger.info("#####################################################")
            logger.info("Loop Exercises - 31 through 40")
            logger.info("#####################################################")

            results = l4.exercise_31_segregate_items_in_list()
            results = l4.exercise_32_list_rotation()
            results = l4.exercise_33_word_frequency_counter()
            results = l4.exercise_34_fibonacci_series()
            results = l4.exercise_35_perfect_number_check()
            logger.info(results)
            # results = l4.exercise_35_check_perfect_numbers_collection(1, 25000)
            results = l4.exercise_35_check_perfect_numbers_collection(28, 28)

            results = l4.exercise_36_binary_decimal_conversion()
            results = l4.exercise_36_binary_decimal_conversion("11000000")
            results = l4.exercise_37_display_prime_numbers()
            results = l4.exercise_38_find_sum_of_series()
            results = l4.exercise_39_flatten_list()
            results = l4.exercise_40_nested_list_search()

            logger.info("#####################################################")
            logger.info("Loop Exercises - END")
            logger.info("#####################################################")
            logger.info("")
        pass