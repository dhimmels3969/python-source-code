from src.common_library import helper_functions as hf
import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
#
# Exercises found at web page https://pynative.com/python-comprehensions-exercises/
# Exercises 1 through 10
#


##############################################################################
def exercise_01_squares_list():
    """
    Exercise 1: Squares List
    Problem Statement: Generate a list of squares for
        every integer from 1 to 20 using a list
        comprehension. Do not use a for loop with
        append().
    Purpose: This exercise introduces the list
        comprehension syntax as a concise and readable
        replacement for the classic accumulate-and-append
        loop. Mastering the basic [expression for item
        in iterable] form is the first step toward
        writing idiomatic Python and understanding
        the more powerful filtered and nested
        variations that follow in later exercises.
    Given Input:
        Integers from 1 to 20 (inclusive).
    Expected Output:
        [1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144,
        169, 196, 225, 256, 289, 324, 361, 400]
    """
    logger.info("Exercise 1: Squares List")
    pass


##############################################################################
def exercise_02_even_numbers_list():
    """
    Exercise 2: Even Numbers
    Problem Statement: Given a list of integers, use a list
        comprehension with a conditional clause to extract
        only the even numbers and collect them into a new list.
    Purpose: Adding an if-clause to a list comprehension turns
        it into a combined filter-and-collect operation. This
        pattern replaces the common if-inside-a-loop idiom
        with a single readable expression and is one of the
        most frequently used comprehension forms in everyday
        Python code.
    Given Input:
        numbers = [3, 7, 2, 14, 9, 8, 11, 6, 5, 10]
    Expected Output:
        [2, 14, 8, 6, 10]
    """
    logger.info("Exercise 2: Even Numbers")
    pass


##############################################################################
def exercise_03_string_lengths():
    """
    Exercise 3: String Lengths
    Problem Statement: Given a list of words, use a list
        comprehension to create a new list where each
        element is the length of the corresponding word
        from the original list.
    Purpose: This exercise reinforces that the output
        expression in a list comprehension can be any
        valid Python expression — including a function
        call. Applying len() to each element is a simple
        example of the broader pattern of projecting a
        list of objects onto one of their properties
        or derived values.
    Given Input: words =
        ["python", "list", "comprehension", "is", "powerful"]
    Expected Output:
        [6, 4, 13, 2, 8]
    """
    logger.info("Exercise 3: String Lengths")
    pass


##############################################################################
def exercise_04_uppercase_conversion():
    """
    Exercise 4: Uppercase Converter
    Problem Statement: Given a list of lowercase strings,
        use a list comprehension to produce a new list
        where every string has been converted to
        uppercase. The original list must remain
        unchanged.
    Purpose: This exercise shows that the output expression
        in a comprehension can call a method on each
        element, not just a standalone function. It also
        reinforces the immutability of list comprehensions:
        they always produce a new list, leaving the source
        data untouched.
    Given Input:
        fruits = ["apple", "banana", "cherry", "date", "elderberry"]
    Expected Output:
        ['APPLE', 'BANANA', 'CHERRY', 'DATE', 'ELDERBERRY']
    """
    logger.info("Exercise 4: Uppercase Converter")
    pass


##############################################################################
def exercise_05_flatten_list():
    """
    Exercise 5: Flatten a 2D List
    Problem Statement: Given a matrix represented as a list of lists
        (a 2D list), use a nested list comprehension to flatten it
        into a single one-dimensional list. Each inner list can be
        of a different length.
    Purpose: Nested list comprehensions unlock a second dimension of
        iteration within the same expression. Flattening is the canonical
        example: it requires iterating over outer rows and inner elements
        simultaneously. This pattern extends naturally to matrix
        transposition, Cartesian products, and any operation that needs
        to visit every cell in a grid.
    Given Input:
        matrix = [[1, 2, 3], [4, 5], [6, 7, 8, 9]]
    Expected Output:
        [1, 2, 3, 4, 5, 6, 7, 8, 9]
    """
    logger.info("Exercise 5: Flatten List")
    pass


##############################################################################
def exercise_06_filter_and_transform():
    """
    Exercise 6: Filter & Transform Together
    Problem Statement: Given a list of integers, use a
        single list comprehension to produce a new
        list that contains the squares of only the odd
        numbers. Even numbers should be excluded
        entirely from the output.
    Purpose: This exercise combines both halves of
        the comprehension syntax — a transformation
        expression and a filter condition — in one
        concise statement. Performing a filter and a
        transform simultaneously in a single pass is
        one of the most practical and common
        real-world uses of list comprehensions.
    Given Input:
        numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    Expected Output:
        [1, 9, 25, 49, 81]
    """
    logger.info("Exercise 6: Filter & Transform Together")
    pass


##############################################################################
def exercise_07_word_frequency_list():
    """
    Exercise 7: Word Frequency Dict
    Problem Statement: Given a list of words that may contain
        duplicates, use a dictionary comprehension to build
        a dictionary that maps each unique word to the
        number of times it appears in the list.
    Purpose: Dictionary comprehensions extend the
        comprehension concept to key-value pairs, allowing
        you to build a dict in a single expression rather
        than with a loop and manual assignment. Word
        frequency counting is a classic application that
        demonstrates the pattern clearly and mirrors
        real-world text processing tasks such as building
        search indexes, analyzing logs, and computing
        term frequency for NLP.
    Given Input:
        words = ["apple", "banana", "apple", "cherry", "banana", "apple", "date"]
    Expected Output:
        {'apple': 3, 'banana': 2, 'cherry': 1, 'date': 1}
    """
    logger.info("Exercise 7: Word Frequency Dict")
    pass


##############################################################################
def exercise_08_invert_dictionary():
    """
    Exercise 8: Invert a Dictionary
    Problem Statement: Given a dictionary, use a dict
        comprehension to produce a new dictionary where
        the original keys become values and the
        original values become keys. The original d
        ictionary must remain unchanged.
    Purpose: Dictionary inversion is a common operation
        when you need to look up data in the reverse
        direction — for example, finding a country from
        a country code when your data is keyed by country
        name. This exercise shows that dict
        comprehensions are not limited to building new
        data; they can restructure existing mappings
        with a single readable expression.
    Given Input:
        codes = {"USD": "US Dollar", "EUR": "Euro",
                 "GBP": "British Pound", "JPY": "Japanese Yen"}
    Expected Output:
        {'US Dollar': 'USD', 'Euro': 'EUR',
         'British Pound': 'GBP', 'Japanese Yen': 'JPY'}
    """
    logger.info("Exercise 8: Invert Dictionary")
    pass


##############################################################################
def exercise_09_unique_vowels_list():
    """
    Exercise 9: Unique Vowels
    Problem Statement: Given a string, use a set
        comprehension to extract all unique vowels
        (a e i o u) that appear in it. The result
        should be a set, duplicates are discarded
        automatically and order is not guaranteed.
    Purpose: Set comprehensions apply the same concise
        syntax as list comprehensions but produce a
        set, giving automatic deduplication for free.
        This exercise introduces the set comprehension
        form and demonstrates its natural fit for
        tasks where uniqueness matters more than
        order — a common requirement in text
        analysis, data cleaning, and membership testing.
    Given Input:
        sentence = "the quick brown fox jumps over the lazy dog"
    Expected Output:
        {'a', 'e', 'i', 'o', 'u'} (order may vary)
    """
    logger.info("Exercise 9: Unique Vowels")
    pass


##############################################################################
def exercise_10_square_mapping_check():
    """
    Exercise 10: Square Mapping
    Problem Statement: Use a dict comprehension to create a dictionary
        that maps each integer from 1 to 10 to its square. The keys
        should be the integers and the values should be their squares.
    Purpose: This exercise reinforces dict comprehension syntax by
        pairing range() with a mathematical expression as the value.
        The resulting lookup table is a practical data structure:
        instead of recomputing a square every time it is needed,
        you build the mapping once and retrieve values by key
        in O(1) time.
    Given Input:
        Integers from 1 to 10 (inclusive).
    Expected Output:
        {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81, 10: 100}
    """
    logger.info("Exercise 10: Square Mapping")
    pass


