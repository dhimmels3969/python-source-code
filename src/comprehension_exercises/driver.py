import constants
from src.common_library import helper_functions as hf
from src.comprehension_exercises import exercises as cmp_01
from src.comprehension_exercises import exercises_01 as cmp_02
from src.comprehension_exercises import exercises_02 as cmp_03
import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
#
# Exercises found at web page https://pynative.com/python-file-handling-exercises/
# Driver program to call all methods
#

class Driver:

    """
    Driver Class

    Implements run function which executes multiple functions in the date_time_exercises folder.

    TODO:
        Set up a dictionary to control which function gets executed and which functions get bypassed.
    """
    def __init__(self):
        # pass the root directory to the class for file operations
        pass


    def run(self):
        logger.info(constants.THREE_BLANK_LINES)
        logger.info("#####################################################")
        logger.info("Comprehension Exercises - 1 through 10")
        logger.info("#####################################################")
        results = cmp_01.exercise_01_squares_list()
        results = cmp_01.exercise_02_even_numbers_list()
        results = cmp_01.exercise_03_string_lengths()
        results = cmp_01.exercise_04_uppercase_conversion()
        results = cmp_01.exercise_05_flatten_list()
        results = cmp_01.exercise_06_filter_and_transform()
        results = cmp_01.exercise_07_word_frequency_list()
        results = cmp_01.exercise_08_invert_dictionary()
        results = cmp_01.exercise_09_unique_vowels_list()
        results = cmp_01.exercise_10_square_mapping_check()


        logger.info("")
        logger.info("#####################################################")
        logger.info("Comprehension Exercises - 11 through 20")
        logger.info("#####################################################")
        results = cmp_02.exercise_11_fizzbuzz_comprehension()
        results = cmp_02.exercise_12_matrix_transposition()
        results = cmp_02.exercise_13_cartesian_product()
        results = cmp_02.exercise_14_extract_digits()
        results = cmp_02.exercise_15_nested_filtering()
        results = cmp_02.exercise_16_conditional_dictionary_comprehension()
        results = cmp_02.exercise_17_grouped_dictionary()
        results = cmp_02.exercise_18_common_elements()
        results = cmp_02.exercise_19_character_frequency_set()
        results = cmp_02.exercise_20_lazy_squares()


        logger.info("")
        logger.info("#####################################################")
        logger.info("Comprehension Exercises - 21 through 25")
        logger.info("#####################################################")
        results = cmp_03.exercise_21_fibonacci_generator()
        results = cmp_03.exercise_22_chained_generator_pipeline()
        results = cmp_03.exercise_23_row_parser()
        results = cmp_03.exercise_24_grouped_anagrams()
        results = cmp_03.exercise_25_comprehension_generator_testing()



        logger.info("")
        logger.info("#####################################################")
        logger.info("Object-Oriented Programming - end")
        logger.info("#####################################################\n")

        pass