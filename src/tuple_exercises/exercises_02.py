from src.common_library import helper_functions as hf
from collections.abc import Iterable
from typing import NamedTuple
import sys


#
# Exercises found at web page https://pynative.com/python-tuple-exercise-with-solutions/
# Exercises 13-14 and 22 through 32
#



##############################################################################
def exercise_13_nested_tuple_access():
    """
    Exercise 13: Nested Tuple Access
    Problem Statement: Write a Python program to access a specific element
        that is stored inside a tuple which is itself nested
        inside another tuple.
    Purpose: This exercise builds your understanding of nested data
    structures. Tuples can contain other tuples as elements, and chaining
    index operators is the standard way to drill down into them. This
    pattern appears frequently when working with coordinate grids,
    database records, and configuration structures.
    Given Input:
        matrix = ((1, 2, 3), (4, 5, 6), (7, 8, 9))
    Expected Output:
        6
    """
    print("Exercise 13: Nested Tuple Access")
    matrix = ((1, 2, 3), (4, 5, 6), (7, 8, 9))
    results = matrix[1][2]
    print(results)
    pass



##############################################################################
def exercise_14_tuple_stats_check():
    """
    Exercise 14: Tuple Statistics
    Problem Statement: Write a Python program to calculate the total,
        highest value, and lowest value from a tuple of integers using
        the built-in sum(), max(), and min() functions.
    Purpose: This exercise shows that Python’s built-in aggregate
        functions work directly on tuples, not just lists. Being able
        to derive quick statistics from an immutable sequence without
        converting it first is a practical time-saver in data
        processing and reporting tasks.
    Given Input:
        scores = (88, 95, 70, 62, 99, 74, 85)
    Expected Output:
        Sum: 573, Max: 99, and Min: 62
    """
    print("Exercise 14: Tuple Statistics")
    scores = (88, 95, 70, 62, 99, 74, 85)
    sum_ = sum(scores)
    max_ = max(scores)
    min_ = min(scores)
    print(f"Sum:{sum_}, Max: {max_}, and Min: {min_}")
    pass



##############################################################################
def exercise_22_tuple_sort_check():
    """
    Exercise 22: Sort Tuple of Tuples
    Problem Statement: Write a Python program to sort a tuple of tuples
        based on the second item in each nested tuple.
    Purpose: This exercise teaches you how to use the key parameter of
        Python’s sorted() function with a lambda to sort structured data
        by a specific field – a technique used constantly when ordering
        records, rankings, and tabular data.
    Given Input:
        students = (("Alice", 88), ("Bob", 73), ("Charlie", 95), ("Diana", 61))
    Expected Output:
        Sorted: (('Diana', 61), ('Bob', 73), ('Alice', 88), ('Charlie', 95))
    """
    print("Exercise 22: Sort Tuple of Tuples")
    students = (("Alice", 88), ("Bob", 73), ("Charlie", 95), ("Diana", 61))
    results = tuple(sorted(students, key=lambda item: item[1]))
    print(f"Sorted: {results}")
    pass



##############################################################################
def exercise_23_tuple_filtering():
    """
    Exercise 23: Tuple Filtering
    Problem Statement: Write a Python program to filter a tuple and
        keep only the elements that satisfy a given condition, using
        both filter() and a list comprehension approach.
    Purpose: This exercise demonstrates two idiomatic ways to select
        a subset of items from a sequence based on a condition.
        Filtering is a foundational operation in data processing,
        validation, and functional-style programming.
    Given Input:
        numbers = (3, 14, 7, 22, 9, 41, 18, 5), keep only values greater than 10
    Expected Output:
        Filtered: (14, 22, 41, 18)
    Additional Information:
        tuple(filter(lambda x: x > 10, numbers)) and tuple(n for n in numbers if n > 10)
        produce the same results.
    """
    print("Exercise 23: Tuple Filtering")
    numbers = (3, 14, 7, 22, 9, 41, 18, 5)
    filtered = tuple(x for x in numbers if x > 10)
    print(f"Filtered: {filtered}")
    pass



##############################################################################
def exercise_24_tuple_mapping():
    """
    Exercise 24: Tuple Mapping
    Problem Statement: Write a Python program to apply a square function
        to every item in a tuple using map(), and also demonstrate the
        equivalent generator expression approach.
    Purpose: This exercise introduces the functional programming concept
        of mapping a transformation over a sequence. The map() function
        and its comprehension equivalent appear regularly in data
        transformation, preprocessing pipelines, and mathematical
        computations.
    Given Input:
        numbers = (1, 2, 3, 4, 5, 6)
    Expected Output:
        Squared: (1, 4, 9, 16, 25, 36)
    Additional Information:
        tuple(map(lambda x: x**2, numbers)) and tuple(x**2 for x in numbers)
        produce the same results.
    """
    print("Exercise 24: Tuple Mapping")
    numbers = (1, 2, 3, 4, 5, 6)
    squared = tuple(x**2 for x in numbers)
    print(f"Squared: {squared}")
    pass



##############################################################################
def exercise_25_tuple_dictionary_mapping():
    """
    Exercise 25: Tuple Dictionary Mapping
    Problem Statement: Write a Python program to zip two tuples
        together – one holding keys and the other holding values –
        to create a dictionary.
    Purpose: This exercise demonstrates a common pattern for building
        dictionaries from paired data sources. Combining zip() with
        dict() is widely used when parsing CSV headers, mapping
        configuration keys to values, and constructing lookup tables
        from separate lists.
    Given Input:
        keys = ("name", "age", "city") and values = ("Alice", 30, "Pune")
    Expected Output:
        {'name': 'Alice', 'age': 30, 'city': 'Pune'}
    """
    print("Exercise 25: Tuple Dictionary Mapping")
    keys = ("name", "age", "city")
    values = ("Alice", 30, "Pune")
    results = dict(zip(keys, values))
    print(f"{results}")
    pass



##############################################################################
def exercise_26_tuple_intersection():
    """
    Exercise 26: Tuple Intersection
    Problem Statement: Write a Python program to find all elements that
        are common to two different tuples.
    Purpose: This exercise introduces set intersection as a tool for
        comparing collections. Finding shared elements between two
        sequences is a core operation in data analysis, deduplication,
        access control (shared permissions), and any scenario where
        you need to identify overlap between datasets.
    Given Input:
        t1 = (1, 2, 3, 4, 5, 6) and t2 = (4, 5, 6, 7, 8, 9)
    Expected Output:
        Common elements: (4, 5, 6)
    Additional Information:
        tuple(set(t1).intersection(t2)) and tuple(set(t1) & set(t2))
        produce the same results.
    """
    print("Exercise 26: Tuple Intersection")
    t1 = (1, 2, 3, 4, 5, 6)
    t2 = (4, 5, 6, 7, 8, 9)
    results = tuple(set(t1).intersection(t2))
    print(f"Common elements: {results}")
    pass



##############################################################################
def exercise_27_modification_hack_test():
    """
    Exercise 27: The “Modification” Hack
    Problem Statement: Write a Python program to “modify” a tuple by
        converting it to a list, changing a specific item, and
        converting it back to a tuple.
    Purpose: This exercise highlights the immutability of tuples and
        demonstrates the standard workaround used when a one-off
        change is needed. Understanding this pattern also helps you
        appreciate why tuples are immutable by design and when to
        choose a list instead.
    Given Input:
        colours = ("red", "green", "blue"), replace "green" with "yellow"
    Expected Output:
        Original: ('red', 'green', 'blue')
        Modified: ('red', 'yellow', 'blue')
    """
    print("Exercise 27: Tuple Modification")
    colours = ("red", "green", "blue")
    colours_list = list(colours)
    colours_list[1] = "yellow"
    results = tuple(colours_list)
    print(f"Original: {colours}")
    print(f"Modified: {results}")
    pass



##############################################################################
def exercise_28_tuple_mutability_check():
    """
    Exercise 28: Tuple Mutability
    Problem Statement: Create a tuple that contains a list as one of
        its elements. Modify the list in place and observe that
        the tuple’s identity stays the same while its contents appear
        to change.
    Purpose: This exercise uncovers one of Python’s most instructive
        subtleties: a tuple is immutable in the sense that its references
        cannot be reassigned, but if a reference points to a mutable object
        such as a list, that object itself can still be changed.
        Understanding this distinction is essential for writing
        predictable, bug-free code.
    Given Input: t = (1, 2, [3, 4, 5]), append 99 to the inner list
    Expected Output:
        Before: (1, 2, [3, 4, 5])
        After:  (1, 2, [3, 4, 5, 99])
        Same object? True
    """
    print("Exercise 28: Tuple Mutability")
    t = (1, 2, [3, 4, 5])
    print(f"Before: {t}")
    id_before = id(t)
    t[2].append(99)
    id_after  = id(t)
    print(f"After: {t}")
    print(f"Same object? {id_before == id_after}")
    pass



##############################################################################
def exercise_29_flatten_nested_tuples():
    """
    Exercise 29: Nested Tuple Flattening
    Problem Statement: Write a recursive Python function to flatten a
        deeply nested tuple of tuples into a single flat tuple
        containing all the individual values.
    Purpose: This exercise strengthens your understanding of recursion
        and type checking. Flattening nested structures is a practical
        requirement when processing tree-shaped data, parsed expressions,
        or hierarchical configurations where depth is not known
        in advance.
    Given Input:
        nested = (1, (2, 3), (4, (5, (6, 7))))
    Expected Output:
        Flattened: (1, 2, 3, 4, 5, 6, 7)

    PyNative solution:
        def flatten(t):
            for item in t:
                if isinstance(item, tuple):
                    yield from flatten(item)
                else:
                    yield item
        ####
        nested = (1, (2, 3), (4, (5, (6, 7))))
        result = tuple(flatten(nested))
        print("Flattened:", result)
    """

    def flatten2(payload_, results_):
        for item in payload_:
            if isinstance(item, tuple):
                flatten(item, results_)
            else:
                results_.append(item)
        return results_

    def flatten(payload_, results_):
        for item in payload_:
            if isinstance(item, dict):
                for v in item.values():
                    flatten(v, results_)
            elif isinstance(item, Iterable) and not isinstance(item, (str, bytes)):
                flatten(item, results_)
            else:
                results_.append(item)
        return results_

    print("Exercise 29: Nested Tuple Flattening")
    nested = (1, (2, 3), (4, (5, (6, 7))))
    nested = (1, (2, 3), ("a", "b", "c") , (11, 122, 233, (5, 58, (99, (201,)))), (4, (5, (6, 7)))
                , 13, 21, 34, ((55,), (89,), (144,)
                , (233, 377, 255, 40840, (5,6,7,(9,10,11, (31,42,53,64))))))
    nested = (1, (2, 3), (4, (5, (6, 7, (8,9,(10, 11, (12, 13, 14, 15, 16))))))
              , [99, 98, 97, 96, 95], sorted({"a", "b", "c", "d", "e", "f"})
              )
              # , {"N": "North", "S": "South", "E": "East", "W": "West"})

    results = flatten(nested, [])
    print(f"Tuple Before: {nested}")
    print(f"Flattened: {tuple(results)}")
    pass



##############################################################################
def exercise_30_memory_efficiency_check():
    """
    Exercise 30: Memory Efficiency
    Problem Statement: Use the sys module to measure and compare the
        memory consumed by a list and a tuple, each holding the
        same one million integer elements.
    Purpose: This exercise gives you concrete, measurable evidence
        for one of the key practical advantages of tuples over lists:
        lower memory overhead. This matters in performance-sensitive
        applications that hold large collections of fixed
        data in memory.
    Given Input:
        A range of one million integers, range(1_000_000),
        stored as both a list and a tuple
    Expected Output:
        Printed byte sizes for the list and the tuple,
        followed by the difference in bytes (exact values vary by
        Python version and platform)
    References:
        https://stackabuse.com/bytes/determining-the-size-of-an-object-in-python/
    """
    print("Exercise 30: Memory Efficiency")
    big_list = [x for x in range(1_000_000)]
    big_tuple = tuple(big_list)
    # get the size for both objects...
    list_size_in_bytes = sys.getsizeof(big_list)
    tuple_size_in_bytes = sys.getsizeof(big_tuple)
    difference_in_bytes = list_size_in_bytes - tuple_size_in_bytes
    print(f"Size of List: {list_size_in_bytes:,}")
    print(f"Size of Tuple: {tuple_size_in_bytes:,}")
    # print(f"Difference in Bytes: {difference_in_bytes:,}")
    print(f"Difference: {difference_in_bytes:,} bytes ({difference_in_bytes / 1024:.2f} KB)")
    pass



##############################################################################
def exercise_31_named_tuples_test():
    """
    Exercise 31: NamedTuples
    Problem Statement: Use collections.namedtuple to define an Employee
        data structure with named fields, create a few instances,
        and perform a calculation such as finding the highest-paid
        employee.
    Purpose: This exercise introduces namedtuple as a lightweight way
        to create readable, self-documenting data objects without the
        overhead of a full class. Named tuples are used extensively
        in standard library code, data pipelines, and anywhere
        structured records need to be passed around efficiently.
    Given Input:
        Three employees – ("Alice", "Engineering", 95000),
            ("Bob", "Marketing", 72000), ("Charlie", "Engineering", 88000)
    Expected Output:
        Alice works in Engineering and earns $95,000
        Bob works in Marketing and earns $72,000
        Charlie works in Engineering and earns $88,000
        Highest paid: Alice ($95,000)
    """
    class Employee(NamedTuple):
        name: str
        department: str
        salary: int

    print("Exercise 31: NamedTuples")
    employee_list = [Employee("Alice", "Engineering", 95000), Employee("Bob", "Marketing", 72000),
                     Employee("Charlie", "Engineering", 88000)]
    employee_list_tuple = tuple(employee_list)
    for employee in employee_list_tuple:
        print(f"{employee.name} works in {employee.department} and earns ${employee.salary:,}")
    highest_paid = sorted(employee_list_tuple, key=lambda x: x.salary, reverse=True)[0]
    print(f"Highest Paid: {highest_paid.name} (${highest_paid.salary:,})")
    pass



##############################################################################
def exercise_32_tuple_hashability():
    """
    Exercise 32: The Hashability Paradox
    Problem Statement: Write a Python program that experiments with using
        tuples as dictionary keys. Demonstrate why a fully immutable tuple
        like (1, 2) works as a key, while a tuple containing a mutable
        object like (1, [2]) raises a TypeError.
    Purpose: This exercise builds a deep understanding of Python’s
        hashing rules. Dictionary keys must be hashable, meaning their
        value must never change after being inserted. A tuple containing
        a mutable list violates this guarantee, which is why Python
        rejects it. This concept is fundamental to understanding how
        sets and dictionaries work internally.
    Given Input:
        Attempt to use (1, 2) and (1, [2]) as dictionary keys
    Expected Output:
        (1, 2) as key: success, value = "immutable tuple"
        (1, [2]) as key: TypeError - unhashable type: 'list'
    """
    print("Exercise 32: The Hashability Paradox")
    my_dictionary = {}
    valid_key = (1, 2)
    invalid_key = (1, [2])
    try:
        my_dictionary[valid_key] = "immutable tuple"
        print(f"{valid_key} as key: success, value = '{my_dictionary[valid_key]}'")
    except TypeError as e:
        print(f"TypeError: {e}")

    try:
        my_dictionary[invalid_key] = "ABCDEFGHIJKL" * 10
    except TypeError as e:
        print(f"{invalid_key} as key: TypeError: {e}")
    pass




