import constants
from src.common_library import helper_functions as hf
from src.timers_and_timing_tests import timers_poc as poc
import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
#
# Code samples pertaining to timing and performance measurement.
#   timeit - https://www.learnbyexample.org/timeit-module-to-measure-execution-time-in-python/
#   perf_counter - https://realpython.com/python-timer/
#
# Driver program to call all methods
#

class Driver:

    """
    Driver Class

    Implements run function which executes multiple functions in the date_time_exercises folder.

    TODO:
        Set up a dictionary to control which function gets executed and which functions get bypassed.
    """
    def __init__(self, userInput):
        self.parms = hf.parse_kwargs(userInput)
        self._name = "Timers - Testing and Proof of Concept"
        pass


    def run(self):
        if self.parms["run"] == "False":
            logger.info(f"Skipping the {self._name} module...\n")
        else:
            logger.info(constants.THREE_BLANK_LINES)
            logger.info("#####################################################")
            logger.info(f"{self._name} - Start")
            logger.info("#####################################################")
            results = poc.timer_test_number_01()
            results = poc.timer_test_number_02(100, 25_000)
            results = poc.timer_test_number_02(1_000, 25_000)
            results = poc.timer_test_number_02(10_000, 25_000)
            results = poc.timer_test_number_03()
            results = poc.timer_test_number_04(10_000, 250_000, 5)

            results = poc.perf_counter_test_number_01(1_000, 0, 0)
            results = poc.perf_counter_test_number_01(1_000_000, 0, 0)
            results = poc.perf_counter_test_number_01(10_000_000, 0, 0)
            results = poc.perf_counter_test_number_02(100_000, 0, 0)
            results = poc.perf_counter_test_number_03(100_000, 8, 0)
            results = poc.perf_counter_test_number_04(100_000, 10, 0)
            results = poc.perf_counter_test_number_05(100_000, 3, 0)

            logger.info("")
            logger.info("#####################################################")
            logger.info(f"{self._name} - End")
            logger.info("#####################################################\n")

        pass