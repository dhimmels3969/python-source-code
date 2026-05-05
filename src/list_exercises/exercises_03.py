from src.common_library import helper_functions as hf


#
# Exercises found at web page https://pynative.com/python-list-exercise-with-solutions/
# Exercises 21 through 30
#


##############################################################################
def exercise_21_filter_using_list_comprehension():
    """
    Exercise 21. List Comprehension for Filtering Numbers
    Practice Problem: Given a list of integers, use list comprehension
        to create a new list that contains only the even numbers from the original list.
    Exercise Purpose: This is the “Filter” part of the Map-Filter-Reduce
        paradigm. Here we focuses on Conditional Logic within a single line.
        It is the gold standard for creating subsets of data based on specific criteria.
    Given Input:
        List: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    Expected Output:
        Even Numbers: [2, 4, 6, 8, 10]
    """
    print("Exercise 21. List Comprehension for Filtering Numbers")
    input_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    even_numbers = [x for x in input_list if x % 2 == 0]
    print(f"Even Numbers: {even_numbers}")
    pass



##############################################################################
def exercise_22_concatenate_lists():
    """
    Exercise 22. Concatenate Two Lists Index-wise
    Practice Problem: Given two lists of strings, combine them
        index-by-index to form a single list of concatenated strings.
    Exercise Purpose: Data is often stored in parallel lists
        (e.g., First Names and Last Names). This exercise teaches you
        how to merge parallel data into a usable format, a common need
        for report generation and UI display.
    Given Input:
        • List 1: ["Py", "is", "awes"]
        • List 2: ["thon", " ", "ome"]
    Expected Output:
        Merged: ['Python', 'is ', 'awesome']
    """
    print("Exercise 22. Concatenate Two Lists Index-wise")
    list_1 = ["Py", "is", "awes"]
    list_2 = ["thon", " ", "ome"]
    results = [a+b for a,b in zip(list_1, list_2)]
    print(f"Merged: {results}")
    pass



##############################################################################
def exercise_23_iterate_lists_simultaneously():
    """
    Exercise 23. Iterate Both Lists Simultaneously
    Practice Problem: Use the zip() function to loop through two lists
        at once and print their values as pairs.
    Exercise Purpose: Iterating through two lists with a single index
        variable is error-prone (you might hit an “Index Out of Range”
        if lists are different sizes). zip() is the Safe Parallel Iterator.
        It stops automatically at the end of the shortest list, preventing crashes.
    Given Input:
        • List 1: [10, 20, 30]
        • List 2: [100, 200, 300]
    Expected Output:
        10 100
        20 200
        30 300
    """
    print("Exercise 23. Iterate Both Lists Simultaneously")
    list_1 = [10, 20, 30]
    list_2 = [100, 200, 300]
    for x ,y in zip(list_1, list_2):
        print(x, y)
    pass



##############################################################################
def exercise_24_add_items_to_list():
    """
    Exercise 24. Add New Item After a Specified Item
    Practice Problem: Find a specific item in a list and
        insert a new item immediately after it.
    Exercise Purpose: Unlike append() (end) or insert() (fixed index),
        this is a Context-Aware Insertion. This is useful for things like
        adding a “New!” tag after a specific product name or inserting a
        middleware step into a list of processing functions.
    Given Input:
        • List: [10, 20, 30, 40, 50]
        • Insert after: 30
        • New Item: 35
    Expected Output:
        Updated List: [10, 20, 30, 35, 40, 50]
    """
    print("Exercise 24. Add New Item After a Specified Item")
    input_list = [10, 20, 30, 40, 50]
    target = 30
    new_item = 35
    insertion_point = input_list.index(target) + 1
    input_list.insert(insertion_point, new_item)
    print(f"Updated List: {input_list}")
    pass



##############################################################################
def exercise_25_replace_item_in_list():
    """
    Exercise 25. Replace List’s Item with New Value if Found
    Practice Problem: Find the first occurrence of a specific value in a list
        and replace it with a new value.
    Exercise Purpose: This is a Selective Update. It mimics “Find and Replace”
        functionality. It teaches you how to identify a location in memory
        and overwrite it without affecting the rest of the list structure.
    Given Input:
        • List: [5, 10, 15, 20, 25]
        • Find: 20
        • Replace with: 200
    Expected Output:
        Modified List: [5, 10, 15, 200, 25]
    """
    print("Exercise 25. Replace With New Value")
    input_list = [5, 10, 15, 20, 25]
    item_to_replace = 20
    new_value = 200
    index = input_list.index(item_to_replace)
    input_list[index] = new_value
    print(f"Modified List: {input_list}")
    pass



##############################################################################
def exercise_26_find_item_in_list():
    """
    Exercise 26. Find the Second Largest Number in a List
    Practice Problem: Write a Python function that takes a list of numbers
        and returns the second largest value. Ensure the function handles lists
        with duplicate values correctly (e.g., if the list is [10, 10, 9],
        the second largest is 9).
    Exercise Purpose: This exercise teaches you how to process data sets
        where “rank” matters. It also highlights the importance of handling duplicates.
        Simply sorting a list does not work if the largest number appears multiple
        times. It introduces the concept of using Sets to make data unique.
    Given Input:
        List: [12, 35, 1, 10, 34, 1, 35]
    Expected Output:
        Second Largest: 34
    """
    print("Exercise 26. Find Second Largest Number in a List")
    input_list = [12, 35, 1, 10, 34, 1, 35]
    # convert to set to remove duplicates
    unique_list = set(input_list)
    # convert back to list and sort in descending order
    revised_input_list = list(unique_list)
    revised_input_list.sort(reverse=True)
    # second largest value resides at index 1
    second_largest = revised_input_list[1]
    print(f"Second Largest: {second_largest}")
    pass



##############################################################################
def exercise_27_find_most_frequent_element():
    """
    Exercise 27. Find the Most Frequent Element
    Practice Problem: Create a script that identifies the “Mode” of a
        list—the element that appears most frequently. If there is a tie,
        returning one of the top elements is sufficient for this exercise.
    Exercise Purpose: Finding the mode is a fundamental task in data science
        and statistics. This exercise introduces Frequency Mapping using
        dictionaries, a vital pattern for counting occurrences in any programming language.
    Given Input:
        List: [1, 3, 3, 2, 1, 1, 4, 3, 3]
    Expected Output:
        Mode: 3
    """
    print("Exercise 27. Find Most Frequent Element")
    input_list = [1, 3, 3, 2, 1, 1, 4, 3, 3]
    results_dictionary = hf.build_dictionary(input_list)
    most_frequently_occurring_value = max(results_dictionary.values())
    # now find the key associated with the most frequently occurring value (from PyNative)
    mode = max(results_dictionary, key=results_dictionary.get)
    print(f"Mode: {mode}")
    pass



##############################################################################
def exercise_28_extract_elements_from_list():
    """
    Exercise 28. Extract Every Nth Element from a List
    Practice Problem: Write a function that accepts a list and an integer n,
        returning a new list containing every nth element from the original,
        starting from the first element (index 0).
    Exercise Purpose: This exercise explores List Slicing, one of Python’s
        most powerful features. Understanding slicing notation allows you to manipulate
        sequences with minimal code, which is essential for tasks like data sampling.
    Given Input:
        • List: ['a', 'b', 'c', 'd', 'e', 'f', 'g']
        • n: 3
    Expected Output:
        Result: ['a', 'd', 'g']
    """
    print("Exercise 28. Extract Every Nth Element from a List")
    input_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
    offset = 3
    results = input_list[::offset]
    print(f"Result: {results}")
    pass



##############################################################################
def exercise_29_is_list_palindrome():
    """
    Exercise 29. Check if List is Palindrome
    Practice Problem: Determine if a list reads the same forward and backward.
        The function should return True if it is a palindrome and False otherwise.
    Exercise Purpose: Palindrome checks are classic logic tests. This exercise
        demonstrates how to compare a sequence against its own reverse,
        reinforcing concepts of Symmetry and sequence comparison.
    Given Input:
        List: [1, 2, 3, 2, 1]
    Expected Output:
        Is Palindrome: True
    """
    print("Exercise 29. Check if List is Palindrome")
    input_list = [1, 2, 3, 2, 1]
    print(f"Is Palindrome: {input_list == input_list[::-1]}")
    pass



##############################################################################
def exercise_30_find_common_elements():
    """
    Exercise 30. Find All Common Elements Between Three Lists
    Practice Problem: Given three separate lists, write a function that
        returns a list containing only the elements that appear in all three.
    Exercise Purpose: This exercise introduces Set Intersection. When you
        need to find commonalities across multiple data sources, converting
        them to sets and finding their intersection is the most efficient
        method (O(n) average time complexity).
    Given Input:
        • List A: [1, 5, 10, 20]
        • List B: [6, 7, 20, 80, 100]
        • List C: [3, 4, 15, 20, 30, 70, 80]
    Expected Output:
        Common Elements: [20]
    """
    print("Exercise 30. Find All Common Elements Between Three Lists")
    list_a = [1, 5, 10, 20]
    list_b = [6, 7, 20, 80, 100]
    list_c = [3, 4, 15, 20, 30, 70, 80]
    common_elements = set(list_a).intersection(set(list_b)).intersection(set(list_c))
    print(f"Common Elements: {list(common_elements)}")
    pass



