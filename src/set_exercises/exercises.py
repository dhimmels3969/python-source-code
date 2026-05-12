from src.common_library import helper_functions as hf


#
# Exercises found at web page https://pynative.com/python-set-exercise-with-solutions/
# Exercises 1 through 10
#



##############################################################################
def exercise_01_basic_set_operations():
    """
    Exercise 1: Basic Set Operations
    Problem Statement: Write a Python program to create a set, add
        a new element to it, remove an element using remove(), and
        discard an element using discard().
    Purpose: This exercise introduces you to the core mutation methods
        of Python sets. Understanding the difference between remove()
        and discard() is essential because one raises an error on
        missing elements while the other does not, making each suited
        to different real-world scenarios.
    Given Input:
        fruits = {"apple", "banana", "cherry"}
    Expected Output:
        {'apple', 'banana', 'cherry', 'mango'}
        after add, {'apple', 'cherry', 'mango'}
        after remove, {'apple', 'cherry', 'mango'}
        after discard (no error even if element is absent)
    """
    print("Exercise 1: Basic Set Operations")
    pass



##############################################################################
def exercise_02_clear_all_elements():
    """
    Exercise 2: Clear All Elements
    Problem Statement: Write a Python program to remove all elements from
        a set using .clear(), while keeping the variable itself intact.
    Purpose: This exercise shows the difference between emptying a
        set and deleting the variable entirely. Using .clear() is useful
        when you want to reuse the same set object later in your
        program without reassigning it.
    Given Input:
        colors = {"red", "green", "blue"}
    Expected Output:
        set()
    """
    print("Exercise 2: Clear All Elements")
    pass



##############################################################################
def exercise_03_find_set_length():
    """
    Exercise 3: Find the Length of a Set
    Problem Statement: Write a Python program to determine how many
        elements are in a set without using the built-in len() function.
    Purpose: This exercise strengthens your understanding of iteration
        and manual counting logic. While len() is convenient, building a
        counter loop reinforces how Python traverses collections internally
        and prepares you for situations where custom counting logic
        is required.
    Given Input:
        animals = {"cat", "dog", "bird", "fish"}
    Expected Output:
        Length of set: 4
    """
    print("Exercise 3: Find the Length of a Set")
    pass



##############################################################################
def exercise_04_empty_set_check():
    """
    Exercise 4: Check if a Set is Empty
    Problem Statement: Write a Python program to check whether a set is empty
        using conditional logic, and print an appropriate message
        based on the result.
    Purpose: This exercise builds awareness of how Python evaluates
        collections as truthy or falsy values. Knowing how to check for
        emptiness reliably prevents bugs in data pipelines, loops,
        and validation routines where an empty set should trigger
        a different code path.
    Given Input:
        data = set()
    Expected Output:
        The set is empty.
    """
    print("Exercise 4: Check if a set is empty")
    pass



##############################################################################
def exercise_05_union_of_sets():
    """
    Exercise 5: Union of Sets
    Problem Statement: Write a Python program to combine two sets
        into one, containing all unique elements from both sets.
    Purpose: This exercise introduces the union operation, a fundamental
        concept in set theory and database-style data merging. It is
        commonly used when aggregating data from multiple sources
        while automatically eliminating duplicates.
    Given Input:
        set_a = {1, 2, 3, 4} and set_b = {3, 4, 5, 6}
    Expected Output:
        Union: {1, 2, 3, 4, 5, 6}
    """
    print("Exercise 5: Union of Sets")
    pass



##############################################################################
def exercise_06_set_intersection_check():
    """
    Exercise 6: Intersection of Sets
    Problem Statement: Write a Python program to find all elements
        that are common to both sets.
    Purpose: The intersection operation is widely used in filtering,
        data comparison, and finding overlaps between datasets, such
        as identifying shared customers, tags, or features
        across two groups.
    Given Input:
        set_a = {1, 2, 3, 4} and set_b = {3, 4, 5, 6}
    Expected Output:
        Intersection: {3, 4}
    """
    print("Exercise 6: Intersection of Sets")
    pass



##############################################################################
def exercise_07_sets_difference_check():
    """
    Exercise 7: Difference of Sets
    Problem Statement: Write a Python program to find all elements
        that are present in Set A but not in Set B.
    Purpose: The difference operation is useful for identifying what is
        unique to one group compared to another, such as finding items
        in one inventory but not another, or users who signed up but
        have not yet completed onboarding.
    Given Input:
        set_a = {1, 2, 3, 4} and set_b = {3, 4, 5, 6}
    Expected Output:
        Difference (A - B): {1, 2}
    """
    print("Exercise 7: Difference of Sets")
    pass



##############################################################################
def exercise_08_symmetric_difference():
    """
    Exercise 8: Symmetric Difference
    Problem Statement: Write a Python program to find all elements
        that are in either Set A or Set B, but not in both.
    Purpose: The symmetric difference is useful when you need to
        identify what is exclusive to each group, such as finding
        products carried by one store but not the other, or
        detecting changes between two versions of a dataset.
    Given Input:
        set_a = {1, 2, 3, 4} and set_b = {3, 4, 5, 6}
    Expected Output:
        Symmetric Difference: {1, 2, 5, 6}
    """
    print("Exercise 8: Symmetric Difference")
    pass



##############################################################################
def exercise_09_find_min_max():
    """
    Exercise 9: Find Max and Min
    Problem Statement: Write a Python program to identify the largest
        and smallest values in a set of numbers.
    Purpose: Finding the range boundaries of a dataset is a common
        task in data analysis and validation. This exercise also
        reinforces how Python’s built-in functions operate
        seamlessly on sets, not just lists.
    Given Input:
        numbers = {42, 7, 19, 85, 3, 56}
    Expected Output:
        Max: 85 and Min: 3
    """
    print("Exercise 9: Find Max and Min")
    pass



##############################################################################
def exercise_10_sum_elements():
    """
    Exercise 10: Sum of Set Elements
    Problem Statement: Write a Python program to calculate the
        total sum of all elements in a set manually using a loop,
        without using the built-in sum() function.
    Purpose: This exercise reinforces the accumulator pattern using
        a loop, applied to a set instead of a list. It illustrates
        that iteration works uniformly across Python collection
        types and strengthens your grasp of how aggregation
        functions work internally.
    Given Input:
        numbers = {10, 20, 30, 40, 50}
    Expected Output:
        Sum: 150
    """
    print("Exercise 10: Sum of Set Elements")
    pass


