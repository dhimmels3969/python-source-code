import constants
from src.common_library import helper_functions as hf
from src.exception_handling_exercises import exercises as excp_01
from src.exception_handling_exercises import exercises_02 as excp_02


import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
#
# Exercises found at web page https://pynative.com/python-exception-handling-exercises/
# Driver program to call all methods
#

class Driver:

    """
    Driver Class

    Implements run function which executes multiple functions in the date_time_exercises folder.

    TODO:
        Set up a dictionary to control which function gets executed and which functions get bypassed.
    """
    def __init__(self, root, userInput):
        self.root = root
        self.parms = hf.parse_kwargs(userInput)
        self._name = "Exception Handling Exercises"
        pass


    def run(self):
        if self.parms["run"] == "False":
            logger.info(f"Skipping the {self._name} module...\n")
        else:
            logger.info(constants.THREE_BLANK_LINES)
            logger.info("#####################################################")
            logger.info(f"{self._name} - 1 through 10")
            logger.info("#####################################################")
            results = excp_01.exercise_01_try_except_test()
            results = excp_01.exercise_02_division_error_prevention()
            results = excp_01.exercise_03_file_not_found(self.root)
            results = excp_01.exercise_04_index_out_of_range()
            results = excp_01.exercise_05_key_error_test()
            results = excp_01.exercise_06_type_error_prevention()
            results = excp_01.exercise_07_multiple_exceptions()
            results = excp_01.exercise_08_finally_block_testing(self.root)
            results = excp_01.exercise_09_else_clause_testing()
            results = excp_01.exercise_10_nested_try_except(self.root)

            logger.info("")
            logger.info("#####################################################")
            logger.info(f"{self._name} - 11 through 20")
            logger.info("#####################################################")
            results = excp_02.exercise_11_reraising_exceptions_test()
            results = excp_02.exercise_12_custom_exception_class()
            results = excp_02.exercise_13_exception_chaining()
            results = excp_02.exercise_14_validate_user_input()
            results = excp_02.exercise_15_context_manager_exception_test()
            results = excp_02.exercise_16_exception_hierarchy()
            results = excp_02.exercise_17_logging_exceptions_test()
            results = excp_02.exercise_18_retry_decorator()
            results = excp_02.exercise_19_thread_safe_exception_handling()
            results = excp_02.exercise_20_generator_exception_test()

            logger.info("")
            logger.info("#####################################################")
            logger.info(f"{self._name} - end")
            logger.info("#####################################################\n")

        pass