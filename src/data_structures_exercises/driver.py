from src.common_library import helper_functions as hf
from src.data_structures_exercises import exercises as ds1
import constants
import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)


class Driver():

    """
    Driver Class

    Implements run function which executes multiple functions in
        the data_structures_exercises folder.

    TODO:
        Set up a dictionary to control which function gets executed and which functions get bypassed.
    """
    def __init__(self, userInput):
        self.parms = hf.parse_kwargs(userInput)
        self._name = "Data Structures Exercises"
        pass

    def run(self):
        if self.parms["run"] == "False":
            logger.info(f"Skipping the {self._name} module...\n")
        else:
            logger.info(constants.THREE_BLANK_LINES)
            logger.info("#####################################################")
            logger.info("Data Structure Exercises - 1 through 10")
            logger.info("#####################################################")
            results = ds1.exercise_01_build_output_list_from_two_input_lists()
            results = ds1.exercise_02_add_to_remove_from_list()
            results = ds1.exercise_03_slice_list()
            results = ds1.exercise_04_count_occurrences()
            results = ds1.exercise_05_build_swt_from_paired_elements()
            results = ds1.exercise_06_set_intersection_and_removal()
            results = ds1.exercise_07_subset_superset_test()
            results = ds1.exercise_08_filter_list_against_dictionary()
            results = ds1.exercise_09_unique_dictionary_values()
            results = ds1.exercise_10_remove_duplicates_from_list()
            logger.info(constants.THREE_BLANK_LINES)

        pass



