


#
# Exercises found at web page https://pynative.com/python-if-else-and-for-loop-exercise-with-solutions/
# Exercises 21 through 30
#

def exercise_21_reverse_number_pattern():
    """
    Practice Problem: Write a program to use for loop to print the following reverse number pattern:
    Exercise Purpose: This exercise builds on nested loops and introduces Dynamic Range Boundaries.
        It shows how to make the inner loop’s starting point depend on the outer loop’s
        current value to create decreasing structures.
    Given Input:
        n = 5
    Expected Output:
        5 4 3 2 1
        4 3 2 1
        ...
        1
    """
    print("Exercise 21: Print a reverse number")
    starting_point = 5
    for i in range(starting_point,0, -1):
        for j in range(starting_point,0, -1):
            print(j, end="\t")
        print()
        starting_point -= 1
    pass
###########################################################


def exercise_22_alternate_numbers_pattern():
    """
    Exercise 22. Print the alternate numbers pattern
    Practice Problem: Write a program to print a pattern of alternate numbers from 1 to 20 (e.g., 1, 3, 5…).
    Exercise Purpose: This exercise emphasizes Step Logic in ranges. Being able to skip values
        efficiently without using unnecessary if statements inside your loop makes your code
        more “Pythonic” and faster to execute.
    Given Input: Range:
        1 to 20
    Expected Output:
        1 3 5 7 9 11 13 15 17 19
    """
    print("Exercise 22: Print a range")
    for i in range(1, 20, 2):
        print(i, end="\t")
    print()
    pass

###########################################################


def exercise_23_alphabet_pyramid_pattern(number_of_rows= 5):
    """
    Exercise 23. Print Alphabet pyramid (A, BB, CCC) pattern
    Practice Problem: Write a program to print a triangle pattern where
        each row consists of the same letter, and the letter changes (increments) with each new row.
    Exercise Purpose: This exercise introduces ASCII Value Manipulation.
        You’ll learn to use the chr() function to convert numbers into characters,
        so you can generate the alphabet dynamically without hardcoding each letter.
    Given Input: rows = 5
    Expected Output:
        A
        B B
        C C C
        D D D D
        E E E E E
    """
    print("Exercise 23: Print an alphabet pyramid")
    start_val = 64
    for i in range(1, number_of_rows + 1):
        ascii_value = start_val + i
        myChar = chr(ascii_value)
        for j in range(i):
            print(myChar, end=" ")
        print()
    pass
###########################################################


def exercise_24_hollow_square_pattern():
    """
    Exercise 24. Hollow square pattern
    Practice Problem: Print a 5*5 square of stars where the middle is empty, leaving only the border.
    Exercise Purpose: This exercise teaches Boundary Condition Logic. Instead of printing every
        item in a nested loop, you use if statements to identify edges, such as the first or
        last rows and columns, which is essential for UI layouts and 2D array processing.
    Given Input:
        size = 5
    Expected Output:
        * * * * *
        *       *
        *       *
        *       *
        * * * * *
    """
    print("Exercise 24: Print a 5*5 square of stars")
    pass
    pass
###########################################################


def exercise_25_pyramid_star_pattern():
    """
    Exercise 25. Print pyramid pattern of stars
    Practice Problem: Write a program to print the following pattern using nested loops:
    Exercise Purpose: Introduce Symmetrical Logic. It combines an increasing and a
        decreasing pattern. You learn to use two separate loop structures sequentially
        to create a complex visual shape.
    Given Input:
        rows = 5
    Expected Output: (As shown in the problem description)
        *
        * *
        ...
        * * * * *
        ...
        * *
        *
    """
    print("Exercise 25: Print pyramid pattern")
    pass
###########################################################


def exercise_26_full_multiplication_table():
    """
    Exercise 26. Print full multiplication table (1 to 10)
    Practice Problem: Write a program to print the full multiplication
        table from 1 to 10 in a grid format.
    Exercise Purpose: This is the ultimate test for Tabular Data Representation.
        It forces you to think about how nested loops interact. The outer loop represents
        the rows (multiplicands), and the inner loop represents the columns (multipliers).
        It also introduces the use of escape characters like \t (tab) to align
        text columns perfectly.
    Given Input:
        None (Range 1-10)
    Expected Output:
        1	2	3	4	5	6	7	8	9	10
        2	4	6	8	10	12	14	16	18	20
        ...
        10	20	30	40	50	60	70	80	90	100
    From solution provided at website:
        # Print product followed by a tab for alignment
        print(i * j, end="\t")
        # Move to the next line after finishing a row
        print()
    """
    print("Exercise 26: Print full multiplication table")
    final_results = []
    message = ""
    for i in range(1,11):
        message = f"{i:2}: "
        for j in range(1,11):
            item = f"{i*j:<4} "
            message += item

        final_results.append(message)
    # print results
    for line in final_results:
        print(line)
    print("")
    pass
###########################################################


def exercise_27_list_cumulative_sums():
    """
    Exercise 27. List Cumulative Sum: Each element is the sum of all previous
    Practice Problem: Given a list of numbers, create a new list where
        each element is the sum of all elements from the original list up to that position.
    Exercise Purpose: This introduces the Running Total pattern. It is
        essentially “memory” within a loop, carrying the result of previous
        iterations into the current one. This logic is used in financial ledgers
        to calculate a balance after each transaction.
    Given Input:
        [1, 2, 3, 4]
    Expected Output:
        Cumulative Sum: [1, 3, 6, 10]
    """
    print("Exercise 27: List Cumulative Sum")
    pass
###########################################################


def exercise_28_filter_dictionary():
    """
    Exercise 28. Dictionary Filter: Extract pairs where value exceeds a threshold.
    Practice Problem: Given a dictionary of student scores, create a new dictionary
        that only includes students who scored above a certain threshold (e.g., 75).
    Exercise Purpose: This exercise teaches Dictionary Iteration. Unlike lists,
        dictionaries have keys and values. You learn to use .items() to unpack
        both at once and how to conditionally build a new mapping.
    Given Input:
        scores = {"Alice": 85, "Bob": 70, "Charlie": 95, "David": 60}
        threshold = 75
    Expected Output:
        Passing Students: {'Alice': 85, 'Charlie': 95}
    """
    print("Exercise 28: Dictionary Filter")
    pass
###########################################################


def exercise_29_identify_common_elements():
    """
    Exercise 29. Find common elements (Intersection) using loop
    Practice Problem: Given two lists, find the elements that appear in both.
        Do not use Python’s built-in set().intersection() method.
    Exercise Purpose: This exercise focuses on Cross-Reference Iteration. It demonstrates
        how to use one collection as a master list and check its members against a
        secondary “filter” list to find commonalities.
    Given Input:
        list_a = [1, 2, 3, 4, 5]
        list_b = [4, 5, 6, 7, 8]
    Expected Output:
        Common elements: [4, 5]
    """
    print("Exercise 29: Find common elements")
    pass
###########################################################


def exercise_30_remove_duplicates():
    """
    Exercise 30. Remove duplicates without set
    Practice Problem: Write a program to remove all duplicate values from a list using a loop,
        maintaining the original order of elements.
    Exercise Purpose: Although set(list) quickly removes duplicates, it destroys order.
        This exercise teaches Uniqueness Validation, ensuring each piece of data is
        processed once while preserving sequence.
    Given Input:
        [1, 2, 2, 3, 4, 4, 4, 5]
    Expected Output:
        Unique List:
            [1, 2, 3, 4, 5]
    """
    print("Exercise 30. Remove Duplicates")
    pass
###########################################################


