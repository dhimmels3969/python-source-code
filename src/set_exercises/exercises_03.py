from src.common_library import helper_functions as hf
import time
import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

#
# Exercises found at web page https://pynative.com/python-set-exercise-with-solutions/
# Exercises 21 through 31
#



##############################################################################
def exercise_21_common_elements_check():
    """
    Exercise 21: Find Common Elements in Lists
    Problem Statement: Write a Python program to find the common elements
        between two lists by converting them to sets and using the
        intersection operation.
    Purpose: This exercise shows how sets can solve a practical problem
        more elegantly than nested loops. Converting lists to sets before
        intersecting them removes duplicates and enables fast lookup,
        making the approach both concise and efficient.
    Given Input:
        list1 = [1, 2, 3, 4, 5, 3, 2] and list2 = [3, 4, 5, 6, 7, 4, 5]
    Expected Output:
        common = {3, 4, 5}
    """
    logger.info("Exercise 21: Find Common Elements in Lists")
    list1 = [1, 2, 3, 4, 5, 3, 2]
    list2 = [3, 4, 5, 6, 7, 4, 5]
    results = set(list1).intersection(set(list2))
    logger.info(f"  common = {results}")
    pass



##############################################################################
def exercise_22_count_unique_words():
    """
    Exercise 22: Count Unique Words
    Problem Statement: Write a Python program to process a string and
        find the total number of unique words it contains,
        ignoring case differences.
    Purpose: This exercise shows how sets can be used to deduplicate
        data from a real-world source. Converting words to a set is a
        fast and idiomatic way to count distinct tokens, a technique
        used in text analysis, search engines, and natural language
        processing pipelines.
    Given Input:
        text = "the cat sat on the mat the cat"
    Expected Output:
        Unique word count: 5
    """
    logger.info("Exercise 22: Count Unique Words")
    text = "the cat sat on the mat the cat"
    words = set(text.split())
    logger.info(f"  Unique word count: {len(words)}")
    pass



##############################################################################
def exercise_23_convert_to_joined_string():
    """
    Exercise 23: Convert Set to Joined String
    Problem Statement: Write a Python program to convert a set of words
        into a single string where each element is separated
        by a specified delimiter.
    Purpose: This exercise practises combining set data back into
        a human-readable string. Joining a set is commonly needed when
        generating comma-separated values, building display labels
        from tags, or serializing a set of identifiers into a single field.
    Given Input:
        tags = {"python", "set", "programming", "tutorial"}
    Expected Output:
        A single string with all tags joined by " | " (order may vary)
    """
    logger.info("Exercise 23: Convert Set to Joined String")
    tags = {"python", "set", "programming", "tutorial"}
    results = " | ".join(tags)
    logger.info(f"  Joined string: {results}")
    pass



##############################################################################
def exercise_24_proper_subset_superset():
    """
    Exercise 24: Proper Subset and Superset
    Problem Statement: Write a Python program to check whether one set
        is a proper subset and another is a proper superset using
        the < and > operators.
    Purpose: This exercise clarifies the difference between regular
        and proper subset/superset relationships. Understanding strict
        comparisons is useful when validating permissions, checking
        feature flag hierarchies, or verifying that one group of
        items is strictly contained within another.
    Given Input:
        a = {1, 2, 3} and b = {1, 2, 3, 4, 5}
    Expected Output:
        a is a proper subset of b: True
        b is a proper superset of a: True
        a is a proper subset of a: False
    """
    logger.info("Exercise 24: Proper Subset and Superset")
    a = {1, 2, 3}
    b = {1, 2, 3, 4, 5}
    logger.info(f"  a is a proper subset of b: {a < b}")
    logger.info(f"  b is a proper superset of a: {b > a}")
    logger.info(f"  a is a proper subset of a: {a < a}")
    pass



##############################################################################
def exercise_25_frozenset_check():
    """
    Exercise 25: Frozen Set
    Problem Statement: Write a Python program to create a frozenset, demonstrate
        that set operations work on it, and confirm that any attempt to modify
        it raises a TypeError.
    Purpose: This exercise introduces immutability in the context of sets.
        A frozenset can be used as a dictionary key or stored inside another
        set, making it valuable when you need a hashable, read-only collection,
        such as representing a fixed combination of permissions or
        configuration flags.
    Given Input:
        fs = frozenset([1, 2, 3, 4, 5])
    Expected Output:
        frozenset: frozenset({1, 2, 3, 4, 5})
        Intersection with {3, 4, 5, 6}: frozenset({3, 4, 5})
        Error: 'frozenset' object has no attribute 'add'
    Additional information:
        "fs.intersection(set_02)" and "fs & set_02" produce the same results.
    """
    logger.info("Exercise 25: Frozen Set")
    fs = frozenset([1, 2, 3, 4, 5])
    set_02 = {3, 4, 5, 6}
    logger.info(f"  frozenset: {fs}")
    logger.info(f"  Intersection with {3, 4, 5, 6}: {fs.intersection(set_02)}")
    # try to add an item to frozenset fs... will result in an error (AttributeError)
    try:
        fs.add(100)
    except AttributeError as e:
        logger.error(f"  Error: {e}")
    pass



##############################################################################
def exercise_26_set_comprehension():
    """
    Exercise 26: Set Comprehension
    Problem Statement: Write a Python program to generate a set of squares
        of all even numbers from 1 to 20 using a set comprehension
        in a single line.
    Purpose: This exercise demonstrates set comprehensions as a concise
        and readable alternative to building sets with loops. They follow
        the same syntax as list comprehensions but produce a set, ensuring
        all resulting values are automatically deduplicated.
    Given Input:
        Numbers from 1 to 20 (inclusive)
    Expected Output:
        {4, 16, 36, 64, 100, 144, 196, 256, 324, 400}
    """
    logger.info("Exercise 26: Set Comprehension")
    set_of_squares = sorted({x**2 for x in range(1,21,1) if x %2 == 0})
    logger.info(f"  {set_of_squares}")
    pass



##############################################################################
def exercise_27_remove_duplicates_preserve_order():
    """
    Exercise 27: Remove Duplicates (Preserving Order)
    Problem Statement: Write a Python program to remove duplicate values
        from a list while preserving the original order of first
        appearances.
    Purpose: Converting a list directly to a set removes duplicates but
        loses order. This exercise teaches a practical pattern that
        combines the deduplication power of a set with the ordering
        properties of a list, commonly needed in data cleaning,
        deduplication pipelines, and maintaining insertion-ordered
        unique sequences.
    Given Input:
        items = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
    Expected Output:
        [3, 1, 4, 5, 9, 2, 6]
    """
    logger.info("Exercise 27: Remove Duplicates (Preserving Order)")
    items = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
    seen = set()
    results = []
    for item in items:
        if item not in seen:
            seen.add(item)
            results.append(item)
    logger.info(f"  {results}")
    pass



##############################################################################
def exercise_28_multiset_difference():
    """
    Exercise 28: Multi-Set Difference
    Problem Statement: Write a Python program to find all elements
        that are in Set A but not present in either Set B or Set C.
    Purpose: This exercise extends the two-set difference operation to
        multiple sets. It is practical in scenarios such as finding
        users who have not yet completed any of several onboarding steps
        , or items in a master list that have not been processed by
        any of several workers.
    Given Input:
        A = {1, 2, 3, 4, 5, 6, 7, 8}
        B = {2, 4, 6}
        C = {5, 7, 9}
    Expected Output:
        Result: {1, 3, 8}
    Additional information:
        "A - B - C" and "A.difference(B).difference(C)" produce the same results
    """
    logger.info("Exercise 28: Multi-Set Difference")
    A = {1, 2, 3, 4, 5, 6, 7, 8}
    B = {2, 4, 6}
    C = {5, 7, 9}
    logger.info(f"  Result: {A.difference(B).difference(C)}")
    pass



##############################################################################
def exercise_29_tuples_test():
    """
    Exercise 29: Set of Tuples
    Problem Statement: Write a Python program to demonstrate that a set
        can store tuples as elements but cannot store lists, and explain
        why this difference exists.
    Purpose: This exercise builds a concrete understanding of hashability,
        the property that determines which types can live inside a set
        or be used as dictionary keys. Knowing why lists are rejected
        and tuples are accepted prevents common bugs when working with
        collections of compound values.
    Given Input:
        A set containing tuples, then an attempt to add a list as an element
    Expected Output:
        Set of tuples: {(1, 2), (3, 4), (5, 6)}
        Error: unhashable type: 'list'
    """
    logger.info("Exercise 29: Set Comparison")
    results = set()
    a = (1,2)
    b = (3,4)
    c = (5,6)
    myList = [1,2,3,4,5,6]
    results.add(a)
    results.add(b)
    results.add(c)
    # attempting to add a list to the set results in a TypeError
    try:
        results.add(myList)
    except TypeError as e:
        logger.info(f"  Error: {e}")

    pass



##############################################################################
def exercise_30_shallow_copy_test():
    """
    Exercise 30: Shallow Copy vs. Assignment
    Problem Statement: Write a Python program to demonstrate the difference
        between assigning a set to a new variable with = and creating
        an independent copy using the .copy() method.
    Purpose: This exercise addresses one of the most common sources of
        subtle bugs in Python: confusing reference assignment with object
        copying. Understanding this distinction is essential whenever
        you intend to work with a separate version of a collection
        without affecting the original.
    Given Input:
        original = {1, 2, 3, 4, 5}
    Expected Output:
        --- Assignment (=) ---
        original: {1, 2, 3, 4, 5, 99}
        ref: {1, 2, 3, 4, 5, 99}
        --- Shallow copy (.copy()) ---
        original: {1, 2, 3, 4, 5}
        copied: {1, 2, 3, 4, 5, 42}
    """
    logger.info("Exercise 30: Shallow Copy vs. Assignment")
    original = {1, 2, 3, 4, 5}
    ref_copy = original
    original.add(99)
    logger.info(f"  --- Assignment (=) ---")
    logger.info(f"  original: {original}")
    logger.info(f"  ref: {ref_copy}")

    # restore original
    original.remove(99)
    shallow_copy = original.copy()
    # original.add(43)
    shallow_copy.add(42)
    logger.info(f"  --- Shallow copy (.copy()) ---")
    logger.info(f"  original: {original}")
    logger.info(f"  copied: {shallow_copy}")
    pass



##############################################################################
def exercise_31_test_performance():
    """
    Exercise 31: Membership Testing Performance
    Problem Statement: Write a Python program to compare the time taken to check
        whether an item exists in a large list versus a large set, and observe
        the performance difference.
    Purpose: This exercise makes the performance advantage of sets concrete and
        measurable. Membership testing is one of the most frequent operations in
        programming, and switching from a list to a set can reduce lookup time
        from O(n) to O(1) on average – a critical optimization for large datasets.
    Given Input: A range of 1,000,000 integers, searching for 999999
    Expected Output:
        List lookup time:  0.008542 seconds
        Set lookup time:   0.000001 seconds
    """
    def elapsed_time(object_, lookup_):
        results = False
        start = time.time()
        results = lookup_ in object_
        end = time.time()
        elapsed_time = end - start
        return elapsed_time

    logger.info("Exercise 31: Membership Testing Performance")
    myList = list(range(1_000_000))
    mySet = set(myList)
    search_arg = 999_999

    list_lookup_time = elapsed_time(myList, search_arg)
    set_lookup_time = elapsed_time(mySet, search_arg)
    logger.info(f"  List lookup time: {list_lookup_time:.6f} seconds")
    logger.info(f"  Set lookup time: {set_lookup_time:.6f} seconds")


    pass



