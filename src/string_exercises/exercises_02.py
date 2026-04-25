#
# Exercises found at web page https://pynative.com/python-string-exercise/
# Exercises 11 through 20
#





#######################################################################################################
def exercise_11_prefix_suffix_check():
    """
    Exercise 11. Prefix/Suffix Check
    Practice Problem: Check if a given URL starts with “https” and ends with “.com”.
    Exercise Purpose: This exercise teaches Boolean Validation. Methods like .startswith()
        and .endswith() are cleaner and less error-prone than manual slicing for
        verifying file formats, protocols, or naming conventions.
    Given Input:
        str1 = "https://google.com"
    Expected Output:
        Is valid URL: True
    """
    print("Exercise 11. Prefix/Suffix Check")
    pass



#######################################################################################################
def exercise_12_swap_case():
    """
    Exercise 12. Swap Case
    Practice Problem: Write a program to toggle the case of all characters in a
        string (uppercase becomes lowercase and vice versa).
    Exercise Purpose: This demonstrates Case Transformation. Though simple, it is
        often used in search algorithms to normalize data or in text editors
        to provide “Toggle Case” functionality.
    Given Input: str1 =
        "PyThOn"
    Expected Output:
        pYtHoN
    """
    print("Exercise 12. Swap Case")
    pass



#######################################################################################################
def exercise_13_remove_whitespace():
    """
    Exercise 13. Remove Whitespace
    Practice Problem: Remove every single space from a given string, including spaces between words.
    Exercise Purpose: This highlights the difference between Trimming and Filtering.
        While .strip() only removes leading/trailing spaces, .replace() can
        reach inside a string to remove characters globally.
    Given Input:
        str1 = " P y t h o n "
    Expected Output:
        Python
    """
    print("Exercise 13. Remove Whitespace")
    pass



#######################################################################################################
def exercise_14_character_removal():
    """
    Exercise 14. N-th Character Removal
    Practice Problem: Write a program to remove the character at index i from a string.
    Exercise Purpose: Since Python strings are Immutable (you can’t just
        delete a character at an index), this exercise teaches you how
        to “reconstruct” a string by skipping over a specific part.
    Given Input:
        str1 = "Python", i = 2
    Expected Output:
    """
    print("Exercise 14. N-th Character Removal")
    pass



#######################################################################################################
def exercise_15_string_partition_test():
    """
    Exercise 15. String Partitioning
    Practice Problem: Use the .partition() method to split a string into three parts:
        the part before a separator, the separator itself, and the part after it.
    Exercise Purpose: .split() is great for breaking a string into many
        pieces. .partition() is a specialized tool that always returns a 3-tuple.
        It is especially useful for parsing data like email addresses or key-value
        pairs where the separator needs to be preserved or accounted for.
    Given Input:
        str1 = "username@company.com", sep = "@"
    Expected Output:
        ('username', '@', 'company.com')
    """
    print("Exercise 15. String Partitioning")
    pass



#######################################################################################################
def exercise_16_extract_file_extension():
    """
    Exercise 16. Extract File Extension
    Practice Problem: Given a filename as a string, extract only
        the file extension (e.g., .png or .pdf).
    Exercise Purpose: This exercise teaches String Parsing. In software development,
        you need to validate file types before processing uploads. It helps you practice
        finding the last occurrence of a character (the dot) to handle files
        with multiple dots correctly (like archive.tar.gz).
    Given Input:
        file_name = "report_final_v2.pdf"
    Expected Output:
        pdf
    """
    print("Exercise 16. Extract File Extension")
    pass



#######################################################################################################
def exercise_17_sort_lower_case_and_upper_case():
    """
    Exercise 17. Lowercase First
    Practice Problem: Write a program to arrange string characters such that
        all lowercase letters come first, followed by all uppercase letters.
    Exercise Purpose: This exercise introduces Conditional Filtering and Reassembly.
        It’s a common pattern in data sorting: you need to group items by a
        specific property (in this case, “casing”) while preserving their relative order.
    Given Input:
        str1 = "PyNaTive"
    Expected Output:
        yaivePNT
    """
    print("Exercise 17. Sort Lowercase First")
    pass



#######################################################################################################
def exercise_18_count_letters_digits_symbols():
    """
    Exercise 18. Count all letters, digits, and special symbols from a given string
    Practice Problem: Write a program to count all letters, digits,
        and special symbols from a given string.
    Exercise Purpose: This introduces Character Classification. Using
        built-in string methods like .isalpha() and .isdigit() is the
        standard way to validate user input and perform data cleaning.
    Given Input:
        str1 = "P@#yn26at^&i5ve"
    Expected Output:
        Total counts of chars, digits, and symbols: Chars = 8 Digits = 3 Symbol = 4
    """
    print("Exercise 18. Count All Letters, Digits, and Symbols")
    pass



#######################################################################################################
def exercise_19_alternating_characters():
    """
    Exercise 19. Create a mixed string using alternating characters
    Practice Problem: Given two strings, s1 and s2, create a third string made
        of the first char of s1, then the last char of s2, Next, the second char
        of s1 and the second-to-last char of s2, and so on. Any left-over
        chars go at the end of the result.
    Exercise Purpose: This exercise sharpens your ability to handle Multiple Pointer Traversal.
        It makes you think about coordinating indices moving in opposite directions
        (forward through one string and backward through another).
    Given Input:
        s1 = "Abc"
        s2 = "Xyz"
    Expected Output:
        AzbycX
    """
    print("Exercise 19. Create a mixed string using alternating characters")
    pass



#######################################################################################################
def exercise_20_calculate_sums_and_averages():
    """
    Exercise 20. Calculate the sum and average of the digits present in a string
    Practice Problem: Given a string, run a loop to calculate the sum and
        average of the digits that appear in the string. Ignore all other characters.
    Exercise Purpose: This combines Data Extraction with Arithmetic Operations.
        It demonstrates how to filter relevant data (numbers) out of a “noisy” string
        (letters and symbols) to perform calculations.
    Given Input:
        str1 = "PYnative29@#8496"
    Expected Output:
        Sum is: 38 Average is 6.33
    """
    print("Exercise 20. Calculate Sum and Average")
    pass



