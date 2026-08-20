import logging
import math

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)




#########################################################################################
def exercise_31_calculate_series_test():

    def calculate_series(number_, power_):
        """
        This function takes a number number_, calculates the number_ raised to each power
          from 0 to power_, and sums the values finally returning the results to the
          calling function.
          For example with number 8 and exponent 5 we will calculate
            results = 8^5 + 8^4 + 8^3 + 8^2 + 8^1 + 8^0
          or more generally
            x^n + x^(n-1) + ... + x^0

        :param number_: number to multiply
        :type number_:  int
        :param power_:  exponent
        :type power_:   int
        :return:
        :rtype:
        """
        if power_ == 0:
            return 1
        else:
            power_ -= 1
            return (calculate_series(number_, power_) * number_ ) + 1


    results = calculate_series(8, 5)
    logger.info("-----------------------------------------------------------")
    logger.info(f"Results of series calculation(8, 5): {calculate_series(8, 5):,}")
    logger.info(f"Results of series calculation(12,4): {calculate_series(12, 4):,}")
    logger.info(f"Results of series calculation(25,3): {calculate_series(25, 3):,}")
    logger.info(f"Results of series calculation(25,4): {calculate_series(25, 4):,}")
    logger.info(f"Results of series calculation(13,16): {calculate_series(13, 16):,}")
    logger.info(f"Results of series calculation(130,16): {calculate_series(130, 16):,}")
    logger.info(f"Results of series calculation(2,31): {calculate_series(2, 31):,}")

    pass


#########################################################################################
def exercise_32_square_root_four_consecutive_numbers_plus_one():
    """
    """

    def calculate_answer(x):
        """
        This function performs the following calculation:
            multiply four consecutive numbers together (example 4*5*6*7)
            add one
            the square root of the above results will always be a perfect square
            and is equivalent to x**2 + 3x + 1

        :param x: first number in the series
        :type x:  int
        :return:
        :rtype:
        """

        # calculate the answer manually
        message = f"Square root of ({x}*{x+1}*{x+2}*{x+3})+1"
        number_calculate_manually = math.sqrt(((x * (x+1) * (x+2) * (x+3)) + 1))
        expected_answer = math.pow(x, 2) + x*3 + 1
        return number_calculate_manually, expected_answer, message

    def display_results(x):
        results_of_calculation = calculate_answer(x)
        message = f"{results_of_calculation[2]} = {results_of_calculation[0]:,.0f}"
        return message

    logger.info("")
    logger.info("-----------------------------------------------------------")
    logger.info(f"  {display_results(50)}")
    logger.info(f"  {display_results(1000)}")
    logger.info(f"  {display_results(2500)}")
    pass