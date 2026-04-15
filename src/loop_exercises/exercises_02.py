# from html.parser import incomplete
from src.common_library import helper_functions as hf

#
# Exercises found at web page https://pynative.com/python-if-else-and-for-loop-exercise-with-solutions/
# Exercises 11 through 20
#



#######################################################################################################
def exercise_11_reverse_string():
    """
    Exercise 11. Reverse a string using a for loop (no slicing)
    Practice Problem: Write a program that takes a string and reverses
        it using a for loop. While Python’s [::-1] shortcut is famous,
        reversing a string manually is a classic way to understand how
        sequences are constructed.
    Exercise Purpose: Learn how accumulation logic works. In Python, strings
        are “immutable,” which means you cannot change them directly.
        Here, you will practice building a new string by adding characters
        to the front. This is a key idea for algorithms that build results step by step.

    Given Input:
        "Python"
    Expected Output:
        Original:
            Python
        Reversed:
            nohtyP
    """
    print("Exercise 11. Reverse a string using a for loop.")
    pass


def exercise_12_count_vowels_consonants():
    """
    Exercise 12. Count vowels and consonants in a sentence
    Practice Problem: Write a program that counts the total number of vowels
        and consonants in a given sentence, ignoring spaces and special characters.
    Exercise Purpose: In this exercise, you will practice membership testing and data
        filtering. You will use the in operator to check if a value is in a collection,
        and try string methods like .isalpha() to quickly clean your data.
    Given Input:
        "Loops are Fun!"
    Expected Output:
        Vowels: 5
        Consonants: 7

    """
    print("Exercise 12. Count vowels and consonants in a sentence")
    pass


def exercise_13_count_total_digits():
    """
    Exercise 13. Count total number of digits in a number
    Practice Problem: Write a program to count the total number of digits
        in a given integer using a while loop.
    Exercise Purpose: This exercise introduces Arithmetic Reduction. Instead
        of treating the number as a string, you learn to peel off digits
        mathematically using floor division (//). This logic is common in
        algorithms involving digit manipulation, such as reversing numbers
        or checking for palindromes.
    Given Input:
        75869
    Expected Output:
        Total digits are: 5
    """
    print("Exercise 13. Count total number of digits in a number")
    pass


def exercise_14_reverse_integer_number():
    """
    Exercise 14. Reverse an integer number
    Practice Problem: Write a program to reverse a given integer number
        (e.g., 76542 should become 24567).
    Exercise Purpose: While you could convert the number to a string and slice it, doing it mathematically
        is more efficient and teaches you to use Modulo (%) and Floor Division (//)
        together to manipulate digits.
    Given Input:
        76542
    Expected Output:
        24567
    :return:
    :rtype:
    """
    print("Exercise 14. Reverse an integer number")
    pass


def exercise_15_find_largest_smallest():
    """
    Exercise 15. Find largest and smallest digit in a number
    Practice Problem: Write a program to find the largest and smallest digit
        within a given integer (e.g., in 75869, the largest is 9 and the smallest is 5).
    Exercise Purpose: This combines Digit Extraction (from Exercise 14) with
        Min/Max Comparison. It’s a foundational logic for finding “extremes”
        in a dataset. You learn how to initialize comparison variables and update
        them dynamically as you scan through data.
    Given Input:
        num = 75869
    Expected Output:
        Largest digit: 9
        Smallest digit: 5
    """
    print("Exercise 15. Find largest and smallest digit in a number")
    pass


def exercise_16_check_for_palindrome():
    """
    Exercise 16. Check if a number is a palindrome
    Practice Problem: Write a program to check if a given number is a palindrome.
        A palindrome number is a number that remains the same when its digits
        are reversed (e.g., 121, 343).
    Exercise Purpose: This exercise combines Mathematical Reversal with Conditional Comparison.
        It teaches storing an original value before modifying it in a
        loop so you can perform a final validation.
    Given Input:
        number = 121
    Expected Output:
        Yes
    """
    print("Exercise 16. Check if a number is a palindrome")
    pass


def exercise_17_find_factorial():
    """
    Exercise 17. Find factorial of a number
    Practice Problem: Write a program to use a loop to find the
        factorial of a given number (e.g., 5!). The factorial of N is the
        product of all integers from 1 to N.
    Exercise Purpose: Factorials grow fast. This exercise demonstrates
        Iterative Multiplication, a core concept used in probability,
        statistics, and combinatorics.
    Given Input:
        num = 5
    Expected Output:
        120
    """
    print("Exercise 17. Find factorial of a given number")
    pass


def exercise_18_collatz_conjecture():
    """
    Exercise 18. Collatz Conjecture: Generate a sequence until it reaches 1
    Practice Problem: The Collatz conjecture states that if you start with
        any positive integer n, and if n is even, divide it by 2; if n is odd,
        multiply it by 3 and add 1. Repeat the process. The sequence will always
        eventually reach 1. Write a program to print this sequence for a given number.
    Exercise Purpose: This exercise demonstrates Indeterminate Iteration.
        Unlike a for loop with a known range, a while loop runs
        until a specific mathematical condition, reaching 1, is met.
    Given Input:
        n = 6
    Expected Output:
        6, 3, 10, 5, 16, 8, 4, 2, 1
    """
    print("Exercise 18. Collatz Conjecture: Generate a sequence until it reaches 1")
    pass


def exercise_19_armstrong_number_check():
    """
    Exercise 19. Armstrong Number Check
    Practice Problem: Write a program to check if a number is an Armstrong number. An Armstrong number
        (for a 3-digit number) is an integer such that the sum of the cubes of its digits
        is equal to the number itself (e.g., 153 = 1^3 + 5^3 + 3^3).
    Exercise Purpose: This logic-heavy exercise combines Type Conversion, Mathematical Iteration,
        and Power Operations. It tests your ability to break a complex problem into steps:
        isolate digits, raise them to a power, and compare the sum.
    Given Input:
        num = 153
    Expected Output:
        Yes
    """
    print("Exercise 19. Armstrong Number Check")
    pass


def exercise_20_print_number_pattern():
    """
    Exercise 20. Print right-angled triangle Number Pattern using a Loop
    Practice Problem: Write a program to print a right-angled triangle
        pattern where each row contains increasing numbers up to the row number.
    Exercise Purpose: This exercise introduces Nested Loops. It demonstrates
        how an “outer” loop can control the rows of a structure, while an “inner”
        loop handles the specific data printed within each row.
    Given Input:
        None (Pattern height is 5).
    Expected Output:
        1
        1 2
        1 2 3
        1 2 3 4
        1 2 3 4 5
    """
    print("Exercise 20. Print right-angled triangle Number Pattern using a Loop.")
    pass




