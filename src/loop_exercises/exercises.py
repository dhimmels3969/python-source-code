# from html.parser import incomplete
from src.common_library import helper_functions as hf
import loop_exercises.exercises_04 as l4

#
# Exercises found at web page https://pynative.com/python-if-else-and-for-loop-exercise-with-solutions/
# Exercises 1 through 10
#





#######################################################################################################
def exercise_01_print_numbers_using_while(limit):
    """
    Exercise 1. Print first 10 natural numbers using while loop
    Practice Problem: Write a program to print the first 10 natural
        numbers using a while loop. Each number should be printed on a new line.
    Exercise Purpose: This is the fundamental introduction to iteration. It
        teaches how to set up a loop condition to execute a block of code
        repeatedly, and manually manage a counter variable to prevent infinite loops.
    """
    incomplete = True
    i = 1
    while incomplete:
        print(i)
        i += 1
        if i > limit:
            incomplete = False

    return None


def exercise_02_display_negative_numbers():
    """
    Exercise 2. Display numbers from -10 to -1 using for loop
    Practice Problem: Write a program to display numbers from -10 to -1 using a for loop.
    Exercise Purpose: This exercise focuses on Negative Indexing and Ranges.
        Understanding how Python handles negative numbers in the range() function
        is crucial for algorithms involving coordinate systems or countdowns.
    Given Input:
        None
    Expected Output:
        -10
        -9
        ...
        -1
    """
    print("\nExercise 2. display_negative_numbers")
    for i in range(-10, 0):
        print(i)
    pass


def exercise_03_loop_completion_test():
    """
    Exercise 3. Display a message “Done” after successful execution of for loop
    Practice Problem: Write a program to display a message “Done” after
        the successful execution of a for loop that iterates from 0 to 4.
    Exercise Purpose: This introduces a unique Python feature: the Loop-Else Clause.
        Unlike if-else, a loop else block only executes if the loop completes all
        its iterations without being interrupted by a break statement. This is
        useful for search loops to signal that a target was not found.
    Given Input:
        None
    Expected Output:
        0
        1
        2
        3
        4
        Done!
    """
    print("\nExercise 3. Loop-Else Clause")
    for i in range(5):
        print(i)
    else:
        print("Done!")
    pass


def exercise_04_calculate_sum():
    """
    Exercise 4. Calculate the sum of all numbers from 1 to N
    Practice Problem: Write a program that accepts a number from
        the user and calculates the sum of all numbers from 1 up to that number.
    Exercise Purpose: This exercise teaches Value Accumulation. It shows
        how to use a loop to process data and store a running total in a
        variable, a common task in data processing.
    Given Input:
        Enter number: 10
    Expected Output:
        Sum is: 55
    """
    incomplete = True
    while incomplete:
        user_number = input("Enter number greater than 0: ")
        try:
            user_number = int(user_number)
            if user_number > 0:
                incomplete = False
            else:
                print("Number must be greater than 0. Please try again.")

        except ValueError:
            print("Previous value was invalid. Enter a number.")

    # now calculate the sum the old-fashioned way...
    cumulative_total = 0
    counter = 1
    while counter <= user_number:
        cumulative_total += counter
        # print(cumulative_total)
        counter += 1

    print(f"\nSum is: {cumulative_total}")
    pass


def exercise_05_multiplication_table(number: int, multiplier):
    """
    Exercise 5. Print multiplication table of a given number
    Practice Problem: Create a program that takes an integer
        and prints its multiplication table from 1 to 10.
    Exercise Purpose: This reinforces the use of loops for generating
        Mathematical Sequences. It shows how to use the loop index (i)
        as a multiplier against a fixed constant.
    Given Input:
        2
    Expected Output:
        2
        4
        6
        ...
        20
    """
    print("\nExercise 5. Multiplication Table")

    for i in range(1, 11):
        message = f"{number} times {i} equals {i * number}"
        print(message)
    print("")
    pass


def exercise_06_calculate_cube():
    """
    Exercise 6. Calculate the cube of all numbers from 1 to a given number
    Practice Problem: Write a program that takes an integer n and prints
        the cube of every number from 1 to n in the format Current Number is : 1 and the cube is 1.
    Exercise Purpose: This exercise teaches Result Formatting and Power Operations.
        It shows how to combine text with calculated variables using f-strings or commas
        and perform exponentiation with the ** operator or pow() function.
    Given Input:
        input_number = 6
    Expected Output:
        Current Number is : 1  and the cube is 1
        Current Number is : 2  and the cube is 8
        ...
        Current Number is : 6  and the cube is 216
    :return:
    :rtype:
    """
    print("Exercise 6. Calculate the cube of every number from 1 to n")
    given_number = hf.get_positive_int_from_user("Enter number greater than 0: ")
    for i in range(1, given_number + 1):
        message = f"Current number is : {i} and the cube is {i ** 3}"
        print(message)
    print("")
    pass


def exercise_07_display_list_items():
    """
    Exercise 7. Display numbers from a list using a loop
    Practice Problem: Given a list of numbers, iterate through it
        and print numbers that satisfy these conditions:
        1. The number must be divisible by five.
        2. If the number is greater than 150, skip it and move to the next.
        3. If the number is greater than 500, stop the loop entirely.
    Exercise Purpose: This vital Flow Control exercise introduces continue (to skip)
        and break (to exit), essential for writing efficient code that
        avoids processing unnecessary data.
    Given Input:
        numbers = [12, 75, 150, 180, 145, 525, 50]
    Expected Output:
        75
        150
        145

    :return:
    :rtype:
    """
    results = []
    print("Exercise 7. Display numbers from a list using a loop")
    numbers = [12, 75, 150, 180, 145, 525, 50]
    for item in numbers:
        if item % 5 == 0 and item <= 150:
            message = f"{item}"
            print(message)
        if item > 500:
            break
    pass


def exercise_08_count_occurrences():
    """
    Exercise 8. Count occurrences of a specific element in a list
    Practice Problem: Given a list of numbers, use a loop to count
        how many times a specific number (e.g., 10) appears.
    Exercise Purpose: This introduces Frequency Counting, a staple
        of data analysis. It shows how to iterate through a collection
        and use a conditional filter to increment a tally only when a match is found.
    Given Input:
        list1 = [10, 20, 10, 30, 10, 40, 50]
        target = 10
    Expected Output:
        10 appears 3 times
    :return:
    :rtype:
    """
    print("Exercise 8. Count occurrences of a specific element in a list")
    list1 = [10, 20, 10, 30, 10, 40, 50]
    target = 10
    target_found = 0
    for item in list1:
        if item == target:
            target_found += 1
    print(f"{target} appears {target_found} times")
    pass


def exercise_09_odd_index_positions():
    """
    Exercise 9. Print elements from a list present at odd index positions
    Practice Problem: Given a Python list, use a loop to print only
        the elements that are located at odd index positions (index 1, 3, 5, etc.).
    Exercise Purpose: This exercise teaches Index-Based Iteration. It
        helps you distinguish between an item’s value in a list and
        its position (index), which is fundamental for data filtering.
    Given Input:
        my_list = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
    Expected Output:
        [20 40 60 80 100]
    :return:
    :rtype:
    """
    print("Exercise 9. Print elements from a list present at odd index positions")
    results = []
    my_list = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
    for i in range(my_list.__len__()):
        if i % 2 == 1:
            results.append(my_list[i])
    print(results)
    return None


def exercise_10_print_list_in_reverse_order():
    """
    Exercise 10. Print list in reverse order using a loop
    Practice Problem: Given a list, iterate it in reverse order and print each element.
    Exercise Purpose: Learning to Traverse Data Backwards is essential
        for many data structures. This exercise shows how to use the reversed()
        function or custom range slicing to iterate over a list
        from the end to the beginning.
    Given Input:
        list1 = [10, 20, 30, 40, 50]
    Expected Output:
        [50, 40, 30, 20, 10]
    :return:
    :rtype:
    """
    print("Exercise 10. Print list in reverse order using a loop")
    list1 = [10, 20, 30, 40, 50]
    for i in range (list1.__len__(),0,-1):
        print(list1[i-1])
    pass