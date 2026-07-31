import constants
from src.common_library import helper_functions as hf
from src.math_statistics_exercises import exercises as math_01
from src.math_statistics_exercises import exercises_02 as math_02
from src.math_statistics_exercises import exercises_03 as math_03

import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
#
# Exercises found at web page https://pynative.com/python-math-statistics-exercises/
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
        self._name = "Math and Statistics Exercises"
        pass


    def run(self):
        if self.parms["run"] == "False":
            logger.info(f"Skipping the {self._name} module...\n")
        else:
            logger.info(constants.THREE_BLANK_LINES)
            logger.info("#####################################################")
            logger.info(f"{self._name} - 1 through 10")
            logger.info("#####################################################")
            results = math_01.exercise_01_square_root_and_power()
            results = math_01.exercise_02_area_of_circle()
            results = math_01.exercise_03_factorial_computation_test()
            results = math_01.exercise_04_floor_and_ceiling_test()
            results = math_01.exercise_05_greatest_common_divisor()
            results = math_01.exercise_06_hypotenuse_of_right_triangle()
            results = math_01.exercise_07_logarithms_tests()
            results = math_01.exercise_08_degrees_to_radians_conversion()
            results = math_01.exercise_09_combinations_and_permutations()
            results = math_01.exercise_10_floating_point_precision()

            logger.info("")
            logger.info("#####################################################")
            logger.info(f"{self._name} - 11 through 20")
            logger.info("#####################################################")
            results = math_02.exercise_11_fibonacci_golden_ratio()
            results = math_02.exercise_12_exp_log_tests()
            results = math_02.exercise_13_degrees_to_dms_converter()
            results = math_02.exercise_14_perfect_square_check()
            results = math_02.exercise_15_product_of_prime_numbers()
            results = math_02.exercise_16_mean_median_mode()
            results = math_02.exercise_17_sample_standard_deviation_test()
            results = math_02.exercise_18_variance_of_temperatures()
            results = math_02.exercise_19_median_low_median_high()
            results = math_02.exercise_20_find_all_modes()

            logger.info("")
            logger.info("#####################################################")
            logger.info(f"{self._name} - 21 through 25")
            logger.info("#####################################################")
            results = math_03.exercise_21_quartiles_testing()
            results = math_03.exercise_22_harmonic_mean_testing()
            results = math_03.exercise_23_geometric_mean_for_compound_growth()
            results = math_03.exercise_24_covariance_testing()
            results = math_03.exercise_25_pearson_correlation_coefficient()
            results = math_03.exercise_26_probability_with_normal_distribution()
            results = math_03.exercise_27_distribution_overlap()
            results = math_03.exercise_28_grading_curve_with_normal_distribution()
            results = math_03.exercise_29_linear_regression_testing()
            results = math_03.exercise_30_z_score_outlier_detection()

            logger.info("")
            logger.info("#####################################################")
            logger.info(f"{self._name} - end")
            logger.info("#####################################################\n")

        pass