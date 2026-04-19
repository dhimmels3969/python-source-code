#
# Exercises found at web page https://pynative.com/python-if-else-and-for-loop-exercise-with-solutions/
# Exercises 31 through 40
#


def exercise_31_segregate_items_in_list():
    """
    Exercise 31. Even/Odd Segregation: Move evens to front, odds to back
    Practice Problem: Given a list of integers, move all even numbers
        to the beginning of the list and all odd numbers to the end.
    Exercise Purpose: This introduces List Reorganization, a simplified version
        of the partitioning logic used in QuickSort algorithms. You learn to
        categorize data and reassemble it into a specific structural order.
    Given Input:
        [1, 2, 3, 4, 5, 6]
    Expected Output:
        Segregated List:
            [2, 4, 6, 1, 3, 5]
    """
    pass
###########################################################


def exercise_32_list_rotation():
    """
    Exercise 32. List Rotation: Rotate elements left by k positions
    Practice Problem: Given a list and an integer k, rotate the list
        to the left by k positions. For example, if k=2, the first two elements
        move to the end of the list.
    Exercise Purpose: This exercise teaches Positional Manipulation. While slicing is common,
        using a loop helps you understand how data shifts in memory. This is a core concept for
        circular buffers and scheduling algorithms.
    Given Input:
        nums = [1, 2, 3, 4, 5]
        k = 2
    Expected Output:
        Rotated List: [3, 4, 5, 1, 2]
    """
    print("Exercise 32. List Rotation")
    pass
###########################################################


def exercise_33_word_frequency_counter():
    """
    Exercise 33. Word frequency counter
    Practice Problem: Write a program to count the frequency of each word in a given string.
    Exercise Purpose: This introduces Mapping Logic. You learn to transform a “flat”
        string into a structured dictionary. This is the starting point for almost
        all Natural Language Processing (NLP) tasks, such as building a search engine or a tag cloud.
    Given Input:
        text = "apple banana apple orange banana apple"
    Expected Output:
        {'apple': 3, 'banana': 2, 'orange': 1}
    """
    print("Exercise 33. Word frequency counter")
    pass
###########################################################



def exercise_34_fibonacci_series():
    """
    Exercise 34. Display fibonacci series up to 10 terms
    Practice Problem: Write a program to display the Fibonacci sequence up to 10 terms.
        The sequence starts with 0 and 1, and each subsequent number is the sum of the two preceding ones.
    Exercise Purpose: This exercise teaches State Management. You keep track of
        two changing variables (n1 and n2) and update them in sync
        to crawl forward through the sequence.
    Given Input:
        n_terms = 10
    Expected Output:
        0 1 1 2 3 5 8 13 21 34
    """
    print("Exercise 34. Fibonacci series up to 10 terms")
    pass
###########################################################



def exercise_35_perfect_number_check():
    """
    Exercise 35. Perfect number check
    Practice Problem: Write a program to check if a number is a “Perfect Number.”
        A perfect number is a positive integer that is equal to the sum of its
        proper divisors (excluding the number itself). For example,
        6 is perfect because 1 + 2 + 3 = 6.
    Exercise Purpose: Emphasizes efficiency in search. While you
        could check every number up to n, you only need to check up
        to n/2 to find all divisors, showing how to optimize loop ranges.
    Given Input:
        num = 28
    Expected Output:
        28 is a Perfect Number (1 + 2 + 4 + 7 + 14 = 28)
    """
    print("Exercise 35. Perfect Number Check")
    pass
###########################################################



def exercise_36_binary_decimal_conversion():
    """
    Exercise 36. Binary to decimal conversion using loop
    Practice Problem: Manually convert a binary string (e.g., "1101")
        into its decimal integer equivalent using a loop. Do not use int(binary, 2).
    Exercise Purpose: This exercise teaches Positional Notation and Powers.
        It helps you visualize how computers store numbers and process strings
        from right to left or vice versa to apply mathematical weights.
    Given Input:
        binary_str = "1101"
    Expected Output:
        Decimal value: 13
    """
    print("Exercise 36. Binary to decimal conversion using loops")
    pass
###########################################################



def exercise_37_display_prime_numbers():
    """
    Exercise 37. Display all prime numbers within a range
    Practice Problem: Write a program to display all prime numbers within a range (e.g., 25 to 50).
        A prime number is a natural number greater than 1 that is not a product of two smaller
        natural numbers.
    Exercise Purpose: This is a classic test of Nested Loop Logic. You iterate
        through a range of numbers (outer loop) and, for each,
        run another loop (inner loop) to check if any smaller number
        divides it evenly. It’s excellent for practicing flag variables or the loop-else construct
    Given Input:
        start = 25, end = 50
    Expected Output:
        Prime numbers between 25 and 50 are:
        29
        31
        37
        41
        43
        47
    """
    print("Exercise 37. Display all prime numbers within a range")
    pass
###########################################################



def exercise_38_find_sum_of_series():
    """
    Exercise 38. Find the sum of the series up to n terms
    Practice Problem: Write a program to calculate the sum of the
        series 2 + 22 + 222 + 2222 + …. up to N terms.
        For example, if n=5, the series is 2 + 22 + 222 + 2222 + 22222.
    Exercise Purpose: This advanced Pattern Accumulation exercise
        requires generating a new number at each step by multiplying
        the previous number by 10, adding 2, and then adding that
        result to a running total.
    Given Input:
        number_of_terms = 5
    Expected Output:
        24690
    """
    print("Exercise 38. Find the sum of the series up to n terms")
    pass
###########################################################



def exercise_39_flatten_list():
    """
    Exercise 39. flatten a nested list using loops
    Practice Problem: Given a nested list (a list containing other lists),
        write a program to “flatten” it into a single list containing
        all the individual elements.
    Exercise Purpose: In data science and web development, data often arrives
        in “nested” formats (like JSON). This exercise teaches you
        Dimensionality Reduction. You learn how to “reach inside”
        one container to pull items out and place them into a new, simpler container.
`   Given Input:
        nested_list = [[10, 20], [30, 40], [50, 60]]
    Expected Output:
        [10, 20, 30, 40, 50, 60]
    """
    print("Exercise 39. flatten list")
    pass
###########################################################



def exercise_40_nested_list_search():
    """
    Exercise 40. Nested list search (2D matrix coordinates)
    Practice Problem: Given a 2D list (matrix), find the row and column index of a target value.
    Exercise Purpose: This is the foundation of Coordinate Systems.
        You learn to use nested loops, where the outer loop iterates over rows,
        and the inner loop iterates over columns. This logic is essential for
        game development, image processing, and spreadsheet automation.
    Given Input:
        matrix = [[10, 20], [30, 40], [50, 60]]
        target = 30
    Expected Output:
        Target 30 found at Row: 1, Column: 0
    """
    print("Exercise 40. Nested list search")
    pass
###########################################################
