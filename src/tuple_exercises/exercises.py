from src.common_library import helper_functions as hf
import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)


#
# Exercises found at web page https://pynative.com/python-tuple-exercise-with-solutions/
# Exercises 1 through 12
#



##############################################################################
def exercise_01_tuple_basics_check():
    """
    Exercise 1: Basic Tuple Operations
    Problem Statement: Write a Python program to create a tuple,
        access its elements by index, and find its length.
    Purpose: This exercise introduces you to the fundamental building blocks
        of working with tuples: creating them, retrieving individual elements
        using index positions, and measuring their size using len(). These are
        the first skills you need before working with any tuple-based data.
    Given Input:
        fruits = ("apple", "banana", "cherry", "date")
    Expected Output:
        First element: apple, Last element: date, and Length: 4
    """
    logger.info("Exercise 1: Basic Tuple Operations")
    fruits = ("apple", "banana", "cherry", "date")
    first_element = fruits[0]
    last_element = fruits[-1]
    size_of_fruits = len(fruits)
    logger.info(f"  First element: {first_element}, Last element: {last_element}, and Length: {size_of_fruits}")
    pass



##############################################################################
def exercise_02_trailing_comma_check():
    """
    Exercise 2: The Trailing Comma
    Problem Statement: Write a Python program to create a tuple containing
        a single item, the number 50, and confirm its type.
    Purpose: This exercise highlights one of the most common beginner mistakes
        with tuples: assuming that parentheses alone create a tuple. A trailing
        comma is required when the tuple has only one element, and this
        exercise trains you to remember that rule.
    Given Input:
        A single integer value 50
    Expected Output:
        (50,) and <class 'tuple'>
    """
    logger.info("Exercise 2: Trailing Comma")
    my_tuple = (50,)
    logger.info(f"  my tuple: {my_tuple}, type: {type(my_tuple)}")
    pass



##############################################################################
def exercise_03_tuple_repetition():
    """
    Exercise 3: Tuple Repetition
    Problem Statement: Write a Python program to repeat a tuple three
        times using the * operator.
    Purpose: This exercise shows how the * operator works with sequences.
        Repeating a tuple is a concise way to generate patterned data
        without writing loops, and it reinforces the idea that tuples
        support sequence operations just like strings and lists.
    Given Input:
        colors = ("red", "green")
    Expected Output:
        ('red', 'green', 'red', 'green', 'red', 'green')

    """
    logger.info("Exercise 3: Tuple Repetition")
    colors = ("red", "green")
    colors_times_three = colors * 3
    logger.info(f"  {colors_times_three}")
    pass



##############################################################################
def exercise_04_tuple_concatenation():
    """
    Exercise 4: Tuple Concatenation
    Problem Statement: Write a Python program to join three separate tuples
        into one new tuple using the + operator.
    Purpose: This exercise demonstrates how to combine multiple tuples
        without modifying any of the originals. Concatenation is useful
        when you need to assemble a final ordered collection from
        several independent parts.
    Given Input:
        a = (1, 2), b = (3, 4), and c = (5, 6)
    Expected Output:
        (1, 2, 3, 4, 5, 6)
    Additional Information:
        a + b + c will produce different results than (a,b,c)
    """
    logger.info("Exercise 4: Tuple Concatenation")
    a = (1, 2)
    b = (3, 4)
    c = (5, 6)
    combined_tuple = a + b + c
    logger.info(f"  a+b+c: {combined_tuple}")
    different_combined_tuple = (a,b,c)
    logger.info(f"  (a,b,c): {different_combined_tuple}")
    pass



##############################################################################
def exercise_05_tuple_slicing():
    """
    Exercise 5: Tuple Slicing
    Problem Statement: Write a Python program to extract a specific portion
        of a tuple using slice notation.
    Purpose: This exercise teaches you how to retrieve a contiguous subset
        of elements from a tuple without a loop. Slicing is a fundamental
        Python skill used across strings, lists, and tuples alike, and it
        is essential for tasks like pagination, windowing, and data
        partitioning.
    Given Input:
        numbers = (10, 20, 30, 40, 50, 60, 70)
    Expected Output:
        (30, 40, 50)
    """
    logger.info("Exercise 5: Tuple Slicing")
    numbers = (10, 20, 30, 40, 50, 60, 70)
    subset = numbers[2:5]
    logger.info(f"  {subset}")
    pass



##############################################################################
def exercise_06_tuple_reversal():
    """
    Exercise 6: Tuple Reversal
    Problem Statement: Write a Python program to reverse the order of
        elements in a tuple.
    Purpose: This exercise shows how to reverse a tuple even though
        tuples have no built-in .reverse() method (unlike lists). You will
        practice using slice notation with a step value, which is a widely
        used Python idiom for reversing any sequence.
    Given Input:
        items = (1, 2, 3, 4, 5)
    Expected Output:
        (5, 4, 3, 2, 1)
    """
    logger.info("Exercise 6: Tuple Reversal")
    items = (1, 2, 3, 4, 5)
    items_in_reverse = items[::-1]
    logger.info(f"  items: {items} ... items_in_reverse: {items_in_reverse}")
    pass



##############################################################################
def exercise_07_type_casting():
    """
    Exercise 7: Type Casting
    Problem Statement: Write a Python program to convert a list into
        a tuple using the tuple() constructor.
    Purpose: This exercise demonstrates how to convert between mutable
        and immutable sequence types. Converting a list to a tuple is a
        common pattern when you want to protect data from accidental
        modification, use it as a dictionary key, or pass it to a
        function that expects an immutable sequence.
    Given Input:
        my_list = [10, 20, 30, 40, 50]
    Expected Output:
        (10, 20, 30, 40, 50) and <class 'tuple'>
    """
    logger.info("Exercise 7: Type Casting")
    my_list = [10, 20, 30, 40, 50]
    my_tuple = tuple(my_list)
    logger.info(f"  my_tuple: {my_tuple}")
    logger.info(f"  {type(my_tuple)}")
    pass



##############################################################################
def exercise_08_tuple_to_string():
    """
    Exercise 8: Tuple to String
    Problem Statement: Write a Python program to convert a tuple of
        characters into a single joined string.
    Purpose: This exercise shows how to bridge the gap between tuples
        and strings. The str.join() method is a core Python tool for
        assembling strings from iterable sequences, and practising it
        on a tuple reinforces that join() works on any iterable,
        not just lists.
    Given Input:
        chars = ('a', 'b', 'c')
    Expected Output:
        abc
    """
    logger.info("Exercise 8: Tuple to String")
    chars = ('a', 'b', 'c')
    results = "".join(chars)
    logger.info(f"  {results}")
    pass



##############################################################################
def exercise_09_tuple_membership_test():
    """
    Exercise 9: Tuple Membership Testing
    Problem Statement: Write a Python program to check whether a specific
        element exists inside a tuple using the in keyword.
    Purpose: This exercise introduces membership testing, one of the most
        readable and expressive features of Python. Checking for the presence
        of a value in a collection is a task that appears constantly in
        real-world code, from input validation to search logic.
    Given Input:
        fruits = ("apple", "banana", "cherry", "date")
    Expected Output:
        True and False
    """
    logger.info("Exercise 9: Tuple Membership Testing")
    fruits = ("apple", "banana", "cherry", "date")
    apple_ = "apple" in fruits
    tomato_ = "tomato" in fruits
    logger.info(f"  fruits: {fruits}")
    logger.info(f"  'apple' in fruits: {apple_}")
    logger.info(f"  'tomato' in fruits: {tomato_}")
    pass



##############################################################################
def exercise_10_counting_test():
    """
    Exercise 10: Counting
    Problem Statement: Write a Python program to use the .count() method
        to find how many times a specific element appears in a tuple.
    Purpose: This exercise introduces one of the two built-in methods that
        tuples provide. Knowing how to count occurrences without writing a
        manual loop is a practical skill used in frequency analysis,
        data validation, and duplicate detection.
    Given Input:
        votes = ("yes", "no", "yes", "yes", "no", "yes")
    Expected Output:
        yes appears 4 times and no appears 2 times
    """
    logger.info("Exercise 10: Counting")
    votes = ("yes", "no", "yes", "yes", "no", "yes")
    yes_ = votes.count("yes")
    no_ = votes.count("no")
    logger.info(f"  yes appears {yes_} times and no appears {no_} times")
    pass



##############################################################################
def exercise_11_tuple_unpacking():
    """
    Exercise 11: Tuple Unpacking
    Problem Statement: Write a Python program to unpack a four-element
        tuple into four distinct variables in a single assignment.
    Purpose: This exercise introduces tuple unpacking, one of Python’s most
        elegant features. Unpacking makes code more readable by giving meaningful
        names to positional data, and it is widely used when working with
        function return values, database rows, and coordinate pairs.
    Given Input:
        person = ("Alice", 30, "Engineer", "Pune")
    Expected Output:
        Name: Alice, Age: 30, Job: Engineer, and City: Pune
    """
    logger.info("Exercise 11: Tuple Unpacking")
    person = ("Alice", 30, "Engineer", "Pune")
    (Name, Age, Job, City) = person
    logger.info(f"  Name: {Name}, Age: {Age}, Job: {Job}, and City: {City}")
    pass



##############################################################################
def exercise_12_swap_values():
    """
    Exercise 12: The Swap Trick
    Problem Statement: Write a Python program to swap the values of two variables
        using tuple unpacking, without using a temporary third variable.
    Purpose: This exercise demonstrates one of Python’s most well-known idioms.
        The swap trick works because Python evaluates the entire right-hand side as
        a tuple before performing any assignment, making it both concise and safe.
        It is a practical showcase of how unpacking can replace verbose
        boilerplate code.
    Given Input:
        a = 100 and b = 200
    Expected Output:
        After swap: a = 200, b = 100
    """
    logger.info("Exercise 12: Swap Trick")
    a = 100
    b = 200
    logger.info(f"  ----BEFORE---- a: {a}, b: {b}")
    b, a = a, b
    logger.info(f"  ----AFTER----  a: {a}, b: {b}")
    pass





