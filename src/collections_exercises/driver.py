import constants
from src.common_library import helper_functions as hf
from src.collections_exercises import exercises as coll_01
from src.collections_exercises import exercises_01 as coll_02
from src.collections_exercises import exercises_02 as coll_03

import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
#
# Exercises found at web page https://pynative.com/python-collections-module-exercises/
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
        logger.info("Collections Exercises - 1 through 10")
        logger.info("#####################################################")
        results = coll_01.exercise_01_word_frequency_counter()
        results = coll_01.exercise_02_most_common_elements()
        results = coll_01.exercise_03_counter_subtraction()
        results = coll_01.exercise_04_character_frequency_string()
        results = coll_01.exercise_05_counter_addition()
        results = coll_01.exercise_06_group_words_by_first_letter()
        results = coll_01.exercise_07_count_occurrences()
        results = coll_01.exercise_08_build_adjacency_list()
        results = coll_01.exercise_09_nested_defaultdict()
        results = coll_01.exercise_10_use_set_with_default_dict()


        logger.info("")
        logger.info("#####################################################")
        logger.info("Collections Exercises - 11 through 20")
        logger.info("#####################################################")
        results = coll_02.exercise_11_preserve_insertion_order()
        results = coll_02.exercise_12_move_to_end()
        results = coll_02.exercise_13_implement_single_cache()
        results = coll_02.exercise_14_compare_ordered_dicts()
        results = coll_02.exercise_15_reverse_ordered_dict()
        results = coll_02.exercise_16_basic_deque_operations()
        results = coll_02.exercise_17_implement_fifo_queue()
        results = coll_02.exercise_18_implement_stack()
        results = coll_02.exercise_19_rotate_deque()
        results = coll_02.exercise_20_bounded_deque()


        logger.info("")
        logger.info("#####################################################")
        logger.info("Collections Exercises - 21 through 25")
        logger.info("#####################################################")
        results = coll_03.exercise_21_create_namedtuple()
        results = coll_03.exercise_22_namedtuple_lightweight_record()
        results = coll_03.exercise_23_convert_namedtuple_to_dict()
        results = coll_03.exercise_24_replace_field_value()
        results = coll_03.exercise_25_namedtuple_default_values()




        logger.info("")
        logger.info("#####################################################")
        logger.info("Object-Oriented Programming - end")
        logger.info("#####################################################\n")

        pass