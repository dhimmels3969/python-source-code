from src.common_library import helper_functions as hf
import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
#
# Exercises found at web page https://pynative.com/python-comprehensions-exercises/
# Exercises 11 through 20
#


##############################################################################
def exercise_11_fizzbuzz_comprehension():
    """
    Exercise 11: FizzBuzz with Comprehension
    Problem Statement: Produce the classic FizzBuzz sequence
        for integers 1 to 50 in a single list comprehension.
        Each element should be "FizzBuzz" if the number is
        divisible by both 3 and 5, "Fizz" if divisible by 3
        only, "Buzz" if divisible by 5 only, and the number
        itself (as an integer) otherwise.
    Purpose: FizzBuzz requires branching logic with multiple
        conditions — traditionally written as a cascade of
        if/elif/else statements. Expressing it inside a
        comprehension using nested ternary expressions shows
        how conditional output expressions work, and
        forces you to think carefully about condition order
        to get correct results.
    Given Input:
        Integers from 1 to 50 (inclusive).
    Expected Output:
        [1, 2, 'Fizz', 4, 'Buzz', 'Fizz', 7, 8, 'Fizz', 'Buzz',
         11, 'Fizz', 13, 14, 'FizzBuzz', 16, 17, 'Fizz', 19, 'Buzz',
         21, 22, 'Fizz', 'Buzz', 26, 'Fizz', 28, 29, 'FizzBuzz', 31,
         ...]
    """
    logger.info("Exercise 11: FizzBuzz with Comprehension")
    pass


##############################################################################
def exercise_12_matrix_transposition():
    """
    Exercise 12: Matrix Transposition
    Problem Statement: Given a 3×3 matrix represented
        as a list of lists, use a nested list comprehension
        to produce its transpose — a new matrix where
        rows and columns are swapped. Row i, column j
        of the original becomes row j, column i of
        the result.
    Purpose: Matrix transposition is a fundamental
        operation in linear algebra, image processing,
        and data manipulation (it is what pandas.DataFrame.T
        does internally). Implementing it with a nested
        list comprehension — where the outer loop
        produces rows and the inner loop fills columns
        — deepens understanding of how nested
        comprehensions build two-dimensional structures
        rather than flattening them.
    Given Input:
        matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    Expected Output:
        Original:
            [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        Transposed:
            [[1, 4, 7], [2, 5, 8], [3, 6, 9]]
    """
    logger.info("Exercise 12: Matrix Transposition")
    pass


##############################################################################
def exercise_13_cartesian_product():
    """
    Exercise 13: Cartesian Product
    Problem Statement: Given two lists, use a nested list
        comprehension to generate every possible (x, y) pair
        where x comes from the first list and y comes from
        the second. This is the Cartesian product of the
        two lists. Do not use itertools.product.
    Purpose: The Cartesian product is needed any time you
        want to try every combination of two sets of values
        — grid coordinates, test parameter combinations,
        pairing sizes with colors in a catalogue, or
        generating game board positions. A nested
        comprehension produces it naturally and clearly,
        and understanding it is the key to recognizing
        when itertools.product is the right tool for
        more complex cases.
    Given Input:
        xs = [1, 2, 3] and ys = ["a", "b", "c"]
    Expected Output:
        [(1, 'a'), (1, 'b'), (1, 'c'),
         (2, 'a'), (2, 'b'), (2, 'c'),
         (3, 'a'), (3, 'b'), (3, 'c')]
    """
    logger.info("Exercise 13: Cartesian Product")
    pass


##############################################################################
def exercise_14_extract_digits():
    """
    Exercise 14: Extract Digits
    Problem Statement: Given a list of strings that contain
        a mix of letters and digits, use a nested list
        comprehension to extract every numeric character
        from every string and collect them all into a
        single flat list of digit characters.
    Purpose: This exercise combines nested iteration
        with a filter condition in one comprehension to
        simultaneously flatten and filter a two-level
        structure. It mirrors a real pattern in data
        cleaning: stripping non-numeric characters from
        product codes, phone numbers, or identifiers
        spread across a collection of strings.
    Given Input:
        strings = ["abc123", "hello", "42px", "year2024", "no-digits"]
    Expected Output:
        ['1', '2', '3', '4', '2', '4', '2', '0', '2', '4']
    """
    logger.info("Exercise 14: Extract Digits")
    pass


##############################################################################
def exercise_15_nested_filtering():
    """
    Exercise 15: Nested Filtering
    Problem Statement: Given a list of lists of numbers, use a list
        comprehension to extract only those sub-lists where every
        element is positive. Each qualifying sub-list should appear
        in the output intact — do not flatten or modify
        the inner lists.
    Purpose: This exercise separates nested filtering from nested
        iteration. Rather than looping inside a sub-list to
        transform its contents, you are evaluating a condition
        that considers the sub-list as a whole and either keeps
        it or discards it. This pattern appears whenever you want
        to select complete rows, groups, or records based on a
        property of all their members.
    Given Input:
        groups = [[1, 2, 3], [-1, 4, 5], [6, 7, 8], [0, 9, 10], [-3, -1, 2], [4, 5, 6]]
    Expected Output:
        [[1, 2, 3], [6, 7, 8], [4, 5, 6]]
    """
    logger.info("Exercise 15: Nested Filtering")
    pass


##############################################################################
def exercise_16_conditional_dictionary_comprehension():
    """
    Exercise 16: Conditional Dict Comprehension
    Problem Statement: Given a dictionary mapping student
        names to their exam scores, use a dict comprehension
        with an if clause to produce a new dictionary
        containing only the students who passed — defined
        as a score of 50 or above.
    Purpose: Filtering a dictionary down to a relevant
        subset is one of the most common data-processing
        tasks in Python: extracting active users, keeping
        only in-stock products, or selecting records above
        a threshold. A dict comprehension with an
        if clause handles this in a single readable line,
        replacing a manual loop with conditional
        assignment.
    Given Input:
        scores = {"Alice": 82, "Bob": 45, "Charlie": 91,
                  "Diana": 37, "Eve": 55, "Frank": 49}
    Expected Output:
        {'Alice': 82, 'Charlie': 91, 'Eve': 55}
    """
    logger.info("Exercise 16: Conditional Dict Comprehension")
    pass


##############################################################################
def exercise_17_grouped_dictionary():
    """
    Exercise 17: Grouped Dict from Two Lists
    Problem Statement: Given a list of keys and a
        list of values of equal length, use a dict
        comprehension with zip() to pair them into
        a dictionary. Where a value is None,
        substitute it with the string "N/A".
    Purpose: Combining two parallel lists into a
        dictionary is a common data-wrangling task
        — turning a list of column headers and a
        list of row values into a record, for
        example. Adding the None-to-"N/A" substitution
        shows how a conditional expression on the
        value side of a dict comprehension handles
        missing data inline, without a separate
        preprocessing step.
    Given Input:
        keys = ["name", "age", "city", "email"] and
        values = ["Alice", 30, None, None]
    Expected Output:
        {'name': 'Alice', 'age': 30, 'city': 'N/A', 'email': 'N/A'}
    """
    logger.info("Exercise 17: Grouped Dict from Two Lists")
    pass


##############################################################################
def exercise_18_common_elements():
    """
    Exercise 18: Set of Common Elements
    Problem Statement: Given two lists of integers that
        may contain duplicates, use a set comprehension to
        find all numbers that appear in both lists. Each
        number should appear only once in the result
        regardless of how many times it occurs in
        either list.
    Purpose: Finding the intersection of two collections is
        a fundamental operation in data analysis
        — matching customer IDs across two datasets,
        finding common tags between posts, or identifying
        shared product codes. This exercise shows how a
        set comprehension with an in check produces the
        intersection naturally, and sets up an intuition
        for when Python’s built-in set operations are
        the right tool.
    Given Input:
        list_a = [1, 2, 3, 4, 5, 3, 2] and list_b = [3, 4, 5, 6, 7, 4, 5]
    Expected Output:
        {3, 4, 5} (order may vary)
    """
    logger.info("Exercise 18: Set of Common Elements")
    pass


##############################################################################
def exercise_19_character_frequency_set():
    """
    Exercise 19: Character Frequency Set
    Problem Statement: Given a sentence, use a set comprehension
        with a condition to build a set of all characters
        — excluding spaces — that appear more than once in the
        sentence. The result should contain each such character
        exactly once.
    Purpose: This exercise combines set comprehensions with a
        condition that requires querying the source data
        (the sentence’s character counts) to decide which
        elements to include. It shows that the filter condition
        in a comprehension is not limited to simple comparisons
        — it can call any function, including str.count(),
        which turns a comprehension into a concise
        frequency-based analysis tool.
    Given Input:
        sentence = "comprehension makes python powerful"
    Expected Output:
        A set of characters that each appear at least twice.
        Expected characters include 'o', 'e', 'n', 's', 'i',
        'p', and 'h' (order may vary).
    """
    logger.info("Exercise 19: Character Frequency Set")
    pass


##############################################################################
def exercise_20_lazy_squares():
    """
    Exercise 20: Lazy Squares
    Problem Statement: Create a generator expression that yields
        the squares of integers from 1 to 1,000,000. Retrieve only
        the first 10 values using itertools.islice(). Then compare
        the memory footprint of the generator against an equivalent
        list comprehension using sys.getsizeof() to make the
        efficiency difference concrete.
    Purpose: A list comprehension materializes every value into
        memory immediately. A generator expression computes each
        value only when requested and stores nothing beyond the
        current position. When only a small portion of a large
        sequence is needed, the generator uses a constant amount
        of memory regardless of the sequence’s theoretical
        length — a critical distinction for large-scale
        data processing.
    Given Input:
        Integers from 1 to 1,000,000.
    Expected Output:
        First 10 squares: [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
        Generator size:   208 bytes
        List size:        8,000,056 bytes
    """
    logger.info("Exercise 20: Lazy Squares")
    pass