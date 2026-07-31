import logging
from pathlib import Path
import math
from src.common_library import helper_functions as hf

#
# https://pynative.com/python-math-statistics-exercises/
# Exercises 1 through 10
#


logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)



#########################################################################################
def exercise_01_square_root_and_power():
    """
    Exercise 1: Square Root and Power
    Problem Statement:
        Write a Python program that uses math.sqrt() to find the
        square root of 144 and math.pow() to compute 2 raised
        to the power of 10, then prints both results.
    Purpose:
        Square roots and powers appear constantly in geometry,
        physics simulations, financial modelling, and algorithm
        complexity analysis. This exercise introduces the two
        most fundamental functions in the math module and
        highlights the difference between math.pow() and Python’s
        built-in ** operator in terms of return type and precision.
    Given Input:
        number = 144 and base, exponent = 2, 10
    Expected Output:
        Square root of 144: 12.0 and 2 ^ 10 = 1024.0
    """
    logger.info(f"Exercise 1: Square Root and Power")
    pass



#########################################################################################
def exercise_02_area_of_circle():
    """
    Exercise 2: Area of a Circle
    Problem Statement:
        Write a Python program that calculates the area of a circle
        with radius 7 using math.pi, and also computes the
        circumference, printing both results rounded to two
        decimal places.
    Purpose:
        Circle geometry is foundational in graphics, physics engines,
        signal processing, and engineering calculations. Using math.pi
        instead of a hardcoded approximation like 3.14159 gives the
        highest precision available in floating-point arithmetic and
        makes the code’s intent immediately clear to any reader.
    Given Input:
        radius = 7
    Expected Output:
        Area: 153.94 and Circumference: 43.98
    """
    logger.info(f"Exercise 2: Area of a Circle")
    pass



#########################################################################################
def exercise_03_factorial_computation_test():
    """
    Exercise 3: Factorial Computation
    Problem Statement:
        Write a Python program that uses math.factorial() to
        compute 10! and verifies that the result equals 3628800.
    Purpose:
        Factorials are central to combinatorics, probability
        theory, permutation and combination calculations, and
        Taylor series expansions. Using math.factorial() is
        significantly faster and safer than writing a manual loop
        or recursive function, especially for large values where
        Python’s arbitrary-precision integers shine.
    Given Input:
        n = 10
    Expected Output:
        10! = 3628800 and Verification passed: True
    """
    logger.info(f"Exercise 3: Factorial Computation")
    pass



#########################################################################################
def exercise_04_floor_and_ceiling_test():
    """
    Exercise 4: Ceiling and Floor
    Problem Statement:
        Write a Python program that uses math.ceil() and math.floor()
        to find the ceiling and floor of 4.7, then demonstrates the
        same functions on negative numbers to reveal their behavior
        around zero.
    Purpose:
        Ceiling and floor rounding are essential in pagination logic
        (how many pages to display), resource allocation (how many
        containers to provision), pricing (always rounding up to the
        nearest cent), and grid snapping in graphics. Understanding
        how they behave with negative numbers prevents a common
        off-by-one class of bugs.
    Given Input:
        value = 4.7 and negative_value = -4.7
    Expected Output:
        ceil(4.7) = 5, floor(4.7) = 4, ceil(-4.7) = -4, floor(-4.7) = -5
    """
    logger.info(f"Exercise 4: Floor and Ceiling Rounding")
    pass



#########################################################################################
def exercise_05_greatest_common_divisor():
    """
    Exercise 5: Greatest Common Divisor
    Problem Statement:
        Write a Python program that uses math.gcd() to find the
        greatest common divisor of 48 and 180, then uses it to
        reduce the corresponding fraction to its simplest form.
    Purpose:
        The GCD is a foundational operation in number theory
        with practical applications in fraction simplification,
        cryptography (RSA key generation), scheduling (finding
        common cycle lengths), and screen resolution scaling.
        This exercise shows both the direct use of math.gcd()
        and a concrete real-world application of its result.
    Given Input:
        a = 48 and b = 180
    Expected Output:
        GCD(48, 180) = 12 and 48/180 simplified = 4/15
    """
    logger.info(f"Exercise 5: Greatest Common Divisor")
    pass



#########################################################################################
def exercise_06_hypotenuse_of_right_triangle():
    """
    Exercise 6: Hypotenuse of a Right Triangle
    Problem Statement:
        Write a Python program that computes the hypotenuse of
        a right triangle with legs 3 and 4 using math.hypot(),
        then verifies the result against the manually computed
        Pythagorean formula.
    Purpose:
        Euclidean distance – the straight-line distance
        between two points – is the hypotenuse formula in
        disguise. It is used constantly in game development,
        mapping applications, robotics path planning, machine
        learning distance metrics, and physics simulations.
        math.hypot() is numerically safer than the manual
        formula because it avoids overflow and underflow for
        very large or very small values.
    Given Input:
        a = 3 and b = 4
    Expected Output:
        Hypotenuse: 5.0 and Manual formula result: 5.0
    """
    logger.info(f"Exercise 6: Hypotenuse of Right Triangle")
    pass



#########################################################################################
def exercise_07_logarithms_tests():
    """
    Exercise 7: Natural and Base-10 Logarithms
    Problem Statement:
        Write a Python program that uses math.log() and math.log10()
        to compute the natural logarithm (base e) and the base-10
        logarithm of 1000, then verifies each result by reversing it
        with the corresponding exponential function.
    Purpose:
        Logarithms are used in decibel calculations, pH measurements,
        earthquake magnitude scales, information entropy, algorithmic
        complexity (binary search is O(log n)), and machine learning
        loss functions. Understanding both the natural log and
        base-10 log, and knowing how to verify them by reversal,
        builds the intuition needed to apply them correctly across
        these domains.
    Given Input:
        value = 1000
    Expected Output:
        ln(1000) = 6.9078, log10(1000) = 3.0, and
        verification that reversing each result
        recovers the original value.
    """
    logger.info(f"Exercise 7: Natural and Base-10 Logarithms")
    pass



#########################################################################################
def exercise_08_degrees_to_radians_conversion():
    """
    Exercise 8: Degrees to Radians, Sine and Cosine
    Problem Statement:
        Write a Python program that converts 270 degrees to
        radians using math.radians(), then computes and
        prints its sine and cosine values.
    Purpose:
        Python’s trigonometric functions operate in radians,
        not degrees, so converting between the two is a
        required first step in any geometry, physics, or
        signal processing task. This exercise also builds
        intuition for the unit circle – knowing that
        sin(270°) = -1 and cos(270°) = 0 provides a mental
        anchor for verifying trigonometric results.
    Given Input:
        degrees = 270
    Expected Output:
        270° in radians: 4.7124, sin(270°) = -1.0, cos(270°) = 0.0
    """
    logger.info(f"Exercise 8: Degrees to Radians, Sine and Cosine")
    pass



#########################################################################################
def exercise_09_combinations_and_permutations():
    """
    Exercise 9: Combinations and Permutations
    Problem Statement:
        Write a Python program that uses math.comb() and
        math.perm() to calculate the number of combinations
        and permutations for n=10 items taken k=3 at a time,
        then prints both results with a clear explanation
        of what each value means.
    Purpose:
        Combinations and permutations are the building blocks
        of probability theory, statistics, and discrete
        mathematics. They appear in lottery odds, card game
        probabilities, password strength calculations, and
        test case generation. math.comb() and math.perm()
        were introduced in Python 3.8 as direct, readable
        replacements for the manual factorial-based formulas.
    Given Input:
        n = 10, k = 3
    Expected Output:
        C(10, 3) = 120 and P(10, 3) = 720
    """
    logger.info(f"Exercise 9: Combinations and Permutations")
    pass



#########################################################################################
def exercise_10_floating_point_precision():
    """
    Exercise 10: Floating-Point Precision with math.isclose()
    Problem Statement:
        Write a Python program that uses math.isclose() to
        compare 0.1 + 0.2 with 0.3, demonstrates why a
        direct == comparison fails, and explains the
        floating-point precision issue behind it.
    Purpose:
        Floating-point precision errors are among the most
        common sources of bugs in scientific computing,
        financial software, and unit tests. Understanding
        why 0.1 + 0.2 != 0.3 in binary floating-point
        arithmetic, and knowing how to compare floats
        correctly using math.isclose(), is an essential
        skill for writing reliable numerical code.
    Given Input:
        a = 0.1 + 0.2 and b = 0.3
    Expected Output:
        0.1 + 0.2 == 0.3 : False and
        math.isclose(0.1 + 0.2, 0.3): True
    """
    logger.info(f"Exercise 10: Floating-Point Precision with math.isclose()")
    pass

