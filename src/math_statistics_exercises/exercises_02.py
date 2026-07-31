import logging
from pathlib import Path
import math
from src.common_library import helper_functions as hf

#
# https://pynative.com/python-math-statistics-exercises/
# Exercises 11 through 20
#


logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)



#########################################################################################
def exercise_11_fibonacci_golden_ratio():
    """
    Exercise 11: nth Fibonacci Using the Golden Ratio
    Problem Statement:
        Write a Python function that computes the nth
        Fibonacci number using Binet’s formula, which involves
        math.sqrt() and the golden ratio, then verifies the
        results against the traditional iterative approach
        for the first 15 terms.
    Purpose:
        Binet’s formula is a striking example of how a
        purely integer sequence (Fibonacci numbers) can be
        computed using irrational numbers (the golden ratio
        and square roots). It also demonstrates the practical
        limits of floating-point arithmetic – the formula works
        perfectly for small n but accumulates rounding error
        for large n, making it an excellent case study in
        numerical precision trade-offs.
    Given Input:
        Compute Fibonacci numbers for n from 0 to 14.
    Expected Output:
        A table comparing the golden ratio formula result
        and the iterative result for each n, confirming
        they match for small values.
    """
    logger.info(f"Exercise 11: nth Fibonacci Using the Golden Ratio")
    pass



#########################################################################################
def exercise_12_exp_log_tests():
    """
    Exercise 12: Verifying exp() and log() Are Inverses
    Problem Statement:
        Write a Python program that uses math.exp() and
        math.log() to verify that exp(log(x)) == x and
        log(exp(x)) == x for several test values, using
        math.isclose() for the comparison.
    Purpose:
        Understanding that exp and log are inverse functions
        is foundational for solving exponential equations,
        working with growth and decay models, and
        understanding how neural network activation functions
        relate to their loss functions. Verifying mathematical
        identities in code also reinforces the habit of
        testing assumptions rather than trusting them
        implicitly.
    Given Input:
        Test values [1, 2, 10, 0.5, 100, math.e]
    Expected Output:
        A table showing exp(log(x)) and log(exp(x)) for each test
        value, with a verification flag confirming both
        round-trips recover the original.
    """
    logger.info(f"Exercise 12: Verifying exp() and log() Are Inverses")
    pass



#########################################################################################
def exercise_13_degrees_to_dms_converter():
    """
    Exercise 13: Degrees to DMS Converter
    Problem Statement:
        Write a Python function that converts a decimal degree
        value into degrees, minutes, and seconds (DMS) format
        using math.floor() and math.modf(), then formats the
        output as a standard geographic coordinate string.
    Purpose:
        DMS notation is the standard format for geographic
        coordinates in GPS devices, aviation, cartography, and
        astronomy. Converting between decimal degrees and DMS
        is a practical exercise in decomposing a float into its
        integer and fractional parts, which is exactly what
        math.modf() is designed for.
    Given Input:
        decimal_degrees = 45.8833 (representing a latitude or longitude)
    Expected Output:
        45.8833° = 45° 52' 59.88"
    """
    logger.info(f"Exercise 13: Degrees to DMS Converter")
    pass



#########################################################################################
def exercise_14_perfect_square_check():
    """
    Exercise 14: Perfect Square Checker Using math.isqrt()
    Problem Statement:
        Write a Python function that uses math.isqrt() to check
        whether a given positive integer is a perfect square,
        then tests it against a range of values and prints
        which ones qualify.
    Purpose:
        Perfect square detection appears in number theory
        puzzles, competitive programming, cryptographic
        primality tests, and grid-layout algorithms (e.g.
        determining whether n items can be arranged in a
        square grid). Using math.isqrt() instead of math.sqrt()
        avoids floating-point rounding errors that can cause
        int(math.sqrt(n))**2 == n to return incorrect results
        for large perfect squares.
    Given Input:
        Test integers from 1 to 30, then verify specific large values.
    Expected Output:
        A list of perfect squares in the range 1-30 and a
        verification result for large numbers like 999999999999999999.
    """
    logger.info(f"Exercise 14: Perfect Square Checker")
    pass



#########################################################################################
def exercise_15_product_of_prime_numbers():
    """
    Exercise 15: Product of All Primes Below 30
    Problem Statement:
        Write a Python program that identifies all prime numbers
        below 30, then uses math.prod() to compute their product
        (the primorial), and prints both the list of primes and
        the final result.
    Purpose:
        math.prod() was introduced in Python 3.8 as a clean,
        readable counterpart to the built-in sum() function,
        replacing verbose functools.reduce() or manual loop
        patterns for multiplicative aggregation. This exercise
        pairs it with a prime sieve to demonstrate how
        functional tools compose naturally with number theory
        operations used in cryptography, hashing,
        and combinatorics.
    Given Input:
        All prime numbers below 30.
    Expected Output:
        Primes below 30: [2, 3, 5, 7, 11, 13, 17, 19, 23, 29] and
        Primorial (product): 6469693230
    """
    logger.info(f"Exercise 15: Product of All Primes Below 30")
    pass



#########################################################################################
def exercise_16_mean_median_mode():
    """
    Exercise 16: Mean, Median, and Mode of Exam Scores
    Problem Statement:
        Write a Python program that takes a list of exam scores
        and uses the statistics module to compute the mean,
        median, and mode, then prints a formatted summary.
    Purpose:
        Mean, median, and mode are the three measures of central
        tendency that appear in every branch of data analysis.
        Using Python’s built-in statistics module produces
        accurate results without external dependencies, making
        it the right choice for lightweight scripts, educational
        tools, and situations where NumPy or pandas would
        be overkill.
    Given Input:
        scores = [72, 85, 90, 88, 76, 95, 85, 60, 72, 85, 91, 78]
    Expected Output:
        Mean: 81.42, Median: 85.0, Mode: 85
    """
    logger.info(f"Exercise 16: Mean, Median, and Mode of Exam Scores")
    pass



#########################################################################################
def exercise_17_sample_standard_deviation_test():
    """
    Exercise 17: Sample vs Population Standard Deviation
    Problem Statement:
        Write a Python program that computes both statistics.stdev()
        (sample standard deviation) and statistics.pstdev()
        (population standard deviation) on the same dataset,
        prints both values, and explains when each should
        be used.
    Purpose:
        Choosing between sample and population standard deviation
        is one of the most common statistical mistakes made by
        programmers. Using the wrong one leads to either
        underestimating or overestimating the spread of data, which
        has real consequences in machine learning feature scaling,
        quality control, A/B testing, and scientific reporting.
    Given Input:
        temperatures = [22.1, 24.5, 19.8, 23.3, 25.0, 21.7, 20.4, 26.1, 23.8, 22.9]
    Expected Output:
        Sample stdev: 1.99 and
        Population pstdev: 1.89
    """
    logger.info(f"Exercise 17: Sample vs Population Standard Deviation")
    pass



#########################################################################################
def exercise_18_variance_of_temperatures():
    """
    Exercise 18: Variance of Temperatures
    Problem Statement:
        Write a Python program that computes the variance of a
        list of daily temperature readings using statistics.variance(),
        then uses the result to identify which readings fall
        more than one standard deviation from the mean.
    Purpose:
        Variance quantifies how spread out a dataset is around
        its mean. It is a foundational metric in quality control,
        financial risk modelling, weather analysis, and machine
        learning (where high variance in a model signals
        overfitting). Extending the exercise to flag outliers
        bridges the gap between computing a statistic and
        applying it to a real decision.
    Given Input:
        temperatures = [18.5, 21.0, 19.3, 35.2, 20.1, 17.8
                        , 22.4, 16.9, 21.7, 34.8, 20.5, 19.0]
    Expected Output:
        Variance, standard deviation, and a list of readings
        flagged as outliers (more than one standard deviation
        from the mean).
    """
    logger.info(f"Exercise 18: Variance of Temperatures")
    pass



#########################################################################################
def exercise_19_median_low_median_high():
    """
    Exercise 19: median_low() and median_high()
    Problem Statement:
        Write a Python program that applies statistics.median_low()
        and statistics.median_high() to an even-length dataset,
        compares their results with the standard statistics.median(),
        and explains when each variant is the appropriate choice.
    Purpose:
        When a dataset has an even number of values, the standard
        median is the average of the two middle elements – which may
        not itself be a value in the dataset. In contexts such as
        reporting a real measurement, selecting a representative
        record from a database, or choosing a salary benchmark from
        actual payroll data, median_low() and median_high() ensure
        the result is always a genuine data point.
    Given Input:
        response_times = [120, 135, 98, 150, 112, 143, 107
                        , 160, 125, 138] (10 values – even length)
    Expected Output:
        median: 131.5, median_low: 125, median_high: 138
    """
    logger.info(f"Exercise 19: median_low() and median_high()")
    pass



#########################################################################################
def exercise_20_find_all_modes():
    """
    Exercise 20: Finding All Modes with multimode()
    Problem Statement:
        Write a Python program that creates a dataset containing
        multiple repeated values and uses statistics.multimode()
        to find all modes, then demonstrates how the result
        differs from statistics.mode() when there are ties.
    Purpose:
        Real-world datasets are frequently multimodal – think of
        survey responses clustered at two popular options, or sales
        data peaking in two different regions. statistics.multimode()
        was introduced in Python 3.8 specifically to handle tie
        cases that mode() either misses or handles ambiguously,
        making it essential for accurate frequency analysis.
    Given Input:
        survey_responses = [3, 5, 2, 4, 5, 3, 1, 5, 2, 3, 4, 2, 5, 3, 1, 4, 2, 3]
    Expected Output:
        multimode: [3, 2, 5] (or the modes in order of first appearance)
        and a frequency count confirming the tie.
    """
    logger.info(f"Exercise 20: Finding All Modes with multimode()")
    pass

