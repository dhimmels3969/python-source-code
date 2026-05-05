from src.common_library import helper_functions as hf
from itertools import pairwise

#
# Exercises found at web page https://pynative.com/python-list-exercise-with-solutions/
# Exercises 31 through 40
#




##############################################################################
def exercise_31_filter_by_value_length():
    """
    Exercise 31. Filter Strings by Length in a List
    Practice Problem: Write a function that takes a list of strings
        and an integer k. The function should return a new list
        containing only the strings that have a length greater than
        or equal to k.
    Exercise Purpose: This exercise introduces List Comprehensions,
        which are the “Pythonic” way to filter data. It demonstrates
        how to combine iteration and conditional logic into a single
        , readable line of code.
    Given Input:
        • List: ["apple", "pie", "banana", "kiwi", "pear"]
        • k: 5
    Expected Output:
        Filtered List: ['apple', 'banana']
    """
    print("Exercise 31. Filter Strings by Length in a List")
    input_list = ["apple", "banana", "kiwi", "pear"]
    min_length = 5
    filtered_list = [x for x in input_list if len(x) >= min_length]
    print(f"Filtered List: {filtered_list}")
    pass



##############################################################################
def exercise_32_sorted_list_check():
    """
    Exercise 32. Check if List is Sorted
    Practice Problem: Create a function that determines if a list of
        numbers is sorted in non-decreasing (ascending) order.
        Return True if it is, and False otherwise.
    Exercise Purpose: Checking order is a common prerequisite
        for algorithms like Binary Search. This exercise teaches
        you to perform Neighbor Comparison by examining an element
        and its immediate successor together.
    Given Input:
        List: [10, 20, 30, 25, 40]
    Expected Output:
        Is Sorted: False

    # from PyNative website
    def is_list_sorted(lst):
        # Check if every element is <= the next element
        return all(lst[i] <= lst[i + 1] for i in range(len(lst) - 1))
    """

    def sorted(item_pair):
        return item_pair[1] >= item_pair[0]

    def is_list_sorted(list_in):
        comparisons = list(pairwise(list_in))
        conditions = (sorted(item) for item in comparisons)
        return all(conditions)

    print("Exercise 32. Check if List is Sorted")
    input_list = [10, 20, 30, 25, 40]
    results = is_list_sorted(input_list)
    print(f"List: {input_list} Sorted: {results}")

    input_list = [10, 20, 30, 80, 122, 240]
    results = is_list_sorted(input_list)
    print(f"List: {input_list} Sorted: {results}")


    # comparisons = list(pairwise(input_list))
    # conditions = (sorted (item) for item in comparisons)
    # results = all(conditions)


    # sorted = True
    # for i in range(len(input_list)-1):
    #     if input_list[i] > input_list[i+1]:
    #         sorted = False
    #         break

    pass



##############################################################################
def exercise_33_list_to_dictionary_conversion():
    """
    Exercise 33. List to Dictionary Conversion
    Practice Problem: Given two lists of the same length, one containing
        keys and the other containing values. combine them into a single
        dictionary.
    Exercise Purpose: In data processing, you often receive related data
        in separate arrays. This exercise teaches you how to use the zip()
        function to pair elements and transform them into a dictionary.
    Given Input:
        • Keys: ["name", "age", "city"]
        • Values: ["Alice", 25, "New York"]
    Expected Output:
    Dictionary:
        {'name': 'Alice', 'age': 25, 'city': 'New York'}

    # from PyNative website
    def lists_to_dict(keys, values):
        # Zip pairs the elements, dict() converts pairs to key-value entries
        return dict(zip(keys, values))
    """
    print("Exercise 33. List to Dictionary Conversion")
    keys = ["name", "age", "city"]
    values = ["Alice", 25, "New York"]
    results_dictionary = {}
    if len(keys) != len(values):
        raise TypeError("Keys and Values must have the same length")
    else:
        for i in range(len(keys)):
            results_dictionary[keys[i]] = values[i]
    print(f"Dictionary: {results_dictionary}")
    pass



##############################################################################
def exercise_34_list_differences():
    """
    Exercise 34. Find the Difference Between Two Lists
    Practice Problem: Write a function that finds the “difference”
        between two lists—specifically, all elements that are present
        in the first list but not in the second list.
    Exercise Purpose: This exercise explores Set Logic and exclusion.
        It is a common task when synchronizing databases or filtering
        out “already processed” items from a new batch of data.
    Given Input:
        • List A: [1, 2, 3, 4, 5]
        • List B: [2, 4, 6]
    Expected Output:
        Difference (A – B): [1, 3, 5]
    """
    print("Exercise 34. Find the Difference Between Two Lists")
    list_a = [1, 2, 3, 4, 5]
    list_b = [2, 4, 6]
    results = list(set(list_a) - set(list_b))
    print(f"Difference (A – B): {results}")
    pass



##############################################################################
def exercise_35_remove_values_in_place():
    """
    Exercise 35. Remove Negative Numbers In-place
    Practice Problem: Write a function that removes all negative
        numbers from a list without creating a new list. You must
        modify the original list object directly.
    Exercise Purpose: This is a classic “trap” exercise. If you remove
        items while iterating forward, the indices shift and you will
        skip elements. This exercise teaches In-place Modification and
        the importance of iterating backwards or using slice assignment.
    Given Input:
        List: [10, -5, 20, -1, 0, -8]
    Expected Output:
        Modified List: [10, 20, 0]
    """
    print("Exercise 35. Remove Negative Numbers In-place")
    input_list = [10, -5, 20, -1, 0, -8]
    for i in range(len(input_list)-1, 0, -1):
        if input_list[i] < 0:
            input_list.pop(i)
    print(f"Modified List: {input_list}")
    pass



##############################################################################
def exercise_36_extend_nested_list():
    """
    Exercise 36. Extend Nested List by Adding a Sublist
    Practice Problem: Write a function that iterates through a
        list of nested lists and appends a specific sublist
        (or value) to each inner list.
    Exercise Purpose: Working with “lists of lists” is common
        in matrix manipulation and data grouping. This exercise
        reinforces the concept of Nested Iteration, accessing
        an object that exists inside another object and modifying
        it in place.
    Given Input:
        • Nested List: [['apple', 'banana'], ['cherry', 'date']]
        • To Append: "elderberry"
    Expected Output:
        Modified List: [['apple', 'banana', 'elderberry'], ['cherry', 'date', 'elderberry']]
    """
    print("Exercise 36. Extend Nested List by Adding a Sublist")
    input_list = [['apple', 'banana'], ['cherry', 'date']]
    item_to_add = "elderberry"
    for inner_list in input_list:
        inner_list.append(item_to_add)
    print(f"Modified List: {input_list}")
    pass



##############################################################################
def exercise_37_concatenate_lists():
    """
    Exercise 37. Concatenate Two Lists in a Specific Order
    Practice Problem: Given two lists of strings, create a new list
        that contains every possible combination of elements from
        the first and second list, concatenated together.
    Exercise Purpose: This exercise simulates a Cartesian Product. It is
        useful for generating permutations like combining first names
        with last names or product categories with sizes. It shows how
        Nested List Comprehensions can replace bulky nested loops.
    Given Input:
        • List 1: ["Hello ", "Take "]
        • List 2: ["Dear", "Sir"]
    Expected Output:
        Result: ['Hello Dear', 'Hello Sir', 'Take Dear', 'Take Sir']
    """
    print("Exercise 37. Concatenate Lists")
    list_1 = ["Hello ", "Take "]
    list_2 = ["Dear", "Sir"]
    results = [x + y for x in list_1 for y in list_2]
    print(f"Result: {results}")
    pass



##############################################################################
def exercise_38_flatten_nested_list():
    """
    Exercise 38. Flatten Nested List (2D to 1D)
    Practice Problem: Take a 2D list (a list containing several lists)
        and “flatten” it into a single 1D list containing all the
        individual elements in their original order.
    Exercise Purpose: Flattening is a core data-wrangling task. When you
        have data chunked into groups (like rows in a table) but need to
        perform a single operation on every individual piece, you must
        flatten the structure first.
    Given Input:
        2D List: [[1, 2, 3], [4, 5], [6, 7, 8, 9]]
    Expected Output:
        1D List: [1, 2, 3, 4, 5, 6, 7, 8, 9]
    """
    print("Exercise 38. Flatten Nested List (2D to 1D)")
    input_list = [[1, 2, 3], [4, 5, 6, 7, 8, 9]]
    flattened_list = [item for sublist in input_list for item in sublist]
    print(f"1D List: {flattened_list}")
    pass



##############################################################################
def exercise_39_flatten_deeply_nested_lists():
    """
    Exercise 39. Flatten a Deeply Nested List (Recursion)
    Practice Problem: Write a function that flattens a list of arbitrary depth.
        The list may contain integers or other lists, which in turn may contain
        even more lists (e.g., [1, [2, [3, 4]]]).
    Exercise Purpose: This is a significant step up in logic. It introduces
        Recursion, the act of a function calling itself. This is the only
        clean way to handle “infinite” depth without knowing the structure
        ahead of time.
    Given Input:
        Deep List: [1, [2, [3, 4], 5], 6, [7, 8]]
    Expected Output:
        Flattened: [1, 2, 3, 4, 5, 6, 7, 8]
    """
    def flatten(in_, out_):
        for item in in_:
            if isinstance(item, list):
                flatten(item, out_)
            else:
                out_.append(item)
        return out_

    print("Exercise 39. Flatten Deeply Nested List (Recursion)")
    # input_list = [1, [2, 3, 4]]
    # input_list = [1, [2, [3, 4], 5], 6, [7, 8], 14, [175, 225, 275], 19, 34, [1000, [22, 27, [16, 256, 4094, \
    #     [70, 71, 72, [90, 91, 92, [87, 86, 85, [6561, 729, [14, 13, 12, [11, 121, 1331, 14641] ] ] ] ] ] ] ] ] ]
    input_list = [1, [2, [3, 4], 5], 6, [7, 8]]

    results = []
    final_results = flatten(input_list, results)
    print(f"Flattened: {final_results}")
    pass



##############################################################################
def exercise_40_calculate_cumulative_sum():
    """
    Exercise 40. Calculate Cumulative Sum (Prefix Sums)
    Practice Problem: Create a function that transforms a list
        of numbers into their cumulative sum. Each element at
        index i in the new list should be the sum of all elements
        from index 0 to i in the original list.
    Exercise Purpose: Cumulative sums (or prefix sums) are used
        in financial tracking (running balance), signal processing,
        and algorithms that require quick range-sum queries. It teaches
        you how to maintain a Running Total.
    Given Input:
        List: [10, 20, 30, 40]
    Expected Output:
        Cumulative Sum: [10, 30, 60, 100]
    """
    print("Exercise 40. Calculate Cumulative Sum (Prefix Sums)")
    input_list = [10, 20, 30, 40]
    totals_list = []
    cumulative_total = 0
    for i in range(len(input_list)):
        cumulative_total += input_list[i]
        totals_list.append(cumulative_total)
    print(f"Original List: {input_list}")
    print(f"Cumulative Sum: {totals_list}")
    pass



