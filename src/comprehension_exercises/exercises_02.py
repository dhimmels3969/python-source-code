from src.common_library import helper_functions as hf
import itertools
import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
#
# Exercises found at web page https://pynative.com/python-comprehensions-exercises/
# Exercises 21 through 25
#


##############################################################################
def exercise_21_fibonacci_generator():
    """
    Exercise 21: Infinite Fibonacci Generator
    Problem Statement: Write a generator function fibonacci() that
        yields Fibonacci numbers indefinitely. Then use
        itertools.takewhile() to lazily consume from it, stopping as
        soon as a value exceeds a given limit. Collect the results
        into a list and print them.
    Purpose: An infinite generator paired with takewhile() is the
        functional-style alternative to a while loop with a break
        condition. It separates the concern of producing values
        from the concern of deciding when to stop, making both
        halves independently reusable and testable. This pattern
        is fundamental to stream processing and lazy pipelines
        in Python.
    Given Input:
        All Fibonacci numbers up to but not including 200.
    Expected Output:
        [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144]
    """
    def fibonacci():
        a, b = 0, 1
        while True:
            a, b = b, a+b
            yield b

    logger.info("Exercise 21: Infinite Fibonacci Generator")
    threshhold = 200
    results = itertools.takewhile(lambda n: n < threshhold, fibonacci())
    logger.info(f"  {list(results)}")
    pass


##############################################################################
def exercise_22_chained_generator_pipeline():
    """
    Exercise 22: Chained Generator Pipeline
    Problem Statement: Build a three-stage generator pipeline:
        the first stage yields integers from a given range, the
        second filters only prime numbers from that stream, and
        the third formats each prime as a string like "Prime: 7".
        Chain all three stages together without materializing
        any intermediate list. Retrieve and print the
        first 10 results.
    Purpose: This exercise shows the full power of chaining
        generator expressions into a multi-stage pipeline.
        Each stage is a lazy wrapper around the previous one
        — values flow through all three transforms one at a
        time, with no intermediate collections ever built in
        memory. This pattern is the Python equivalent of
        Unix pipes and is the foundation of memory-efficient
        data processing at scale.
    Given Input:
        Integers from 2 to 100.
    Expected Output:
        ['Prime: 2', 'Prime: 3', 'Prime: 5', 'Prime: 7', 'Prime: 11',
         'Prime: 13', 'Prime: 17', 'Prime: 19', 'Prime: 23', 'Prime: 29']
    """
    logger.info("Exercise 22: Chained Generator Pipeline")
    pass


##############################################################################
def exercise_23_row_parser():
    """
    Exercise 23: CSV Row Parser
    Problem Statement: Given a multi-line CSV string, use a
        generator expression to lazily parse it row by row.
        Each yielded value should be a list of stripped
        string values produced by splitting on commas.
        Skip the header row. Consume the generator with a
        for loop and print each parsed row.
    Purpose: In real applications, CSV files can be
        gigabytes in size — far too large to load into
        memory at once. A generator expression over the
        lines of a file (or a string in this exercise)
        reads and parses one row at a time, keeping memory
        usage constant. This exercise builds the habit
        of thinking lazily about row-by-row data
        processing before reaching for a library
        like pandas.
    Given Input:
        A CSV string with a header row and four data rows
        containing name, age, and city fields.
    Expected Output:
        ['Alice', '30', 'New York']
        ['Bob', '25', 'London']
        ['Charlie', '35', 'Tokyo']
        ['Diana', '28', 'Paris']
    """
    logger.info("Exercise 23: CSV Row Parser")
    pass


##############################################################################
def exercise_24_grouped_anagrams():
    """
    Exercise 24: Dict of Grouped Anagrams
    Problem Statement: Given a list of words, group all
        anagrams together into a dictionary where each key
        is the sorted tuple of letters shared by a group,
        and each value is a list of all words from the input
        that are anagrams of one another. Use a dict
        comprehension and sorted() to build the grouping
        in a single pass.
    Given Input:
        words = ["eat", "tea", "tan", "ate", "nat", "bat", "tab"]
    Expected Output:
        {('a', 'e', 't'): ['eat', 'tea', 'ate'],
         ('a', 'n', 't'): ['tan', 'nat'],
         ('a', 'b', 't'): ['bat', 'tab']}
    """
    logger.info("Exercise 24: Grouped Anagrams")
    pass


##############################################################################
def exercise_25_comprehension_generator_testing():
    """
    Exercise 25: Comprehension vs Generator Benchmark
    Problem Statement: Write the same transformation — squaring
        all even numbers from 1 to 100,000 — as both a list
        comprehension and a generator expression. Use
        sys.getsizeof() to compare their memory footprints
        and timeit.timeit() to measure construction time
        and full iteration time for each. Print a clear
        report and explain when each form is preferable.
    Purpose: Knowing that generators are more memory-efficient
        than lists is theoretical until you measure it.
        This exercise makes both differences concrete with
        real numbers, and frames the decision not as
        “generators are always better” but as a trade-off:
        generators win on memory and initial construction
        speed, while lists win when you need random access,
        multiple iterations, or a known length.
        Understanding this trade-off is essential for
        writing Python that is both correct and
        efficient at scale.
    Given Input:
        Even numbers from 1 to 100,000, squared.
    Expected Output:
        --- Memory ---
        List  size: 434,944 bytes
        Gen   size:     208 bytes
        --- Construction time (1000 runs) ---
        List  build: 0.4521s
        Gen   build: 0.0003s
        --- Full iteration time (1000 runs) ---
        List  iter:  0.1843s
        Gen   iter:  0.5102s
    """
    logger.info("Exercise 25: Comprehension vs Generator Benchmark")
    pass