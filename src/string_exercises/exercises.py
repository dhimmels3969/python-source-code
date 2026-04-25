#
# Exercises found at web page https://pynative.com/python-string-exercise/
# Exercises 1 through 10
#

import itertools





#######################################################################################################
def exercise_01_grab_first_middle_last_character():
    """
    Exercise 1. Create a string made of the first, middle, and last character
    Practice Problem: Write a program to create a new string made
        of an input string’s first, middle, and last characters.
    Exercise Purpose: This exercise teaches the fundamentals of String Indexing.
        Accessing specific positions, especially the middle that requires calculating length,
        is a foundational skill for data parsing and text manipulation.
    Given Input:
        str1 = "James"
    Expected Output:
        Jms
    """
    print("Exercise 1. Create a string made of the first, middle, and last character")
    str1 = "James"
    first = str1[0]
    middle = str1[len(str1) // 2]
    last = str1[-1]
    result = "".join([first, middle, last])
    print(result)
    return None


#######################################################################################################
def exercise_02_grab_middle_three_characters():
    """
    Exercise 2. Create a string made of the middle three characters
    Practice Problem: Write a program to create a new string made of the
        middle three characters of an input string of odd length.
    Exercise Purpose: This builds on indexing by introducing String Slicing. Slicing is a powerful
        Python feature that lets you extract entire “chunks” of data efficiently.
    Given Input:
        str1 = "JhonDipPeta"
    Expected Output:
        Dip

    solution from website
        # Find middle index
        mi = int(len(str1) / 2)
        # Slice string from (mid - 1) to (mid + 2)
        res = str1[mi - 1:mi + 2]
    """
    print("Exercise 2. Create a string made of the middle three characters")
    str1 = "JhonDipPeta"
    total_len = len(str1)
    chars_to_grab = 3
    offset = (total_len - chars_to_grab) // 2
    result = str1[offset:offset + chars_to_grab]
    print(result)
    pass


#######################################################################################################
def exercise_03_insert_data_in_middle_of_string():
    """
    Exercise 3. Append new string in the middle of a given string
    Practice Problem: Given two strings, s1 and s2,
        create a new string by appending s2 in the middle of s1.
    Exercise Purpose: This exercise introduces String Partitioning and Concatenation.
        In programming, you often need to “inject” data into a template or
        modify strings at specific locations.
    Given Input:
        s1 = "Ault"
        s2 = "Kelly"
    Expected Output:
        AuKellylt
    """
    print("Exercise 3. Append new string in the middle of a given string")
    s1 = "Ault"
    s2 = "Kelly"
    midpoint = len(s1) // 2
    head = s1[:midpoint]
    tail = s1[midpoint:]
    result = "".join([head, s2, tail])
    print(result)
    pass


#######################################################################################################
def exercise_04_create_new_string():
    """
    Exercise 4. Create a new string made of the first, middle,
        and last characters of each input string
    Practice Problem: Given two strings, s1 and s2, create a new string
        from the first, middle, and last characters of each input string.
    Exercise Purpose: This exercise practices Complex Concatenation. It requires
        multiple independent extractions and organizing them into a single result,
        common when generating IDs or codes from user data.
    Given Input:
        s1 = "America"
        s2 = "Japan"
    Expected Output:
        AJrpan
    """
    print("Exercise 4. Create a new string from the first, middle,")
    s1 = "America"
    s1_midpoint = len(s1) // 2
    s2 = "Japan"
    s2_midpoint = len(s2) // 2
    s1_list = [s1[0], s1[s1_midpoint], s1[-1]]
    s2_list = [s2[0], s2[s2_midpoint], s2[-1]]
    results_list = itertools.chain.from_iterable(zip(s1_list, s2_list))
    final_result = "".join(results_list)
    print(final_result)
    pass


#######################################################################################################
def exercise_05_reverse_a_string():
    """
    Exercise 5. Reverse a given string
    Practice Problem: Write a program to reverse a given string.
    Exercise Purpose: Reversing a string is a classic logic-building exercise.
        In Python, this is most efficiently done via Slicing, demonstrating the
        language’s ability to manipulate sequences using “steps.” It is a
        prerequisite for solving problems like palindrome detection.
    Given Input:
        str1 = "PYnative"
    Expected Output:
        evitanYP
    """
    print("Exercise 5. Reverse a given string")
    str1 = "PYnative"
    final_result = str1[-1::-1]
    print(final_result)
    print()
    pass


#######################################################################################################
def exercise_06_find_last_occurrence():
    """
    Exercise 6. Find the last position of a given substring
    Practice Problem: Write a program to find the last index of the
        substring “Emma” in a given string.
    Exercise Purpose: While the .find() method searches from the beginning
        of a string, the .rfind() method (Reverse Find) locates the most
        recent occurrence of a specified pattern. This functionality is
        essential when parsing file paths or URLs that require identification of the final delimiter.
    Given Input:
        str1 = "Emma is a data scientist who knows Python. Emma works at google."
    Expected Output:
        Last occurrence of Emma starts at index 43
    """
    print("Exercise 6. Find the last occurrence of a given substring")
    str1 = "Emma is a data scientist who knows Python. Emma works at google."
    results = str1.rfind("Emma")
    print(f"Last occurrence of Emma starts at index {results}")
    pass


#######################################################################################################
def exercise_07_split_string_using_delimiter():
    """
    Exercise 7. Split a string on hyphens
    Practice Problem: Write a program to split a given string
        on hyphens and display each substring.
    Exercise Purpose: This exercise introduces the concept of tokenization.
        Dividing strings into smaller components based on delimiters, such
        as commas, spaces, or hyphens, is a common technique for
        processing CSV files, logs, and user-entered lists.
    Given Input:
        str1 = "Emma-is-a-data-scientist"
    Expected Output:
    Displaying each substring:
        Emma
        is
        a
        data
        scientist
    """
    print("Exercise 7. Split a given string")
    str1 = "Emma-is-a-data-scientist"
    results = str1.split("-")
    for item in results:
        print(item)
    pass


#######################################################################################################
def exercise_08_find_all_occurrences():
    """
    Exercise 8. Find all occurrences of a substring in a given string by ignoring the case
    Practice Problem: Write a program to find the total count of the substring “USA”
        in a given string, ignoring the case (i.e., both “usa” and “USA” should be counted).
    Exercise Purpose: This exercise addresses case normalization. In practical
        data science and web scraping applications, text data is frequently
        inconsistent. Converting all text to lowercase prior to processing is
        considered a standard best practice.
    Given Input:
        str1 = "Welcome to USA. usa awesome, isn't it?"
    Expected Output:
        The USA count is: 2
    """
    print("Exercise 8. Find all occurrences of a substring in a given string")
    str1 = "Welcome to USA. usa awesome, isn't it?"
    search_arg = "usa"
    results = str1.lower().count(search_arg)
    print(f"The USA count is: {results}")
    pass


#######################################################################################################
def exercise_09_balanced_strings_check():
    """
    Exercise 9. String characters balance test
    Practice Problem: Write a program to check if two strings are balanced.
        For example, strings s1 and s2 are balanced if all the characters in s1
        are present in s2. The character’s position doesn’t matter.
    Exercise Purpose: This exercise focuses on membership testing. This
        fundamental concept is utilized in data validation, such as verifying
        whether a password contains required characters or determining if a
        search query matches a database entry.
    Given Input:
        Case 1: s1 = "yn", s2 = "PyNative"
        Case 2: s1 = "ynf", s2 = "PyNative"
    Expected Output:
        Case 1: True
        Case 2: False
    """
    print("Exercise 9. String characters balance test")
    s1 = "yn"
    s2 = "PyNative"
    results = (s2.lower().count(s1)) >  0
    print(f"Case 1: {results}")

    s1 = "ynf"
    results = (s2.lower().count(s1)) >  0
    print(f"Case 2: {results}")
    pass


#######################################################################################################
def exercise_10_vowel_counter():
    """
    Exercise 10. Vowel Counter
    Practice Problem: Write a program to count the total number
        of vowels (a, e, i, o, u) in a given string.
    Given Input:
        str1 = "Hello World"
    Expected Output:
        Vowel Count: 3
    """
    print("Exercise 10. Vowel Counter")
    str1 = "Hello World"
    vowel_counter = 0
    for char in str1:
        if char.lower() in "aeiou":
            vowel_counter += 1
    print(f"Vowel Count: {vowel_counter}")
    print()
    pass