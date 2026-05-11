import json
import copy
from unittest import result
from src.common_library import helper_functions as hf


#
# Exercises found at web page https://pynative.com/python-dictionary-exercise-with-solutions/
# Exercises 31 through 40
#

##############################################################################
def exercise_31_check_for_subset():
    """
    Exercise 31: Check for Subset
    Problem Statement: Write a Python program to verify whether one
        dictionary is a subset of another, meaning all key-value pairs
        of the smaller dictionary exist in the larger one.
    Purpose: This exercise helps you practice dictionary comparison,
        use of the .items() method, and set operations – techniques
        commonly used in configuration matching, permission checks,
        and data filtering.
    Given Input:
        main = {"a": 1, "b": 2, "c": 3, "d": 4} and subset = {"a": 1, "c": 3}
    Expected Output:
        True
    """
    def is_subset(dict_main, dict_subset):
        # results = ( set(dict_main.items()).intersection(set(dict_subset.items())) == set(dict_subset.items()))
        # return results
        return ( set(dict_main.items()).intersection(set(dict_subset.items())) == set(dict_subset.items()))

    print("Exercise 31: Check for Subset")
    main = {"a": 1, "b": 2, "c": 3, "d": 4}
    subset = {"a": 1, "c": 3}
    subset2 = {"a": 1, "b": 2, "y": 25}
    print(is_subset(main, subset2))
    print(is_subset(main, subset))
    pass



##############################################################################
def exercise_32_sort_by_value_length():
    """
    Exercise 32: Sort Dictionary by Value Length
    Problem Statement: Write a Python program to sort a dictionary’s items
        by the length of their string values, from shortest to longest.
    Purpose: This exercise helps you practice combining sorted() with a
        custom key function, working with string properties inside dictionaries,
        and rebuilding ordered dictionaries – useful in text processing
        and display formatting tasks.
    Given Input:
        words = {"a": "banana", "b": "kiwi", "c": "strawberry", "d": "fig"}
    Expected Output:
        {"d": "fig", "b": "kiwi", "a": "banana", "c": "strawberry"}
    """
    print("Exercise 32: Sort Dictionary by Value Length")
    words = {"a": "banana", "b": "kiwi", "c": "strawberry", "d": "fig"}
    revised_words = dict(sorted(words.items(), key=lambda item: len(item[1])))
    print(revised_words)
    pass



##############################################################################
def exercise_33_key_with_longest_list():
    """
    Exercise 33: Key with Longest List
    Problem Statement: Write a Python program to find the key in a dictionary
        whose associated list value has the greatest number of elements.
    Purpose: This exercise helps you practice using max() with a custom key on
        dictionary items, working with list values, and extracting meaningful
        information from nested data structures – patterns common in analytics
        and data aggregation.
    Given Input:
        data = {"fruits": ["apple", "banana", "cherry"], "vegs": ["carrot"], "grains": ["rice", "wheat"]}
    Expected Output:
        fruits
    from PyNative website
        longest_key = max(data.items(), key=lambda item: len(item[1]))[0]
    """
    print("Exercise 33: Find Key")
    data = {"fruits": ["apple", "banana", "cherry"], "vegs": ["carrot"], "grains": ["rice", "wheat"]}
    # revised_data = dict(sorted(data.items(), key=lambda item: len(item[1]), reverse = True))
    largest_sublist = max(data.items(), key=lambda item: len(item[1]))
    # display the key of the largest sublist...
    print(largest_sublist[0])
    pass



##############################################################################
def exercise_34_convert_dictionary_to_json():
    """
    Exercise 34: Convert Dictionary to JSON
    Problem Statement: Write a Python program to convert a nested dictionary
        into a formatted JSON string with readable indentation.
    Purpose: This exercise helps you practice using Python’s built-in json module,
        serializing complex data structures, and controlling output formatting –
        skills essential for APIs, configuration files, and data interchange between systems.
    Given Input:
        person = {"name": "Alice", "age": 30, "address": {"city": "Mumbai", "pin": "400001"}}
    Expected Output:
        {
            "name": "Alice",
            "age": 30,
            "address": {
                "city": "Mumbai",
                "pin": "400001"
            }
        }
    """
    print("Exercise 34: Convert Dictionary to JSON")
    person = {"name": "Alice", "age": 30, "address": {"city": "Mumbai", "pin": "400001"}}
    results = json.dumps(person, sort_keys=False, indent=4)
    print(results)
    pass



##############################################################################
def exercise_35_invert_dictionary():
    """
    Exercise 35: Invert Dictionary
    Problem Statement: Write a Python program to invert a dictionary by
        swapping its keys and values, so each original value becomes a key
        and each original key becomes the corresponding value.
    Purpose: This exercise helps you practice dictionary comprehensions,
        understanding key uniqueness constraints, and transforming data
        structures – a technique used in reverse lookups, encoding/decoding
        maps, and symbol tables.
    Given Input:
        original = {"a": 1, "b": 2, "c": 3}
    Expected Output:
        {1: "a", 2: "b", 3: "c"}
    """
    print("Exercise 35: Invert Dictionary")
    original = {"a": 1, "b": 2, "c": 3}
    # revised = {k[1]: k[0] for k in original.items()}
    # from Pynative website
    inverted = {v: k for k, v in original.items()}
    print(inverted)
    pass



##############################################################################
def exercise_36_invert_with_duplicate_values():
    """
    Exercise 36: Invert with Duplicate Values
    Problem Statement: Write a Python program to invert a dictionary
        where multiple keys may share the same value. Instead of overwriting,
        group all original keys that map to the same value into a list under
        that value as the new key.
    Purpose: This exercise helps you practice handling collisions during
        dictionary inversion, using setdefault() or defaultdict, and building
        grouped structures from flat data – a pattern common in indexing,
        tagging systems, and reverse lookups.
    Given Input:
        original = {"a": 1, "b": 2, "c": 1, "d": 3, "e": 2}
    Expected Output:
        {1: ["a", "c"], 2: ["b", "e"], 3: ["d"]}
    From PyNative website:
        inverted = {}
        for k, v in original.items():
            inverted.setdefault(v, []).append(k)
    """
    print("Exercise 36: Invert with Duplicate Values")
    original = {"a": 1, "b": 2, "c": 1, "d": 3, "e": 2}
    results = {}
    for pairs in original.items():
        results[pairs[1]] = results.setdefault(pairs[1], []) + [pairs[0]]
    print(results)
    pass



##############################################################################
def exercise_37_flatten_nested_dictionary():
    """
    Exercise 37: Flatten Nested Dictionary
    Problem Statement: Write a Python program to flatten a multi-level nested
        dictionary into a single-level dictionary, joining nested keys with
        a dot separator to form the new keys.
    Purpose: This exercise helps you practice recursive thinking
        , string key construction, and traversing nested data structures –
        skills used in configuration parsing, JSON flattening for databases
        , and working with API responses.
    Given Input:
        nested = {"a": 1, "b": {"c": 2, "d": {"e": 3, "f": 4}}}
    Expected Output:
        {"a": 1, "b.c": 2, "b.d.e": 3, "b.d.f": 4}
    From PyNative website:
        def flatten(d, prefix=""):
        result = {}
        for k, v in d.items():
            new_key = f"{prefix}.{k}" if prefix else k
            if isinstance(v, dict):
                result.update(flatten(v, new_key))
            else:
                result[new_key] = v
        return result
    """
    def initialize(a, b):
        """
        Initialize  objects that will be used in the recursive flatten function.
        :param a:   dictionary used to store the flattened results
        :type a:    dictionary
        :param b:   list used to build the keys for the flattened dictionary
        :type b:    list
        :return:    the initialized dictionary and the initialized list
        :rtype:     dictionary, list
        """
        a = {}
        b = []
        return a, b

    def flatten(payload_, results_, parent_):
        for k,v in payload_.items():
            parent_.append(k)
            if isinstance(v, dict):
                flatten(v, results_, parent_)
            else:
                key_ = ".".join(parent_)
                results_[key_] = v

            # remove the last item in the list
            # need to use indexing because it's possible to have duplicate entries
            # in the list and remove will remove all of the duplicate key values resulting
            # in inaccurate keys
            del parent_[len(parent_) - 1]
        return results_

    def nested_dictionary_report_driver(payload_, results_, parent_, message_):
        initialize(results_, parent_)
        final_results = flatten(payload_, results_, parent_)
        line2 = "=" * 80
        print(f"{line2}")
        print(f"{message_}")
        print(f"{final_results}")
        print(f"{line2}")
        print()
        pass

    print("Exercise 37: Flatten Nested Dictionary")
    # objects needed for the recursion routines (a dictionary and a list)
    results = {}
    parent = []

    # initialize(results, parent)
    nested = {"a": 1, "b": {"c": 2, "d": {"e": 3, "f": 4}}}
    nested2 = {"a": 1, "b": {"c": 2, "d": {"e": 3, "f": 4}},
               "z": {"y": {"x": {"id": "George", "w": {
                   "v": {"u": {"t": {"s": {"r": {"q": {"a": "North", "b": "South", "c": "East", "d": "West"
                       , "p": {"o": {"v1": 10125, "v2": 45590, "v3": 60516, "v4": "frigate"}}}}}}}}}}}}}
    nested2a = {"a": 1, "b": {"c": 2, "d": {"e": 3, "f": 4}},
               "z": {"y": {"x": {"id": "George"}}}}

    # parse dictionaries and generate reports...
    nested_dictionary_report_driver(nested, results, parent, "Parse simple nested dictionary")
    nested_dictionary_report_driver(nested2, results, parent, "Parse complex nested dictionary")
    pass



##############################################################################
def exercise_38_group_by_first_character():
    """
    Exercise 38: Group by First Letter
    Problem Statement: Write a Python program to organize a list of words
        into a dictionary where each key is a starting letter and the
        corresponding value is a list of all words beginning with that letter.
    Purpose: This exercise helps you practice grouping data with dictionaries
        , using setdefault(), and building index-like structures – techniques
        commonly used in autocomplete engines, glossaries, and search indexing.
    Given Input:
        words = ["apple", "avocado", "banana", "blueberry", "cherry", "apricot"]
    Expected Output:
        {"a": ["apple", "avocado", "apricot"], "b": ["banana", "blueberry"], "c": ["cherry"]}
    """
    print("Exercise 38: Group by First Letter")
    words = ["apple", "avocado", "banana", "blueberry", "cherry", "apricot"]
    results = {}
    for item in words:
        key = item[0].lower()
        results.setdefault(key, []).append(item)
    print(results)
    pass



##############################################################################
def exercise_39_merge_and_sum_overlapping():
    """
    Exercise 39: Merge and Sum Overlapping
    Problem Statement: Write a Python program to merge two dictionaries such that
        when both share the same key, their values are added together rather than
        one overwriting the other.
    Purpose: This exercise helps you practice dictionary merging strategies
        , iterating over items, and handling key conflicts deliberately –
        skills useful in inventory systems, vote tallying, word frequency counting
        , and financial aggregation.
    Given Input:
        dict1 = {"a": 10, "b": 20, "c": 30} and
        dict2 = {"b": 5, "c": 15, "d": 25}
    Expected Output:
        {"a": 10, "b": 25, "c": 45, "d": 25}
    """
    print("Exercise 39: Merge and Sum Overlapping")
    dict1 = {"a": 10, "b": 20, "c": 30}
    dict2 = {"b": 5, "c": 15, "d": 25}
    results = {}
    results = dict1.copy()
    for k, v in dict2.items():
        results[k] = results.get(k, 0) + v
    print(results)
    pass



##############################################################################
def exercise_40_deep_shallow_copy():
    """
    Exercise 40: Deep vs. Shallow Copy
    Problem Statement: Write a Python program that demonstrates the difference
        between a shallow copy and a deep copy of a dictionary containing nested lists
        , showing how changes to nested data affect each copy differently.
    Purpose: This exercise helps you understand how Python manages object references
        , why mutating nested structures in a shallow copy also affects the original
        , and when to use copy.deepcopy() – critical knowledge for avoiding
        hard-to-trace bugs in data processing and state management.
    Given Input:
        original = {"name": "Alice", "scores": [90, 85, 92]}
    Expected Output:
        Shallow copy scores: [90, 85, 92, 100]
        Original scores after shallow mutation: [90, 85, 92, 100]
        Deep copy scores: [90, 85, 92, 99]
        Original scores after deep mutation: [90, 85, 92, 100]
    """
    def display_results(message_, orig_msg_, copy_msg_, orig_, copy_):
        print(message_)
        print(f"{orig_msg_} {orig_}")
        print(f"{copy_msg_} {copy_}")
        print()

    print("\nExercise 40: Deep vs. Shallow Copy")
    original = {"name": "Alice", "scores": [90, 85, 92]}
    shallowcopy = original.copy()
    # update the shallow copy... change should be mirrored in the original
    shallowcopy["scores"].append(100)
    display_results("SHALLOW COPY - Following update to original",
                    "Original scores:", "Original scores (shallowcopy):", original, shallowcopy)


    # test using deepcopy
    original = {"name": "Alice", "scores": [90, 85, 92]}
    deepcopy = copy.deepcopy(original)
    display_results("DEEP COPY - Prior to updates",
                    "Original scores:", "Original scores (deepcopy):", original, deepcopy)

    # add score to original... it will NOT be copied to the deepcopy
    deepcopy["scores"].append(99)
    original["scores"].append(100)
    display_results("DEEP COPY - Following update to original",
                    "Original scores:", "Original scores (deepcopy):", original, deepcopy)
    pass






