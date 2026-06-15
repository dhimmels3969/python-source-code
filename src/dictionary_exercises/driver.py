from src.common_library import helper_functions as hf
from src.dictionary_exercises import exercises as dict1
from src.dictionary_exercises import exercises_02 as dict2
from src.dictionary_exercises import exercises_03 as dict3
from src.dictionary_exercises import exercises_04 as dict4
import constants
import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

#
# Exercises found at web page https://pynative.com/python-dictionary-exercise-with-solutions/
#

class Driver():

    """
    Driver Class

    Implements run function which executes multiple functions in the list_exercises folder.

    TODO:
        Set up a dictionary to control which function gets executed and which functions get bypassed.
    """
    def __init__(self):
        pass

    def run(self):
        logger.info(constants.THREE_BLANK_LINES)
        logger.info("#####################################################")
        logger.info("Dictionary Exercises - 1 through 10")
        logger.info("#####################################################")
        results = dict1.exercise_01_basic_dictionary_operations()
        results = dict1.exercise_02_dictionary_operations()
        results = dict1.exercise_03_create_dictionary_from_lists()
        results = dict1.exercise_04_clear_dictionary()
        results = dict1.exercise_05_merge_dictionaries()
        results = dict1.exercise_06_access_nested_dictionary()
        results = dict1.exercise_07_access_key_in_nested_dictionary()
        results = dict1.exercise_08_initialize_dictionary_with_default_values()
        results = dict1.exercise_09_rename_key_in_dictionary()
        results = dict1.exercise_10_delete_list_of_keys()


        logger.info("")
        logger.info("#####################################################")
        logger.info("Dictionary Exercises - 11 through 20")
        logger.info("#####################################################")
        results = dict2.exercise_11_check_for_specific_value()
        results = dict2.exercise_12_sum_all_values()
        results = dict2.exercise_13_extract_subset_of_keys()
        results = dict2.exercise_14_map_two_lists()
        results = dict2.exercise_15_count_character_frequencies()
        results = dict2.exercise_16_modify_nested_dictionary()
        results = dict2.exercise_17_update_deeply_nested_key()
        results = dict2.exercise_18_dictionary_comprehension()
        results = dict2.exercise_19_filter_dictionary()
        results = dict2.exercise_20_find_key()

        logger.info("")
        logger.info("#####################################################")
        logger.info("Dictionary Exercises - 21 through 30")
        logger.info("#####################################################")
        results = dict3.exercise_21_find_max_value()
        results = dict3.exercise_22_create_dictionary_from_tuples()
        results = dict3.exercise_23_find_common_keys()
        results = dict3.exercise_24_dictionary_difference()
        results = dict3.exercise_25_dictionary_intersection()
        results = dict3.exercise_26_word_count()
        results = dict3.exercise_27_remove_dictionary_items()
        results = dict3.exercise_28_sort_dictionary_by_keys()
        results = dict3.exercise_29_sort_dictionary_by_values()
        results = dict3.exercise_30_unique_values_check()

        logger.info("")
        logger.info("#####################################################")
        logger.info("Dictionary Exercises - 31 through 40")
        logger.info("#####################################################")
        results = dict4.exercise_31_check_for_subset()
        results = dict4.exercise_32_sort_by_value_length()
        results = dict4.exercise_33_key_with_longest_list()
        results = dict4.exercise_34_convert_dictionary_to_json()
        results = dict4.exercise_35_invert_dictionary()
        results = dict4.exercise_36_invert_with_duplicate_values()
        results = dict4.exercise_37_flatten_nested_dictionary()
        results = dict4.exercise_38_group_by_first_character()
        results = dict4.exercise_39_merge_and_sum_overlapping()
        results = dict4.exercise_40_deep_shallow_copy()
        logger.info("#####################################################")
        logger.info("Dictionary Exercises - end")
        logger.info("#####################################################\n")

        pass