from src.common_library import helper_functions as hf


#
# Exercises found at web page https://pynative.com/python-dictionary-exercise-with-solutions/
# Exercises 21 through 30
#

##############################################################################
def exercise_21_find_max_value():
    """
    Exercise 21: Key of Maximum Value
    Problem Statement: Write a Python program to find the key associated
        with the highest numerical value in a dictionary.
    Purpose: Finding the top-performing key is one of the most common dictionary
        queries used for leaderboards, determining the best-selling product,
        identifying the highest-scoring student, or finding the most frequent
        word in a text analysis.
    Given Input:
        scores = {"Alice": 88, "Bob": 95, "Carol": 72, "Dave": 95, "Eve": 84}
    Expected Output:
        Top scorer: Bob
    """
    print("Exercise 21: Key of Maximum Value")
    scores = {"Alice": 88, "Bob": 95, "Carol": 72, "Dave": 95, "Eve": 84}
    highest_score = max(scores.items(), key=lambda item: item[1])
    print(f"Top scorer: {highest_score[0]}")
    pass



##############################################################################
def exercise_22_create_dictionary_from_tuples():
    """
    Exercise 22: List of Tuples to Dictionary
    Problem Statement: Write a Python program to convert a list of key-value
        tuples into a dictionary without using any loops.
    Purpose: This exercise helps you practice using Python’s built-in dict()
        constructor to transform structured data directly into a dictionary,
        a common pattern in data wrangling and API response parsing.
    Given Input:
        pairs = [("name", "Alice"), ("age", 25), ("city", "Paris")]
    Expected Output:
        {'name': 'Alice', 'age': 25, 'city': 'Paris'}
    """
    print("Exercise 22: List of Tuples to Dictionary")
    pairs = [("name", "Alice"), ("age", 25), ("city", "Paris")]
    results = dict(pairs)
    print(f"{results}")
    pass



##############################################################################
def exercise_23_find_common_keys():
    """
    Exercise 23: Find Common Keys
    Problem Statement: Write a Python program to identify all keys that are present
        in both of two given dictionaries.
    Purpose: This exercise builds your understanding of dictionary views and set operations,
        which are widely used when comparing datasets, merging configurations, or
        validating overlapping fields.
    Given Input:
        d1 = {"a": 1, "b": 2, "c": 3} and d2 = {"b": 20, "c": 30, "d": 40}
    Expected Output:
        Common keys: {'b', 'c'}
    """
    print("Exercise 23: Find Common Keys")
    d1 = {"a": 1, "b": 2, "c": 3}
    d2 = {"b": 20, "c": 30, "d": 40}
    common_keys = set(d1) & set(d2)
    print(f"Common keys: {common_keys}")
    pass



##############################################################################
def exercise_24_dictionary_difference():
    """
    Exercise 24: Dictionary Difference
    Problem Statement: Write a Python program to find all keys that exist in the
        first dictionary but are absent from the second dictionary.
    Purpose: This exercise trains you to use set difference on dictionary views,
        a practical skill for detecting missing fields when comparing records,
        configuration files, or API payloads.
    Given Input:
        d1 = {"a": 1, "b": 2, "c": 3} and d2 = {"b": 20, "d": 40}
    Expected Output:
        Keys only in d1: {'a', 'c'}
    """
    print("Exercise 24: Dictionary Difference")
    d1 = {"a": 1, "b": 2, "c": 3}
    d2 = {"b": 20, "d": 40}
    exclusive_keys = sorted(set(d1).difference(set(d2)))
    print(f"Keys only in d1: {exclusive_keys}")
    pass



##############################################################################
def exercise_25_dictionary_intersection():
    """
    Exercise 25: Dictionary Intersection
    Problem Statement: Write a Python program to create a new dictionary containing
        only the key-value pairs that are identical in both input dictionaries.
    Purpose: This exercise deepens your understanding of dictionary views and dictionary
        comprehensions, useful when reconciling two data sources and keeping only
        the entries they fully agree on.
    Given Input:
        d1 = {"a": 1, "b": 2, "c": 3} and d2 = {"a": 1, "b": 99, "c": 3}
    Expected Output:
        Intersection: {'a': 1, 'c': 3}
    From PyNative website:
        intersection = {k: d1[k] for k in d1.keys() & d2.keys() if d1[k] == d2[k]}
    """
    print("Exercise 25: Dictionary Intersection")
    d1 = {"a": 1, "b": 2, "c": 3}
    d2 = {"a": 1, "b": 99, "c": 3}
    results = {item[0]: item[1] for item in d1.items() for other_item in d2.items() if item[1] == other_item[1]}
    print(f"Intersection: {results}")
    pass



##############################################################################
def exercise_26_word_count():
    """
    Exercise 26: Word Count
    Problem Statement: Write a Python program to count the frequency of each word
        in a string, treating words case-insensitively so that “The” and “the”
        are counted as the same word.
    Purpose: This exercise practises string normalization, splitting, and
        dictionary-based frequency counting, skills that form the foundation of
        text analysis, search indexing, and natural language processing tasks.
    Given Input:
        text = "the cat sat on the mat the cat"
    Expected Output:
        {'the': 3, 'cat': 2, 'sat': 1, 'on': 1, 'mat': 1}
    """
    print("Exercise 26: Word Count")
    text = "the cat sat on the mat the cat"
    words = text.split()
    word_counts = {}
    for word in words:
        word_counts[word] = word_counts.get(word, 0) + 1
    print(f"Word Counts: {word_counts}")
    pass



##############################################################################
def exercise_27_remove_dictionary_items():
    """
    Exercise 27: Remove None Values
    Problem Statement: Write a Python program to remove all key-value pairs
        from a dictionary where the value is None.
    Purpose: This exercise practises filtering dictionaries with a comprehension,
        a pattern that appears frequently when cleaning up API responses,
        database records, or configuration objects that may contain missing
        fields.
    Given Input:
        data = {"name": "Alice", "age": None, "city": "Paris", "score": None}
    Expected Output:
        {'name': 'Alice', 'city': 'Paris'}
    """
    print("Exercise 27: Remove None Values")
    data = {"name": "Alice", "age": None, "city": "Paris", "score": None}
    results = {k: data[k] for k in data.keys() if data[k] is not None}
    print(results)
    pass



##############################################################################
def exercise_28_sort_dictionary_by_keys():
    """
    Exercise 28: Sort Dictionary by Keys
    Problem Statement: Write a Python program to sort a dictionary by its keys and
        return the result as a new dictionary with items in ascending key order.
    Purpose: This exercise practises combining sorted() with dictionary construction,
        a technique useful when producing consistent output for logging, serialization,
        or display purposes.
    Given Input:
        data = {"banana": 3, "apple": 5, "cherry": 1, "date": 4}
    Expected Output:
        {'apple': 5, 'banana': 3, 'cherry': 1, 'date': 4}
    """
    print("Exercise 28: Sort Dictionary by Keys")
    data = {"banana": 3, "apple": 5, "cherry": 1, "date": 4}
    sorted_keys = sorted(data.keys())
    new_data = dict(sorted(data.items()))
    print(new_data)
    pass



##############################################################################
def exercise_29_sort_dictionary_by_values():
    """
    Exercise 29: Sort Dictionary by Values
    Problem Statement: Write a Python program to sort a dictionary’s items based on
        their values in ascending order.
    Purpose: This exercise helps you practice working with dictionary methods, using the
        sorted() function with a custom key, and reconstructing a dictionary from sorted pairs –
        skills useful in ranking, leaderboards, and data ordering tasks.
    Given Input:
        scores = {"Alice": 88, "Bob": 72, "Charlie": 95, "Diana": 60}
    Expected Output:
        {"Diana": 60, "Bob": 72, "Alice": 88, "Charlie": 95}
    """
    print("Exercise 29: Sort Dictionary by Values")
    scores = {"Alice": 88, "Bob": 72, "Charlie": 95, "Diana": 60}
    new_scores = dict(sorted(scores.items(), key=lambda item: item[1]))
    print(new_scores)
    pass



##############################################################################
def exercise_30_unique_values_check():
    """
    Exercise 30: Unique Values Check
    Problem Statement: Write a Python program to check whether all values in a
        dictionary are distinct (i.e., no two keys share the same value).
    Purpose: This exercise helps you practice extracting dictionary values,
        understanding set properties, and comparing lengths to detect duplicates –
        a common pattern in data validation and integrity checks.
    Given Input:
        data = {"a": 1, "b": 2, "c": 3, "d": 2}
    Expected Output:
        False
    """
    def all_unique_values(values):
        data_as_set = set(values)
        return len(data_as_set) == len(values)
    print("Exercise 30: Unique Values Check")
    data = {"a": 1, "b": 2, "c": 3, "d": 2}
    print(all_unique_values(data.values()))
    data = {"a": 1, "b": 2, "c": 3, "d": 23}
    print(all_unique_values(data.values()))
    pass





