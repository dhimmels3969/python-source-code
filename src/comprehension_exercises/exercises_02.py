from common_library.helper_functions import is_prime_number
from src.common_library import helper_functions as hf
import timeit
from collections import defaultdict, deque
import sys
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
    numbers = (n for n in range(2, 101))
    primes = (n for n in numbers if hf.is_prime(n))
    formatted = list(f"Prime: {prime}" for prime in primes)
    results = itertools.islice(formatted, 10)
    logger.info(f"  {list(results)}")
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
    # user_info = "'Name','Age','City'\n'Alice',30,'New York'\n'Bob',25,'London'\n'Charlie',35,'Tokyo'\n'Diana',28,'Paris'"
    user_info = "Name,Age,City\nAlice,30,New York\nBob,25,London\nCharlie,35,Tokyo\nDiana,28,Paris"

    lines = user_info.strip().splitlines()[1:]
    results = list([field.strip() for field in line.split(",")]  for line in lines)
    for user in results:
        logger.info(f"  {user}")
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
    results = {}
    words = ["eat", "tea", "tan", "ate", "nat", "bat", "tab"]
    keys = [tuple(sorted(char for char in word)) for word in words]
    words_with_index = list(zip(keys, words))

    # initialize the dictionary
    results = defaultdict(list)
    # defaultdict(list) is equivalent to the loop below
    # for key, word in words_with_index:
    #     results[key] = []

    # loop through list of words and load the dictionary
    for key, word in words_with_index:
        results[key].append(word)

    # logger.info(f"  {results}")
    for k,v in results.items():
        logger.info(f"  {k}: {v}")

    # Show the comprehension approach -- demonstrates the key idea
    # (last-write-wins, so groups are lost without defaultdict)
    key_demo = {k:v for k,v in words_with_index}
    logger.info(f"  Comprehension only (last word per group):")
    logger.info(f"  {key_demo}")
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

    def build_list(upper_limit):
        return [i**2 for i in range(1,upper_limit) if i %2 ==0]

    def build_gen(upper_limit):
        return (i**2 for i in range(1,upper_limit) if i %2 ==0)

    logger.info("Exercise 25: Comprehension vs Generator Benchmark")
    list_message, gen_message = "", ""
    upper_limit = 100_000
    RUNS = 1000
    squares_list = build_list(upper_limit + 1)
    squares_gen  = build_gen(upper_limit + 1)
    ###############  MEMORY USAGE ###################
    logger.info(f"  ------ Memory ------")
    logger.info(f"  List size: {sys.getsizeof(squares_list):,}")
    logger.info(f"  Gen  size: {sys.getsizeof(squares_gen):,}")

    ###############  CONSTRUCTION TIME ###################
    logger.info(f"  ------ Construction time (1000 runs) ------")
    list_build_time = timeit.timeit(
        lambda: [x ** 2 for x in range(1, upper_limit + 1) if x % 2 == 0],
        number=RUNS
    )
    list_message = f"List build - 1000 runs took: {list_build_time:.6f} seconds"

    gen_build_time = timeit.timeit(
        lambda: (x ** 2 for x in range(1, upper_limit + 1) if x % 2 == 0),
        number=RUNS
    )
    gen_message = f"Gen build - 1000 runs took: {gen_build_time:.6f} seconds"

    logger.info(f"  {list_message}")
    logger.info(f"  {gen_message}")

    ###############  ITERATION TIME ###################
    # List: iterate a pre-built list
    list_iter_time = timeit.timeit(
        lambda: deque([x ** 2 for x in range(1, upper_limit + 1) if x % 2 == 0], maxlen=0),
        number=RUNS
    )
    # Generator: build and fully consume in the same call
    gen_iter_time = timeit.timeit(
        lambda: deque((x ** 2 for x in range(1, upper_limit + 1) if x % 2 == 0), maxlen=0),
        number=RUNS
    )

    logger.info(f"  --- Full iteration time ({RUNS:,} runs) ---")
    logger.info(f"  List  iter:  {list_iter_time:.4f}seconds")
    logger.info(f"  Gen   iter:  {gen_iter_time:.4f}seconds")

    # try:
    #     t = timeit.timeit(stmt=list_builder, number=1_000_000)
    #     # timer = timeit.Timer("build_list(100001)", "build a list")
    #     # t = timer.timeit(number=1000)
    #     list_message = f"List build - 1000 runs took: {t:.6f} seconds"
    # except Exception as e:
    #     print(f"Timer error: {e}")
    pass



###########################################################################
#### Following code verified: 2026-06-21
###########################################################################
#
# my_code = """
# total = 0
# for i in range(500):
#    total += 1
# """
# def timer_test():
#     time_taken = timeit.timeit(my_code)
#     logger.info(f"==========>>>>  Total time taken: {time_taken:,.6f} seconds.")
#     pass
###########################################################################
