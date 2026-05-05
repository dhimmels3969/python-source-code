from src.common_library import helper_functions as hf


#
# Exercises found at web page https://pynative.com/python-list-exercise-with-solutions/
# Exercises 11 through 20
#


##############################################################################
def exercise_11_list_slicing():
    """
    Exercise 11. List Slicing: Extract Middle Elements
    Practice Problem: Given a list, extract a “slice” containing the middle three elements.
    Exercise Purpose: Slicing is one of Python’s most powerful features. Unlike many
        languages that require manual loops to copy array sub-sections, Python uses
        [start:stop] syntax. This forms the foundation for data windowing and pagination
        in web development.
    Given Input:
        List: [10, 20, 30, 40, 50, 60, 70]
    Expected Output:
        Middle Three: [30, 40, 50]
    """
    print(f"Exercise 11. List Slicing: Extract Middle Elements")
    input_list = [10, 20, 30, 40, 50, 60, 70]
    print(f"Original: {input_list}")
    # find mid-point of list. Need to do a boundary change to determine the list contains at least 3 items
    mid_point = len(input_list) // 2

    # determine [start:stop] index range
    # start will equal mid-point -1, stop will equal mid-point +1
    start_index = mid_point - 1
    stop_index = mid_point + 2

    # extract the middle 3 values from the list
    middle_three = input_list[start_index:stop_index]
    print(f"Middle Three: {middle_three}")
    pass


##############################################################################
def exercise_12_swap_elements_in_list():
    """
    Exercise 12. Swap Two Elements at Given Indices
    Practice Problem: Write a script to swap the positions of two elements
        in a list based on their indices.
    Exercise Purpose: Swapping is the heart of every sorting algorithm
        like Bubble Sort or Quick Sort. While other languages require a
        temporary variable to hold a value during the swap, Python offers
        an elegant, one-line tuple unpacking method that is faster to write
        and less error-prone.
    Given Input:
        • List: [23, 65, 19, 90]
        • Indices to Swap: 0 and 2
    Expected Output:
        Original: [23, 65, 19, 90]
        Swapped: [19, 65, 23, 90]
    """
    print(f"Exercise 12. Swap Two Elements at Given Indices")
    input_list = [23, 65, 19, 90]
    print(f"Original: {input_list}")
    input_list[0], input_list[2] = input_list[2], input_list[0]
    print(f"Swapped: {input_list}")
    pass


##############################################################################
def exercise_13_access_nested_lists():
    """
    Exercise 13. Access Nested Lists (Simple Indexing)
    Practice Problem: Given a “list of lists,” access a specific item hidden inside the inner list.
    Exercise Purpose: This exercise teaches you to navigate Multi-dimensional Data.
        Think of nested lists like a spreadsheet (Rows and Columns) or a
        theater seating chart. To find a specific seat, you need the row and seat numbers.
    Given Input:
        • Nested List: [[1, 2], [3, 4, 5], [6, 7]]
        • Goal: Access the number 5.
    Expected Output:
        Accessed Value: 5
    """
    print(f"Exercise 13. Access Nested Lists")
    found = False
    input_list = [[1, 2], [3, 4, 5], [6, 7]]
    target = 5
    # input_list = [[1, 2], [3, 4, 5], [6, 7], 15, 888, 3040, [62, 64, 66, 68, 70, 72, 74, 73, 71], 2499, [2401, 377, 8080, 2156], 156]
    # target = 888
    item_counter = 0
    results = []
    for item in input_list:
        if isinstance(item, list):
            element_counter = 0
            for element in item:
                if element == target:
                    results.append(item_counter)
                    results.append(element_counter)
                    found = True
                    break
                element_counter += 1

        if found:
            break
        else:
            if item == target:
                results.append(item_counter)
                break
            else:
                item_counter += 1
    if results:
        print(f"Accessed Value Found (row, column): {results}  value = {target}")
    pass


##############################################################################
def exercise_14_check_for_specific_item():
    """
    Exercise 14. Check if List Contains a Specific Item
    Practice Problem: Write a check to see if a certain value exists
        within a list and print a message based on the result.
    Exercise Purpose: This is a Membership Test. It’s the logic used for
        “Is this username taken?” or “Is this item in the shopping cart?
        ” Python’s in operator makes this incredibly readable, almost like plain English.
    Given Input:
        • Inventory: ["Laptop", "Mouse", "Monitor", "Keyboard"]
        • Target: "Tablet"
    Expected Output:
        Is Tablet in inventory? False
    """
    print(f"Exercise 14. Check For Specific Item")
    input_list = ["Laptop", "Mouse", "Monitor", "Keyboard"]
    target = "Tablet"
    found = False
    if target in input_list:
        found = True
    print(f"Is {target} in inventory? {found}")
    pass


##############################################################################
def exercise_15_find_longest_string_in_list():
    """
    Exercise 15. Find the Longest String in a List
    Practice Problem: In a list of strings, identify which string
        has the most characters.
    Exercise Purpose: This combines Iteration with Comparison. It teaches you how
        to evaluate an attribute of an object (its length) rather than just its
        raw value. This is used in text processing, UI layout, and data cleaning.
    Given Input:
        Words: ["PHP", "Exercises", "Backend", "Python"]
    Expected Output:
        Longest word: Exercises
    """
    print(f"Exercise 15. Find the Longest String in a List")
    input_list = ["PHP", "Exercises", "Backend", "Python"]
    longest_word = ""
    for word in input_list:
        if len(word) > len(longest_word):
            longest_word = word
    print(f"Longest word: {longest_word}")
    pass


##############################################################################
def exercise_16_transform_each_item_in_list():
    """
    Exercise 16. Turn Every Item of a List into its Square (List Comprehension)
    Practice Problem: Given a list of numbers, create a new list where each number
        is replaced by its square (n2) using a single line of code.
    Exercise Purpose: This is your introduction to List Comprehensions. In Python
        , writing a full for loop to build a new list is often considered un-Pythonic.
        List comprehensions execute faster and are cleaner to read, providing a
        concise way to map a function across a collection.
    Given Input:
        List: [1, 2, 3, 4, 5]
    Expected Output:
        Squared List: [1, 4, 9, 16, 25]
    """
    print(f"Exercise 16. Turn Every Item of a List into its Square")
    input_list = [1, 2, 3, 4, 5]
    squared_list = [X**2 for X in input_list]
    print(f"Squared List: {squared_list}")
    pass


##############################################################################
def exercise_17_count_occurrences():
    """
    Exercise 17. Count Occurrences of an Item
    Practice Problem: Find out how many times a specific value appears in a list.
    Exercise Purpose: This is a basic form of Frequency Analysis. It’s used
        in everything from counting word occurrences in a document to
        verifying how many times a specific error code appears in a server log.
    Given Input:
        • List: [10, 20, 30, 10, 40, 10, 50]
        • Target: 10
    Expected Output:
        The number 10 appears 3 times.
    """
    print(f"Exercise 17. Count Occurrences of an Item")
    input_list = [10, 20, 30, 10, 40, 10, 50]
    target = 10
    frequency_counts = hf.build_dictionary(input_list)
    # message = f"The number {target} appears {frequency_counts[target]} times"
    # Alternate method using count() function
    number_of_occurrences = input_list.count(target)
    message = f"The number {target} appears {number_of_occurrences} times"
    print(message)
    print()

    pass


##############################################################################
def exercise_18_remove_all_occurrences():
    """
    Exercise 18. Remove All Occurrences of a Specific Item
    Practice Problem: Delete every instance of a specific value from a list.
    Exercise Purpose: This is a Filtering Operation. A common mistake is
        using .remove(), which deletes only the first occurrence. To remove
        all instances, you need to filter the list. This is essential for
        data scrubbing when you need to purge “bad data” or “flagged entries” entirely.
    Given Input:
        • List: [5, 20, 15, 20, 25, 50, 20]
        • Item to remove: 20
    Expected Output:
        Cleaned List: [5, 15, 25, 50]

    # From PyNative website...
    # Filter the list using a comprehension
    cleaned_list = [x for x in list_v if x != target]
    """
    print(f"Exercise 18. Remove All Occurrences of a Specific Item")
    input_list = [5, 20, 15, 20, 25, 50, 20]
    target = 20
    target_list = []
    print(f"Original List: {input_list}")
    # identify the index(es) where the target is found... store in a list
    for i in range(len(input_list)):
        if input_list[i] == target:
            target_list.append(i)

    # sort the list in descending order
    target_list = target_list[::-1]

    # iterate through the list in descending order and pop each item
    for index in target_list:
        input_list.pop(index)

    print(f"Cleaned List: {input_list}")
    pass


##############################################################################
def exercise_19_remove_empty_strings():
    """
    Exercise 19. Remove Empty Strings from a List of Strings
    Practice Problem: Take a list of strings that contains empty entries ("")
        and remove them to keep only the valid text.
    Exercise Purpose: Real-world data is often “noisy.” When you split a
        paragraph into words or import a CSV, you often end up with empty
        strings. Learning to “sanitize” your lists is a daily task for
        developers and data scientists.
    Given Input:
        List: ["Mike", "", "Emma", "Kelly", "", "Brad"]
    Expected Output:
        Cleaned Names: ['Mike', 'Emma', 'Kelly', 'Brad']

     From PyNative website...
     # Method: Using filter with None
    # filter(None, ...) removes all "Falsy" values (empty strings, 0, None)
    cleaned_names = list(filter(None, names))
    """
    print(f"Exercise 19. Remove Empty Strings from a List of Strings")
    input_list = ["Mike", "", "Emma", "Kelly", "", "Brad"]
    print(f"Original List: {input_list}")
    clean_list = [x for x in input_list if len(x.strip()) > 0]
    print(f"Cleaned Names: {clean_list}")
    pass


##############################################################################
def exercise_20_remove_duplicates_from_list():
    """
    Exercise 20. Remove Duplicates from List
    Practice Problem: Remove all duplicate values from a list while keeping
        only one instance of each element.
    Exercise Purpose: This exercise introduces Set Theory. In programming
        , you often need to ensure uniqueness (e.g., a list of unique email subscribers).
        While there are many ways to do this, using Python’s set or
        dict structures is the fastest way to handle the logic.
    Given Input:
        List: [10, 20, 10, 30, 40, 40, 20, 50]
    Expected Output:
        Unique List: [10, 20, 30, 40, 50]

    # From PyNative website...
    # Method to remove duplicates while preserving order
    unique_list = list(dict.fromkeys(duplicates))
    """
    print(f"Exercise 20. Remove Duplicates from a List")
    input_list = [10, 20, 10, 30, 40, 40, 20, 50]
    unique_list = []
    print(f"Original List: {input_list}")
    for i in range(len(input_list)):
        if input_list[i] not in unique_list:
            unique_list.append(input_list[i])
    print(f"Unique List: {unique_list}")
    pass