import logging

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