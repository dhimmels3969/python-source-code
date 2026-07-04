from common_library.helper_functions import is_prime_number
from common_library.real_python_timer import Timer, ContextManagerTimer
from src.common_library import helper_functions as hf
from src.common_library import real_python_timer as rptimer
import time
import timeit
from collections import defaultdict, deque
import sys
import itertools
import requests
import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
#
# Info on timeit found at https://www.learnbyexample.org/timeit-module-to-measure-execution-time-in-python/
#
#
#

myCounter = 0

##############################################################################
#### Following code verified: 2026-06-21
##############################################################################

my_code = f""" 
total = 0
for i in range(500):
   total += 1   
"""
def timer_test_number_01():
    # by default timeit executes one million time unless you specify a number value
    # example, number = 100
    time_taken = timeit.timeit(my_code, globals=globals())
    logger.info(f"Basic Timer Test: Code outside function.")
    logger.info(f"  --------------------------------------------------------------------------")
    logger.info(f"  ==========>>>>  Total time taken: {time_taken:,.6f} seconds.")
    logger.info(f"  --------------------------------------------------------------------------")
    pass
##############################################################################



def calculate_sum_via_loop(number):
    total = 0
    for i in range(number+1):
        total += 1
    return ""

def calculate_sum_direct(number):
    total = (number * (number + 1)) / 2
    return ""

def timer_test_number_02(sum_, tests_):
    # by default timeit executes one million time unless you specify a number value
    # example, number = 100
    # number_tests = 25000
    # number_to_sum = 100
    number_tests = tests_
    number_to_sum = sum_
    code = f"calculate_sum_via_loop({number_to_sum})"
    time_taken = timeit.timeit(code, globals=globals(), number=number_tests)
    logger.info(f"Basic Timer Test #2: Separate function. Number to sum: {number_to_sum}, Number of tests: {number_tests}")
    logger.info(f"  --------------------------------------------------------------------------")
    logger.info(f"  ==========>>>>  Total time taken: {time_taken:,.6f} seconds.")
    logger.info(f"  ==========>>>>  Average time per execution: {time_taken/number_tests} ")
    logger.info(f"  --------------------------------------------------------------------------")
    logger.info("")
    pass
##############################################################################


def my_function_03():
    results = ""
    for i in range(3):
        response = requests.get("https://api.github.com/users/dhimmels3969")
        results = response.status_code
    return results

def timer_test_number_03():
    # by default timeit executes one million time unless you specify a number value
    # example, number = 100
    number_tests = 5
    time_taken = timeit.repeat("my_function_03()"
                               ,  setup='import requests'
                               , globals=globals()
                               , repeat = 4
                               , number=number_tests)
    logger.info("")
    logger.info(f"Basic Timer Test #3: Timeit Repeat using API requests.")
    logger.info(f"  --------------------------------------------------------------------------")
    logger.info(f"  Total time taken: {time_taken}")
    logger.info(f"  --------------------------------------------------------------------------")
    pass
##############################################################################



##############################################################################
def timer_test_number_04(sum_, tests_, repeat_):
    """
    Compare two methods of summing numbers: loop vs direct calculation (n * (n+1))/2
    number to sum: user-specified
    number of tests: 1_000_000
    repeat: 10
    """

    # by default timeit executes one million time unless you specify a number value
    # example, number = 100
    # number_tests = 25000
    # number_to_sum = 100
    logger.info(f"Basic Timer Test #4: Sum Calculation Comparisons")
    number_tests = tests_
    number_to_sum = sum_
    code = f"calculate_sum_via_loop({number_to_sum})"
    time_taken = timeit.repeat(code
                               , globals=globals()
                               , repeat = repeat_
                               , number=number_tests)
    logger.info(f"  --------------------------------------------------------------------------")
    logger.info(f"  Method: {code}")
    logger.info(f"  Number to sum: {number_to_sum}")
    logger.info(f"  Number of tests per round: {number_tests}")
    logger.info(f"  Number of repeats: {repeat_}")
    logger.info(f"  Total time taken: {time_taken}")
    logger.info(f"  --------------------------------------------------------------------------")
    logger.info("")


    code = f"calculate_sum_direct({number_to_sum})"
    time_taken = timeit.repeat(code
                               , globals=globals()
                               , repeat = repeat_
                               , number=number_tests)
    logger.info(f"  --------------------------------------------------------------------------")
    logger.info(f"  Method: {code}")
    logger.info(f"  Number to sum: {number_to_sum}")
    logger.info(f"  Number of tests per round: {number_tests}")
    logger.info(f"  Number of repeats: {repeat_}")
    logger.info(f"  Total time taken: {time_taken}")
    logger.info(f"  --------------------------------------------------------------------------")
    logger.info("")

    pass


##############################################################################
def perf_counter_test_number_01(sum_, tests_, repeat_):
    tic = time.perf_counter()
    calculate_sum_via_loop(sum_)
    toc = time.perf_counter()
    logger.info(f"  --------------------------------------------------------------------------")
    logger.info(f"  perf_counter testing - basic functionality")
    logger.info(f"  Sum first {sum_:,} numbers... completed in {toc - tic:0.6f} seconds")
    logger.info(f"  --------------------------------------------------------------------------")
    logger.info("")
    pass


##############################################################################
def perf_counter_test_number_02(sum_, tests_, repeat_):
    myTimer = rptimer.Timer_orig(text="[02] From the Timer_orig class... Elapsed time: {:0.6f} seconds"
                                 , logger=logging.warning)
    myTimer.start()
    calculate_sum_via_loop(sum_)
    elapsedTime = myTimer.stop()
    logger.info(f"  --------------------------------------------------------------------------")
    logger.info(f"  perf_counter_test_number_02 - move timer to a class")
    logger.info(f"  Sum first {sum_:,} numbers... completed in {elapsedTime:0.6f} seconds")
    logger.info(f"  --------------------------------------------------------------------------")
    logger.info("")
    pass



##############################################################################
def perf_counter_test_number_03(sum_, tests_, repeat_):
    myTimer = rptimer.Timer(name = "test_number_03"
                                 , text="[03] From the timer class... Elapsed time: {:0.6f} seconds"
                                 , logger=logging.warning)
    logger.info(f"--------------------------------------------------------------------------")
    logger.info(f"perf_counter_test_number_03 - enhanced timer class")
    for i in range(tests_ + 1):
        myTimer.start()
        calculate_sum_via_loop(sum_)
        elapsedTime = myTimer.stop()
        # logger.info(f"  --------------------------------------------------------------------------")
        # logger.info(f"  perf_counter testing - move timer to a class")
        # logger.info(f"  Sum first {sum_:,} numbers... completed in {elapsedTime:0.6f} seconds")
        # logger.info(f"  --------------------------------------------------------------------------")
        # logger.info("")
    # after completion of all tests accumulated elapsed time will reside in a dictionary within
    # the timer object.

    logger.info(f"  Elapsed time for all tests: {myTimer.timers['test_number_03']:0.6f} seconds")
    logger.info(f"--------------------------------------------------------------------------")
    logger.info("")
    pass



##############################################################################
def perf_counter_test_number_04(sum_, tests_, repeat_):
    myTimer = rptimer.ContextManagerTimer(name = "test_number_04"
                                 , text="[04] Timer as Context Manager... Elapsed time: {:0.6f} seconds"
                                 , logger=logging.warning)
    logger.info(f"--------------------------------------------------------------------------")
    logger.info(f"perf_counter_test_number_04 - timer as context manager")
    for i in range(tests_ + 1):
        with myTimer:
            calculate_sum_via_loop(sum_)

    # after completion of all tests accumulated elapsed time will reside in a dictionary within
    # the timer object.

    logger.info(f"  Elapsed time for all tests: {myTimer.timers['test_number_04']:0.6f} seconds")
    logger.info(f"--------------------------------------------------------------------------")
    logger.info("")
    pass



##############################################################################

@rptimer.ContextManagerTimer(name = "test_number_05"
                                 , text="[05] Timer as Decorator... Elapsed time: {:0.6f} seconds"
                                 , logger=logging.warning)
def time_loops_test_number_05(sum_):
    calculate_sum_via_loop(sum_)
    return None

def perf_counter_test_number_05(sum_, tests_, repeat_):
    myTimer = rptimer.ContextManagerTimer(name = "test_number_05"
                                 , text="[05] Timer as Decorator... Elapsed time: {:0.6f} seconds"
                                 , logger=logging.warning)
    logger.info(f"--------------------------------------------------------------------------")
    logger.info(f"perf_counter_test_number_05 - timer as decorator")

    for i in range(tests_ + 1):
        time_loops_test_number_05(sum_)
    # after completion of all tests accumulated elapsed time will reside in a dictionary within
    # the timer object.

    # logger.info(f"  Elapsed time for all tests: {myTimer.timers['test_number_05']:0.6f} seconds")
    logger.info(f"--------------------------------------------------------------------------")
    logger.info("")
    pass

