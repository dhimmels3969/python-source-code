import types

#
# Exercises found at web page https://pynative.com/python-if-else-and-for-loop-exercise-with-solutions/
# Exercises 31 through 40
#


def exercise_31_segregate_items_in_list():
    """
    Exercise 31. Even/Odd Segregation: Move evens to front, odds to back
    Practice Problem: Given a list of integers, move all even numbers
        to the beginning of the list and all odd numbers to the end.
    Exercise Purpose: This introduces List Reorganization, a simplified version
        of the partitioning logic used in QuickSort algorithms. You learn to
        categorize data and reassemble it into a specific structural order.
    Given Input:
        [1, 2, 3, 4, 5, 6]
    Expected Output:
        Segregated List:
            [2, 4, 6, 1, 3, 5]
    """
    print("\nExercise 31. Sort odd and even numbers in a list.")
    even_list = []
    odd_list = []
    input_list = [1,2,3,4,5,6]
    output_list = []
    for item in input_list:
        if item % 2 == 0:
            even_list.append(item)
        else:
            odd_list.append(item)
    output_list.extend(even_list)
    output_list.extend(odd_list)
    print(output_list)
    pass
###########################################################


def exercise_32_list_rotation():
    """
    Exercise 32. List Rotation: Rotate elements left by k positions
    Practice Problem: Given a list and an integer k, rotate the list
        to the left by k positions. For example, if k=2, the first two elements
        move to the end of the list.
    Exercise Purpose: This exercise teaches Positional Manipulation. While slicing is common,
        using a loop helps you understand how data shifts in memory. This is a core concept for
        circular buffers and scheduling algorithms.
    Given Input:
        nums = [1, 2, 3, 4, 5]
        k = 2
    Expected Output:
        Rotated List: [3, 4, 5, 1, 2]
    """
    print("\nExercise 32. List Rotation")
    original_list = [1, 2, 3, 4, 5]
    number_of_rotations = 2
    print(f"Before: {original_list}")

    # for _ in range(k): We use an underscore _ as the variable name because
    # we don’t actually need the index; we just need the loop to run exactly k times.
    for _ in range(number_of_rotations):
        item_to_shift = original_list.pop(0)
        original_list.append(item_to_shift)
    print(f"After: {original_list}")
    pass
###########################################################


def exercise_33_word_frequency_counter():
    """
    Exercise 33. Word frequency counter
    Practice Problem: Write a program to count the frequency of each word in a given string.
    Exercise Purpose: This introduces Mapping Logic. You learn to transform a “flat”
        string into a structured dictionary. This is the starting point for almost
        all Natural Language Processing (NLP) tasks, such as building a search engine or a tag cloud.
    Given Input:
        text = "apple banana apple orange banana apple"
    Expected Output:
        {'apple': 3, 'banana': 2, 'orange': 1}
    """
    print("\nExercise 33. Word frequency counter")
    input_text = "apple banana apple orange banana apple"
    input_list = input_text.split()
    output_dict = {}
    for item in input_list:
        try:
            key = output_dict[item]
            # increment the counter for the item
            output_dict[item] = output_dict.get(item, 0) + 1
        except KeyError:
            output_dict[item] = 1
    print(output_dict)
    pass
###########################################################



def exercise_34_fibonacci_series(limit = 10):
    """
    Exercise 34. Display fibonacci series up to 10 terms
    Practice Problem: Write a program to display the Fibonacci sequence up to 10 terms.
        The sequence starts with 0 and 1, and each subsequent number is the sum of the two preceding ones.
    Exercise Purpose: This exercise teaches State Management. You keep track of
        two changing variables (n1 and n2) and update them in sync
        to crawl forward through the sequence.
    Given Input:
        n_terms = 10
    Expected Output:
        0 1 1 2 3 5 8 13 21 34
    """
    print("\nExercise 34. Fibonacci series up to 10 terms")
    first = 0
    second = 1
    list = []
    # add the first 2 numbers to the list
    list.append(first)
    list.append(second)
    counter = 0
    # adjust limit to account for the first 2 items in the list...
    limit -= 2
    while counter < limit:
        current = first + second
        list.append(current)
        # update first and second
        first = second
        second = current
        # increment the counter
        counter += 1
    print(list)
    pass
###########################################################



def exercise_35_perfect_number_check(number_to_test = 28):
    """
    Exercise 35. Perfect number check
    Practice Problem: Write a program to check if a number is a “Perfect Number.”
        A perfect number is a positive integer that is equal to the sum of its
        proper divisors (excluding the number itself). For example,
        6 is perfect because 1 + 2 + 3 = 6.
    Exercise Purpose: Emphasizes efficiency in search. While you
        could check every number up to n, you only need to check up
        to n/2 to find all divisors, showing how to optimize loop ranges.
    Given Input:
        num = 28
    Expected Output:
        28 is a Perfect Number (1 + 2 + 4 + 7 + 14 = 28)
    :returns
        string showing results of analysis of the number to test
    """
    results_list = []
    cumulative_total = 0
    number_message = "("
    # print("\nExercise 35. Perfect Number Check")
    for i in range(1, number_to_test // 2 + 1):
        if number_to_test % i == 0:
            results_list.append(i)
    for item in results_list:
        cumulative_total += item
        number_message = number_message + str(item)  + " + "
    number_message = number_message + ")"

    # format the message
    message = f"{number_to_test} is NOT a Perfect Number."
    if cumulative_total == number_to_test:
        message = f"{number_to_test} is a Perfect Number {number_message}."
        message = message.replace(" + )", " = ###)")
        message = message.replace("###", str(number_to_test))

    return message
###########################################################


def exercise_35_check_perfect_numbers_collection(lower_bound = 0, upper_bound = 100):
    """
    Exercise 35. Perfect number check
    Practice Problem: Write a program to check if a number is a “Perfect Number.”
        A perfect number is a positive integer that is equal to the sum of its
        proper divisors (excluding the number itself). For example,
        6 is perfect because 1 + 2 + 3 = 6.
    Exercise Purpose: Emphasizes efficiency in search. While you
        could check every number up to n, you only need to check up
        to n/2 to find all divisors, showing how to optimize loop ranges.
    Given Input:
        num = 28
    Expected Output:
        28 is a Perfect Number (1 + 2 + 4 + 7 + 14 = 28)
    :returns
        string showing results of analysis of the number to test
    """
    results_list = []
    print("\nExercise 35. Perfect Number Check - Multiple Entries")
    for number_to_check in range(lower_bound, upper_bound + 1):
        results_list.append(exercise_35_perfect_number_check(number_to_check))
    for item in results_list:
        if str(item.lower()).__contains__("is a Perfect Number".lower()):
            print(item)
    return None
###########################################################


def exercise_36_binary_decimal_conversion(binary_str = "1101"):
    """
    Exercise 36. Binary to decimal conversion using loop
    Practice Problem: Manually convert a binary string (e.g., "1101")
        into its decimal integer equivalent using a loop. Do not use int(binary, 2).
    Exercise Purpose: This exercise teaches Positional Notation and Powers.
        It helps you visualize how computers store numbers and process strings
        from right to left or vice versa to apply mathematical weights.
    Given Input:
        binary_str = "1101"
    Expected Output:
        Decimal value: 13
    """
    print("\nExercise 36. Binary to decimal conversion using loops")
    final_result = 0
    power = 1
    for i in range(len(binary_str)-1, -1, -1):
        digit = int(binary_str[i])
        amount = digit * power
        final_result += amount
        power *= 2
    print(f"Binary Value: {binary_str}   Decimal value: {final_result}")
    pass
###########################################################



def is_prime(n):
    """
    Use the Sieve of Eratosthenes Algorithm to determine if a number is prime.
    :param n:
    :type n:
    :return:
    :rtype:
    """
    if n < 2:
        return False

    sieve = [True] * (n + 1)
    sieve[0] = sieve[1] = False

    for i in range(2, int(n**0.5) + 1):
        if sieve[i]:
            for j in range(i * i, n + 1, i):
                sieve[j] = False

    return sieve[n]


def exercise_37_display_prime_numbers():
    """
    Exercise 37. Display all prime numbers within a range
    Practice Problem: Write a program to display all prime numbers within a range (e.g., 25 to 50).
        A prime number is a natural number greater than 1 that is not a product of two smaller
        natural numbers.
    Exercise Purpose: This is a classic test of Nested Loop Logic. You iterate
        through a range of numbers (outer loop) and, for each,
        run another loop (inner loop) to check if any smaller number
        divides it evenly. It’s excellent for practicing flag variables or the loop-else construct
    Given Input:
        start = 25, end = 50
    Expected Output:
        Prime numbers between 25 and 50 are:
        29
        31
        37
        41
        43
        47
    """
    print("\nExercise 37. Display all prime numbers within a range")
    start = 25
    end = 50
    prime_list = []
    for n in range(start, end + 1):
        if is_prime(n):
            prime_list.append(n)
    print(f"Prime numbers between {start} and {end} are: ")
    for item in prime_list:
        print(item)
    pass
###########################################################



def exercise_38_find_sum_of_series():
    """
    Exercise 38. Find the sum of the series up to n terms
    Practice Problem: Write a program to calculate the sum of the
        series 2 + 22 + 222 + 2222 + …. up to N terms.
        For example, if n=5, the series is 2 + 22 + 222 + 2222 + 22222.
    Exercise Purpose: This advanced Pattern Accumulation exercise
        requires generating a new number at each step by multiplying
        the previous number by 10, adding 2, and then adding that
        result to a running total.
    Given Input:
        number_of_terms = 5
    Expected Output:
        24690
    """
    print("\nExercise 38. Find the sum of the series up to n terms")
    item = 0
    number_of_terms = 5
    digit = 2
    terms_list = []
    for i in range(number_of_terms):
        item += digit * (10**i)
        terms_list.append(item)
    print(f"Sum of series up to {number_of_terms} terms: {sum(terms_list)}")
    pass
###########################################################



def exercise_39_flatten_list():
    """
    Exercise 39. flatten a nested list using loops
    Practice Problem: Given a nested list (a list containing other lists),
        write a program to “flatten” it into a single list containing
        all the individual elements.
    Exercise Purpose: In data science and web development, data often arrives
        in “nested” formats (like JSON). This exercise teaches you
        Dimensionality Reduction. You learn how to “reach inside”
        one container to pull items out and place them into a new, simpler container.
`   Given Input:
        nested_list = [[10, 20], [30, 40], [50, 60]]
    Expected Output:
        [10, 20, 30, 40, 50, 60]
    """
    print("\nExercise 39. flatten list")
    nested_list = [[10, 20], [30, 40], [50, 60]]
    final_results = []
    for item in nested_list:
        for item_2 in item:
            final_results.append(item_2)
    print(f"Original Input: {nested_list}")
    print(f"Final Result: {final_results}")
    pass
###########################################################



def exercise_40_nested_list_search():
    """
    Exercise 40. Nested list search (2D matrix coordinates)
    Practice Problem: Given a 2D list (matrix), find the row and column index of a target value.
    Exercise Purpose: This is the foundation of Coordinate Systems.
        You learn to use nested loops, where the outer loop iterates over rows,
        and the inner loop iterates over columns. This logic is essential for
        game development, image processing, and spreadsheet automation.
    Given Input:
        matrix = [[10, 20], [30, 40], [50, 60]]
        target = 30
    Expected Output:
        Target 30 found at Row: 1, Column: 0
    """
    print("\nExercise 40. Nested list search")
    matrix = [[10, 20], [30, 40], [50, 60], [112, 56], [240, 30]]
    target = 30
    for i in range (len(matrix)):
        item = matrix[i]
        for j in range (len(item)):
            if item[j] == target:
                print(f"Target {target} found at Row: {i}, Column: {j}")

    pass
###########################################################
