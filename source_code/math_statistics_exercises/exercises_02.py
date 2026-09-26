import itertools
import logging
import statistics
from collections import Counter, defaultdict
from pathlib import Path
import math
from source_code.common_library import helper_functions as hf

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
    def build_expected_fibonacci_list(threshold):
        final_results = []
        fibonacci_results = list(itertools.takewhile(lambda n: n < threshold, hf.fibonacci()))
        final_results.append(1)
        for fibonacci_item in fibonacci_results:
            final_results.append(fibonacci_item)
        return final_results

    logger.info(f"Exercise 11: nth Fibonacci Using the Golden Ratio")
    fibonacci_list = []
    phi = (1 + math.sqrt(5)) / 2

    for n in range(1, 21):
        calculated_answer = round((phi ** n - (-1 / phi) ** n) / math.sqrt(5))
        fibonacci_list.append(calculated_answer)

    # get the first 15 fibonacci numbers using a generator and return in a list
    expected_fibonacci_list = build_expected_fibonacci_list(max(fibonacci_list) + 1)

    # build a list of tuples... in each tuple, the first item is the fibonacci
    # series calculated using the Binet formula, second item is the fibonacci
    # series calculated using a recursive function
    complete_fibonacci_list = list(zip(fibonacci_list, expected_fibonacci_list))
    for item in complete_fibonacci_list:
        logger.info(f"  Binet's Formula: {item[0]}, recursion: {item[1]}")
    logger.info("")
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
    values = [1, 2, 10, 0.5, 100, math.e]
    logger.info(f"{'x':>10} | {'exp(log(x))':>14} | {'log(exp(x))':>14} | {'Both pass':>10}")
    logger.info("-" * 58)

    for value in values:
        exp_of_log = math.exp(math.log(value))
        log_of_exp = math.log(math.exp(value))
        check_1 = math.isclose(exp_of_log, value)
        check_2 = math.isclose(log_of_exp, value)
        logger.info(f"{value:>10.4f} | {exp_of_log:>14.10f} | {log_of_exp:>14.10f} | {str(check_1 and check_2):>10}")

    logger.info("")
    # Highlight the identity visually for x = math.e
    logger.info(f"  Special case: x = math.e = {math.e:.6f}")
    logger.info(f"  log(e)     = {math.log(math.e)}")
    logger.info(f"  exp(log(e))= {math.exp(math.log(math.e))}")
    logger.info(f"  exp(1)     = {math.exp(1):.10f}")

        # exp_value = math.exp(value)
        # # inverse_exp_value = math.log(exp_value)
        # log_value = math.log(exp_value)
        # # inverse_log_value = math.exp(log_value)
        # inverse_relationship = math.isclose(math.exp(math.log(value)), value)
        # logger.info(f"  value: {value:.4f}, exp: {exp_value:.4f}, log: {log_value:.4f}"
        #             f", exp() and log() Are Inverses? {inverse_relationship}")
    logger.info("")
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
    def convert_degrees_to_dms(degrees: float) -> tuple:
        """
        Convert a decimal degree to DMS format.
        :param degrees:  degrees specified by the calling function
        :type degrees:   float
        :return: a formatted string showing degrees, minutes, seconds, and optionally direction
        :rtype:    str
        """
        sign = -1 if degrees < 0 else 1
        degrees = abs(degrees)
        frac_deg, whole_deg = math.modf(degrees)
        resolved_degrees = int(whole_deg)
        frac_min, whole_min = math.modf(frac_deg * 60)
        minutes = int(whole_min)
        seconds = frac_min * 60
        return sign * resolved_degrees, minutes, seconds

    def format_dms(degrees_, minutes_, seconds_, direction=None):
        sign = "-" if degrees_ < 0 else ""
        d = abs(degrees_)
        dir_str = f" {direction}" if direction else ""
        return f"{sign}{d}° {minutes_}' {seconds_:.2f}\"{dir_str}"

    logger.info(f"Exercise 13: Degrees to DMS Converter")
    # Test cases
    requests = [
        (45.8833, "N"),
        (-73.9857, "W"),
        (0.0, "N"),
        (90.0, "N"),
        (51.5074, "N"),  # London latitude
        (-150.3131, "")
    ]
    for val, direction in requests:
        degrees, minutes, seconds = convert_degrees_to_dms(val)
        formatted_results = format_dms(degrees, minutes, seconds, direction)
        logger.info(f"  {val:>10.4f}° = {formatted_results}")
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
    def test_for_perfect_square(number_to_test: int):
        test_using_math_sqrt = (int(math.sqrt(number_to_test)) ** 2 == number_to_test)
        test_using_math_isqrt = (int(math.isqrt(number_to_test)) ** 2 == number_to_test)
        results = (f"Is {number_to_test} a perfect square? using math.sqrt ->{test_using_math_sqrt}, "
                   f" using math.isqrt() ->{test_using_math_isqrt}")
        return results

    logger.info(f"Exercise 14: Perfect Square Checker")
    perfect_squares = []
    threshold = 30
    for n in range(1, threshold+1):
        if int(math.sqrt(n))**2 == n:
            perfect_squares.append(n)
    logger.info(f"  Perfect squares less than {threshold}: {perfect_squares}")
    large_numbers = [
                     999999999999999**2,
                     9999999999999999**2,
                     99999999999999999**2,
                     3**30,
                     3**60,
                     3**100,
                     3**125,
                     111**30
                    ]

    for num in large_numbers:
        logger.info(f"  {test_for_perfect_square(num)}")

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
    prime_list = []
    for n in range(2, 31):
        if hf.is_prime(n):
            prime_list.append(n)
    prime_list_primordial = math.prod(prime_list)
    logger.info(f"  Primes below 30: {prime_list}")
    logger.info(f"  Primorial (product): {prime_list_primordial}")
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
    scores = [72, 85, 90, 88, 76, 95, 85, 60, 72, 85, 91, 78]
    mean_ = statistics.mean(scores)
    median_ = statistics.median(scores)
    mode_ = statistics.mode(scores)
    logger.info(f"  Dataset (sorted) : {sorted(scores)}")
    logger.info(f"  Count            : {len(scores)}")
    logger.info(f"  Mean             : {mean_:.2f}")
    logger.info(f"  Median           : {median_}")
    logger.info(f"  Mode             : {mode_}")
    # Additional context
    logger.info(f"  Min score        : {min(scores)}")
    logger.info(f"  Max score        : {max(scores)}")
    logger.info(f"  Range            : {max(scores) - min(scores)}")
    # Mean vs median: which is more representative?
    logger.info(f"  Mean ({mean_:.2f}) vs Median ({median_})")
    if mean_ < median_:
        logger.info("  Mean < Median: distribution is likely left-skewed.")
    elif mean_ > median_:
        logger.info("  Mean > Median: distribution is likely right-skewed.")
    else:
        logger.info("  Mean == Median: distribution appears symmetric.")
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
    temperatures = [22.1, 24.5, 19.8, 23.3, 25.0, 21.7, 20.4, 26.1, 23.8, 22.9]
    standard_deviation = statistics.stdev(temperatures)
    population_standard_deviation = statistics.pstdev(temperatures)
    variance = statistics.variance(temperatures)
    population_variance = statistics.pvariance(temperatures)
    mean_ = statistics.mean(temperatures)
    logger.info(f"  Dataset (sorted)             : {sorted(temperatures)}")
    logger.info(f"  Count                        : {len(temperatures)}")
    logger.info(f"  Mean                         : {mean_:.2f}")
    logger.info(f"  Sample Standard Deviation    : {standard_deviation:.4f} "
                f"divides by n-1 = {len(temperatures) - 1}")
    logger.info(f"  Population Standard Deviation: {population_standard_deviation:.4f} "
                f"divides by n = {len(temperatures)}")

    # Verify: variance is the square of stdev
    logger.info(f"  Sample variance      : {variance:.4f}")
    logger.info(f"  stdev²               : {standard_deviation ** 2:.4f}  | "
                f"Match: {math.isclose(variance, standard_deviation ** 2)}")
    logger.info(f"  Population variance  : {population_variance:.4f}")
    logger.info(f"  pstdev²              : {population_standard_deviation ** 2:.4f}  | "
                f"Match: {math.isclose(population_variance, population_standard_deviation ** 2)}")
    logger.info("")
    logger.info("  When to use which:")
    logger.info("  stdev / variance   : Use when data is a SAMPLE drawn from a larger population.")
    logger.info("  pstdev / pvariance : Use when data IS the entire population.")
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
    temperatures = [18.5, 21.0, 19.3, 35.2, 20.1, 17.8, 22.4, 16.9, 21.7, 34.8, 20.5, 19.0]
    standard_deviation = statistics.stdev(temperatures)
    population_standard_deviation = statistics.pstdev(temperatures)
    variance = statistics.variance(temperatures)
    population_variance = statistics.pvariance(temperatures)
    mean_ = statistics.mean(temperatures)
    normal = list([temp for temp in temperatures if abs(temp - mean_) <= standard_deviation])
    outliers = list([temp for temp in temperatures if abs(temp - mean_) > standard_deviation])

    logger.info(f"  Standard Deviation: {standard_deviation:.4f} ")

    logger.info(f"  Dataset (sorted)             : {sorted(temperatures)}")
    logger.info(f"  Count                        : {len(temperatures)}")
    logger.info(f"  Mean                         : {mean_:.2f}")
    logger.info(f"  Sample Standard Deviation    : {standard_deviation:.4f} "
                f"divides by n-1 = {len(temperatures) - 1}")
    range_ = f"Normal range (mean ± 1 stdev): [{mean_ - standard_deviation:.2f}, {mean_ + standard_deviation:.2f}]"
    logger.info(f"  {range_}")
    logger.info(f"  Normal readings  : {normal}")
    logger.info(f"  Outlier readings : {outliers}")

    logger.info("  Z-scores (standard deviations from mean):")
    for t in temperatures:
        z = (t - mean_) / standard_deviation
        flag = " <-- outlier" if abs(z) > 1 else ""
        logger.info(f"  {t:5.1f}°C  z = {z:+.2f}{flag}")
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
    response_times = [120, 135, 98, 150, 112, 143, 107, 160, 125, 138]
    mid_low_idx = len(response_times) // 2 - 1
    mid_high_idx = len(response_times) // 2
    logger.info(f"  Response Times (fastest to slowest): {sorted(response_times)}")
    logger.info(f"  Count (n)        : {len(response_times)}  (even-length)")
    logger.info(f"  Two middle values: {sorted(response_times)[mid_low_idx]} (index {mid_low_idx}) and "
          f"{sorted(response_times)[mid_high_idx]} (index {mid_high_idx})")
    median_ = statistics.median(response_times)
    median_low = statistics.median_low(response_times)
    median_high = statistics.median_high(response_times)
    logger.info(f"  Median Low       : {median_low:+.2f}  (average of two middle values - may not be in dataset)")
    logger.info(f"  Median Value     : {median_:+.2f}  (lower middle value - always in dataset)")
    logger.info(f"  Median High      : {median_high:+.2f}  (upper middle value - always in dataset)")
    # Verify median is the average of low and high
    logger.info(f"  Predicted median (median_low + median_high) / 2 = {(median_low + median_high) / 2}")
    logger.info(f"  Equals median()  : {(median_low + median_high) / 2 == median_}")
    # Odd-length example for contrast
    odd_data = response_times[:9]
    logger.info(f"  Odd-length dataset: {sorted(odd_data)}")
    logger.info(f"  median()      : {statistics.median(odd_data)}")
    logger.info(f"  median_low()  : {statistics.median_low(odd_data)}")
    logger.info(f"  median_high() : {statistics.median_high(odd_data)}")
    logger.info(f"  (all three are equal for odd-length data)")
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
    survey_responses = [3, 5, 2, 4, 5, 3, 1, 5, 2, 3, 4, 2, 5, 3, 1, 4, 2]
    survey_responses_counter = Counter(survey_responses)
    logger.info(f"  Dataset          : {survey_responses}")
    logger.info(f"  Frequency table  :")
    for value, count in sorted(survey_responses_counter.items()):
        bar = "#" * count
        logger.info(f"    {value}: {count}  {bar}")
    multi_mode_results = statistics.multimode(survey_responses)
    single_mode_results = statistics.mode(survey_responses)
    logger.info(f"  Multi-mode results  : {multi_mode_results}")
    logger.info(f"  Single mode results : {single_mode_results}")
    logger.info("")

    # Unimodal dataset for contrast
    unimodal = [1, 2, 2, 2, 3, 4, 5]
    logger.info(f"  Unimodal dataset : {unimodal}")
    logger.info(f"  multimode()    : {statistics.multimode(unimodal)}")
    logger.info(f"  mode()         : {statistics.mode(unimodal)}")
    pass

