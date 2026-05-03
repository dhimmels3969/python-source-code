from src.common_library import helper_functions as hf


#
# Exercises found at web page https://pynative.com/python-list-exercise-with-solutions/
# Exercises 1 through 10
#

##############################################################################
def exercise_01_basic_list_operations():
    """
    Exercise 1. Perform Basic List Operations
    Practice Problem: Write a script to perform the following three operations on given list
        1. Access the third element of a list
        2. List Length: Print the total number of items
        3. Check if the list is empty
    Exercise Purpose: Before mastering complex algorithms, you must master data access:
        indexing, sizing, and validation. Quickly checking if a list has data prevents
        “Index Out of Range” errors that crash programs.
    Given
        Input: numbers = [10, 20, 30, 40, 50]
    Expected Output:
        Third element: 30
        Length of list: 5
        Is the list empty? False
    """
    def empty_list(list_in):
        return len(list_in) == 0

    print(f"Exercise 1. Perform Basic List Operations")
    numbers = [10, 20, 30, 40, 50]
    blank_list = []
    print(f"Third element: {numbers[2]}")
    print(f"Length of list: {len(numbers)}")
    print(f"Is the list empty? {empty_list(numbers)}")

    print(f"List Name: blank_list Is it empty? {empty_list(blank_list)}")
    pass


##############################################################################
def exercise_02_perform_list_manipulation():
    """
    Exercise 2. Perform List Manipulation
    Practice Problem: Take a given list and modify it through five specific actions:
        1. Change Element: Change the second element of a list to 200 and print the updated list.
        2. Append Element: Add 600 o the end of a list and print the new list.
        3. Insert Element: Insert 300 at the third position (index 2) of a list and print the result.
        4. Remove Element (by value): Remove 600 from the list and print the list.
        5. Remove Element (by index): Remove the element at index 0 from the list print the list.
    Exercise Purpose: Python lists are mutable, meaning they can be changed after they are created.
        This exercise demonstrates the various ways to “reshape” your data
        dynamically during execution.
    Given Input:
        Initial List: [100, 50, 400, 500]
    Expected Output:
        Updated (Change): [100, 200, 400, 500]
        Updated (Append): [100, 200, 400, 500, 600]
        Updated (Insert): [100, 200, 300, 400, 500, 600]
        Updated (Remove 600): [100, 200, 300, 400, 500]
        Updated (Remove Index 0): [200, 300, 400, 500]
    """
    print(f"Exercise 2. Perform List Manipulation")
    input_list = [100, 50, 400, 500]
    print(f"Initial List: {input_list}")
    input_list[1] = 200
    print(f"Updated (Change)): {input_list}")
    input_list.append(600)
    print(f"Updated (Append)): {input_list}")
    input_list.insert(2, 300)
    print(f"Updated (Insert): {input_list}")
    input_list.remove(600)
    print(f"Updated (Remove 600): {input_list}")
    input_list.pop(0)
    print(f"Updated (Remove Index 0): {input_list}")
    pass


##############################################################################
def exercise_03_calculate_stats():
    """
    Exercise 3. Sum and Average of All Numbers in a List
    Practice Problem: Calculate the total sum of all integers in a list and
        find the arithmetic mean (average).
    Exercise Purpose: Aggregation is the heart of data science. This exercise
        teaches you how to reduce a collection of multiple data points into a
        single, meaningful summary statistic.
    Given Input:
        Numbers: [10, 20, 30, 40, 50]
    Expected Output:
        Sum: 150
        Average: 30.0
    """
    print(f"Exercise 3. Sum and Average of All Numbers in a List")
    numbers = [10, 20, 30, 40, 50]
    numbers_sum = sum(numbers)
    numbers_avg = sum(numbers) / len(numbers)
    print(f"Sum: {numbers_sum}")
    print(f"Average: {numbers_avg}")
    pass


##############################################################################
def exercise_04_find_min_and_max():
    """
    Exercise 4. Find Maximum and Minimum from List
    Practice Problem: Identify the largest and smallest numerical values within a provided list.
    Exercise Purpose: Finding extremes is vital for tasks like identifying the “best”
        price, the “highest” score, or detecting “outlier” data points in a dataset.
    Given Input:
        Data: [45, 12, 89, 2, 67]
    Expected Output:
        Maximum: 89
        Minimum: 2
    """
    print(f"Exercise 4. Find Maximum and Minimum from List")
    input_list = [45, 12, 89, 2, 67]
    max1 = max(input_list)
    min2 = min(input_list)
    print(f"Maximum: {max1}")
    print(f"Minimum: {min2}")
    max_value = input_list[0]
    min_value = input_list[0]
    for i in range(1, len(input_list)):
        if input_list[i] > max_value:
            max_value = input_list[i]
        if input_list[i] < min_value:
            min_value = input_list[i]
    print(f"Maximum: {max_value}, Minimum: {min_value}")
    pass


##############################################################################
def exercise_05_calculate_product():
    """Exercise 5. Calculate the Product of All Elements
    Practice Problem: Multiply every number in a list together
        to find the total product.
    Exercise Purpose: While sum is built-in, “product” often requires you to
        think about how to accumulate values. This exercise reinforces the
        concept of an “accumulator variable” in a loop.
    Given Input:
        Factors: [2, 3, 5, 7]
    Expected Output:
        Product: 210
    """
    print(f"Exercise 5. Calculate the Product of All Elements")
    input_list = [2, 3, 5, 7]
    results = 1
    for i in range(0, len(input_list)):
        results *= input_list[i]
    print(f"Product: {results}")
    pass


##############################################################################
def exercise_06_count_evens_and_odds():
    """
    Exercise 6. Count Even and Odd Numbers
    Practice Problem: Given a list of integers, iterate through the items
        and count how many are even and how many are odd.
    Exercise Purpose: This introduces Flow Control and the Modulo Operator.
        It is a classic “Filtering” pattern where you categorize data based on
        a mathematical property. In real-world apps, this is the foundation
        for things like alternating row colors in a table or batching jobs
        into two different queues.
    Given Input:
        Numbers: [10, 21, 4, 45, 66, 93, 11]
    Expected Output:
        Even numbers: 3
        Odd numbers: 4
    """
    print(f"Exercise 6. Count Even and Odd Numbers")
    input_list = [10, 21, 4, 45, 66, 93, 11]
    odds_count = 0
    even_count = 0
    for i in range(0, len(input_list)):
        if input_list[i] % 2 == 0:
            even_count += 1
        else:
            odds_count += 1
    print(f"Even numbers: {even_count}")
    print(f"Odd numbers: {odds_count}")
    pass


##############################################################################
def exercise_07_reverse_a_list():
    """
    Exercise 7. Reverse a List
    Practice Problem: Take a list and reverse the order of its elements.
    Exercise Purpose: Reversal is a fundamental operation in data structures
        (like reversing a string or a linked list). Python provides multiple ways
        to do this, and understanding the difference between In-place Reversal
        (changing the original) and Slicing (creating a new one) is crucial
        for memory management.
    Given Input:
        List: [100, 200, 300, 400, 500]
    Expected Output:
        Reversed List: [500, 400, 300, 200, 100]
    """
    print(f"Exercise 7. Reverse a List")
    input_list = [100, 200, 300, 400, 500]
    reversed_list = input_list[::-1]
    print(f"Reversed List: {reversed_list}")
    pass


##############################################################################
def exercise_08_sort_list_of_numbers():
    """
    Exercise 8. Sort a List of Numbers
    Practice Problem: Sort a list of numbers in ascending order (lowest to highest).
    Exercise Purpose: Sorting is perhaps the most studied topic in Computer Science.
        It turns chaotic data into organized data, which is a prerequisite for
        high-speed search algorithms like Binary Search. Python uses Timsort,
        an efficient, hybrid sorting algorithm.
    Given Input:
        Unsorted: [56, 12, 89, 3, 22]
    Expected Output:
        Sorted List: [3, 12, 22, 56, 89]
    """
    print(f"Exercise 8. Sort a List")
    input_list = [56, 12, 89, 3, 22]
    sorted_list = sorted(input_list)
    print(f"Sorted List: {sorted_list}")
    pass


##############################################################################
def exercise_09_create_copy_of_list():
    """
    Exercise 9. Create a Copy of a List
    Practice Problem: Create a copy of an existing list so that modifying the copy
        does not change the original.
    Exercise Purpose: This exercise addresses one of the most common “gotchas”
        for new Python programmers: Pass-by-Object-Reference. If you simply write
        list_b = list_a, both variables point to the same list in memory. Learning
        to “Clone” or “Copy” is vital for data integrity.
    Given Input:
        Original: ["Apple", "Banana", "Cherry"]
    Expected Output:
        Original: ['Apple', 'Banana', 'Cherry']
        Copy: ['Apple', 'Banana', 'Cherry']
        (Verification: Modifying copy doesn't hurt original!)
    """
    print(f"Exercise 9. Create a Copy of a List")
    input_list = ["Apple", "Banana", "Cherry"]
    copy_of_input_list = input_list.copy()
    print(f"Original: {input_list}")
    print(f"Copy: {copy_of_input_list}")
    # modify the copy and show the results
    print("------------------------------------- After updating copy_of_input_list")
    copy_of_input_list[1] = "Tangelo"
    print(f"Original: {input_list}")
    print(f"Copy (After update): {copy_of_input_list}")
    pass


##############################################################################
def exercise_10_combine_two_lists():
    """
    Exercise 10. Combine Two Lists
    Practice Problem: Merge two separate lists into a single, unified list.
    Exercise Purpose: Data often arrives in fragments from different sources
        (e.g., two different database queries). Combining or “Concatenating”
        them is the first step in data aggregation.
    Given Input:
        • List A: ["Physics", "Chemistry"]
        • List B: ["Maths", "Biology"]
    Expected Output:
        Combined List: ['Physics', 'Chemistry', 'Maths', 'Biology']
    """
    print(f"Exercise 10. Combine Two Lists")
    list_a = ["Physics", "Chemistry"]
    list_b = ["Maths", "Biology"]
    # append list_b to the end of list_a using the "extend" method.
    list_a.extend(list_b)
    print(f"Combined List: {list_a}")
    pass


