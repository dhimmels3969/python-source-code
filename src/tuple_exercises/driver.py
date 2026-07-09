from src.common_library import helper_functions as hf
from src.tuple_exercises import exercises as tuple_01
from src.tuple_exercises import exercises_02 as tuple_02
import constants
import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

#
# Exercises found at web page https://pynative.com/python-tuple-exercise-with-solutions/
#

class Driver():

    """
    Driver Class

    Implements run function which executes multiple functions in the tuple_exercises folder.

    TODO:
        Set up a dictionary to control which function gets executed and which functions get bypassed.
    """
    def __init__(self, userInput):
        self.parms = hf.parse_kwargs(userInput)
        self._name = f"Tuple Exercises"
        pass

    def run(self):
        if self.parms["run"] == "False":
            logger.info(f"Skipping the {self._name} module...\n")
        else:
            logger.info(constants.THREE_BLANK_LINES)
            logger.info("#####################################################")
            logger.info(f"{self._name} - 1 through 12")
            logger.info("#####################################################")
            results = tuple_01.exercise_01_tuple_basics_check()
            results = tuple_01.exercise_02_trailing_comma_check()
            results = tuple_01.exercise_03_tuple_repetition()
            results = tuple_01.exercise_04_tuple_concatenation()
            results = tuple_01.exercise_05_tuple_slicing()
            results = tuple_01.exercise_06_tuple_reversal()
            results = tuple_01.exercise_07_type_casting()
            results = tuple_01.exercise_08_tuple_to_string()
            results = tuple_01.exercise_09_tuple_membership_test()
            results = tuple_01.exercise_10_counting_test()
            results = tuple_01.exercise_11_tuple_unpacking()
            results = tuple_01.exercise_12_swap_values()
    
    
            logger.info("")
            logger.info("#####################################################")
            logger.info(f"{self._name} - 13, 14, 22 through 32")
            logger.info("#####################################################")
            results = tuple_02.exercise_13_nested_tuple_access()
            results = tuple_02.exercise_14_tuple_stats_check()
            results = tuple_02.exercise_22_tuple_sort_check()
            results = tuple_02.exercise_23_tuple_filtering()
            results = tuple_02.exercise_24_tuple_mapping()
            results = tuple_02.exercise_25_tuple_dictionary_mapping()
            results = tuple_02.exercise_26_tuple_intersection()
            results = tuple_02.exercise_27_modification_hack_test()
            results = tuple_02.exercise_28_tuple_mutability_check()
            results = tuple_02.exercise_29_flatten_nested_tuples()
            results = tuple_02.exercise_30_memory_efficiency_check()
            results = tuple_02.exercise_31_named_tuples_test()
            results = tuple_02.exercise_32_tuple_hashability()
    
            logger.info("")
            logger.info("#####################################################")
            logger.info(f"{self._name} - end")
            logger.info("#####################################################\n")

        pass