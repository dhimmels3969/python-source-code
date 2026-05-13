from src.common_library import helper_functions as hf


#
# Exercises found at web page https://pynative.com/python-set-exercise-with-solutions/
# Exercises 11 through 20
#



##############################################################################
def exercise_11_add_elements():
    """
    Exercise 11: Add a List of Elements
    Problem Statement: Write a Python program to add multiple elements from
        a list into an existing set using the .update() method.
    Purpose: This exercise demonstrates how to efficiently bulk-add items
        to a set from another iterable. The .update() method is preferable
        to calling .add() in a loop when you have a collection of items ready
        to merge, and it automatically handles duplicates.
    Given Input:
        fruits = {"apple", "banana"} and new_fruits = ["cherry", "mango", "apple"]
    Expected Output:
        Updated set: {'apple', 'banana', 'cherry', 'mango'}
    """
    print("Exercise 11: Add Elements")
    fruits = {"apple", "banana"}
    new_fruits = ["cherry", "mango", "apple"]
    fruits.update(new_fruits)
    print(f"Updated set: {sorted(fruits)}")
    pass



##############################################################################
def exercise_12_update_with_multiple_iterables():
    """
    Exercise 12: Update with Multiple Iterables
    Problem Statement: Write a Python program to add elements from a list,
        a tuple, and another set into an existing set in a single
        .update() call.
    Purpose: This exercise highlights the flexibility of .update()
        in accepting multiple iterables at once. It is a practical pattern
        when consolidating data from several heterogeneous sources into
        one unified set in a single step.
    Given Input:
        base = {1, 2}, from_list = [3, 4], from_tuple = (5, 6), from_set = {7, 8}
    Expected Output:
        Updated set: {1, 2, 3, 4, 5, 6, 7, 8}
    """
    print("Exercise 12: Update with Multiple Iterables")
    base = {1, 2}
    from_list = [3, 4]
    from_tuple = (5, 6)
    from_set = {7, 8}
    base.update(from_list, from_tuple, from_set)
    print(f"Updated set: {base}")
    pass



##############################################################################
def exercise_13_subset_superset_check():
    """
    Exercise 13: Check Subset and Superset
    Problem Statement: Write a Python program to check whether one set is a
        subset of another and whether one set is a superset of another using
        .issubset() and .issuperset().
    Purpose: Subset and superset checks are essential in access control
        systems, tag-based filtering, and data validation scenarios where
        you need to confirm that one group of items is entirely contained
        within another.
    Given Input:
        set_a = {1, 2, 3} and set_b = {1, 2, 3, 4, 5}
    Expected Output:
        Is set_a a subset of set_b? True and Is set_b a superset of set_a? True
    """
    def subset(src, tgt):
        return src.issubset(tgt)

    def superset(src, tgt):
        return src.issuperset(tgt)

    print("Exercise 13: Check Subset and Superset")
    set_a = {1, 2, 3}
    set_b = {1, 2, 3, 4, 5}
    set_a_subset_of_set_b = subset(set_a, set_b)
    set_a_superset_of_set_b = superset(set_a, set_b)

    set_b_subset_of_set_a = subset(set_b, set_a)
    set_b_superset_of_set_a = superset(set_b, set_a)
    print(f"Set A subset of Set B: {set_a_subset_of_set_b}")
    print(f"Set A superset of Set B: {set_a_superset_of_set_b}")
    print()
    print(f"Set B subset of Set A: {set_b_subset_of_set_a}")
    print(f"Set B superset of Set A: {set_b_superset_of_set_a}")
    pass



##############################################################################
def exercise_14_disjoint_check():
    """
    Exercise 14: Intersection Check with isdisjoint()
    Problem Statement: Write a Python program to check whether two sets
        share any common elements using the .isdisjoint() method.
    Purpose: Knowing whether two sets are completely separate is valuable in
        scheduling, access control, and data deduplication tasks, where
        overlap between groups signals a conflict or an error that needs
        to be handled.
    Given Input:
        set_a = {1, 2, 3} and set_b = {4, 5, 6}
    Expected Output:
        Are the sets disjoint? True
    """
    print("Exercise 14: Intersection Check with isdisjoint()")
    set_a = {1, 2, 3}
    set_b = {4, 5, 6}
    results = set_a.isdisjoint(set_b)
    print(f"Are the sets disjoint? {results}")
    pass



##############################################################################
def exercise_15_difference_update():
    """
    Exercise 15: Set Difference Update
    Problem Statement: Write a Python program to modify a set by removing
        all elements that are also found in another set using the
        difference_update() method.
    Purpose: This exercise helps you practice in-place set modification.
        Understanding difference_update() is useful when you need to
        strip out unwanted or overlapping entries from a collection
        without creating a new object.
    Given Input:
        a = {1, 2, 3, 4, 5} and b = {3, 4, 5, 6, 7}
    Expected Output:
        a = {1, 2}
    """
    print("Exercise 15: Set Difference Update")
    a = {1, 2, 3, 4, 5}
    b = {3, 4, 5, 6, 7}
    a.difference_update(b)
    results = a
    print(f"a = {results}")
    pass



##############################################################################
def exercise_16_intersection_update():
    """
    Exercise 16: Set Intersection Update
    Problem Statement: Write a Python program to modify a set so that
        it keeps only the elements that are also found in another set
        using the intersection_update() method.
    Purpose: This exercise reinforces in-place filtering of a set to its
        shared elements. It is commonly used when reconciling two collections
        and retaining only the data that appears in both, such as matching
        user IDs or common tags.
    Given Input:
        a = {1, 2, 3, 4, 5} and b = {3, 4, 5, 6, 7}
    Expected Output:
        a = {3, 4, 5}
    """
    print("Exercise 16: Set Intersection Update")
    a = {1, 2, 3, 4, 5}
    b = {3, 4, 5, 6, 7}
    a.intersection_update(b)
    print(f"a = {a}")
    pass



##############################################################################
def exercise_17_symmetric_difference_update():
    """
    Exercise 17: Set Symmetric Difference Update
    Problem Statement: Write a Python program to modify a set so that
        it keeps only elements that are in either set but not in both,
        using the symmetric_difference_update() method.
    Purpose: This exercise teaches you to isolate non-overlapping
        elements between two sets in place. It is useful in scenarios
        like finding items that exist in one dataset but not the
        other, such as detecting mismatches between two records.
    Given Input:
        a = {1, 2, 3, 4, 5} and b = {3, 4, 5, 6, 7}
    Expected Output:
        a = {1, 2, 6, 7}
    """
    print("Exercise 17: Set Symmetric Difference Update")
    a = {1, 2, 3, 4, 5}
    b = {3, 4, 5, 6, 7}
    a.symmetric_difference_update(b)
    print(f"a = {a}")
    pass



##############################################################################
def exercise_18_remove_items():
    """
    Exercise 18: Remove Items Simultaneously
    Problem Statement: Write a Python program to remove a batch of
        specific items from a set all at once using the
        difference_update() method.
    Purpose: This exercise demonstrates a practical use of
        difference_update() as a bulk-removal tool. Rather than looping
        and calling remove() repeatedly, you can pass a collection of
        items to discard in a single operation.
    Given Input:
        items = {10, 20, 30, 40, 50, 60} and to_remove = {20, 40, 60}
    Expected Output:
        items = {10, 30, 50}
    """
    print("Exercise 18: Remove Items Simultaneously")
    items = {10, 20, 30, 40, 50, 60}
    to_remove = {20, 40, 60}
    items.difference_update(to_remove)
    print(f"items = {items}")
    pass



##############################################################################
def exercise_19_pop_elements():
    """
    Exercise 19: The Pop Operation
    Problem Statement: Write a Python program to remove and return
        an arbitrary element from a set using pop(), and handle the KeyError
        that occurs when the set is empty.
    Purpose: This exercise familiarises you with the pop() method and
        its unpredictable nature on sets. It also practices defensive
        programming using try/except blocks to handle runtime errors
        gracefully.
    Given Input:
        s = {100, 200, 300} and then an empty set s = set()
    Expected Output:
        Popped: 100   (or any arbitrary element)
        Error: pop from an empty set
    """
    print("Exercise 19: Pop Operation")
    s = {100, 200, 300}
    try:
        for _ in range(len(s) + 1):
            print(f"Popped: {s.pop()}")
    except KeyError as e:
        print(f"Error: {e}")
        print(f"Set: {s}")
    pass



##############################################################################
def exercise_20_filter_set():
    """
    Exercise 20: Filter a Set
    Problem Statement: Write a Python program to create a new set
        containing only the elements from an existing set that satisfy
        a condition – specifically, elements divisible by 3.
    Purpose: This exercise introduces set comprehensions as a clean and
        readable way to filter data. The pattern mirrors list
        comprehensions but produces a set, which automatically
        eliminates any duplicate results.
    Given Input:
        numbers = {1, 2, 3, 6, 7, 9, 12, 14, 15}
    Expected Output:
        divisible_by_3 = {3, 6, 9, 12, 15}
    """
    print("Exercise 20: Filter Set")
    numbers = {1, 2, 3, 6, 7, 9, 12, 14, 15}
    divisible_by_3 = {x for x in numbers if x % 3 == 0}
    print(f"divisible_by_3 = {divisible_by_3}")
    pass


