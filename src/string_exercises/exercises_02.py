#
# Exercises found at web page https://pynative.com/python-string-exercise/
# Exercises 11 through 20
#
from email import message


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
    str1 = "https://google.com"
    validUrl = False
    if str1.startswith("https") & str1.endswith(".com"):
        validUrl = True
    print(f"Is valid URL: {validUrl}")
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
    Given Input:
        str1 = "PyThOn"
    Expected Output:
        pYtHoN
    """
    print("Exercise 12. Swap Case")
    str1 = "PyThOn"
    result = ""
    for i in range(len(str1)):
        if str1[i].islower():
            result += str1[i].upper()
        else:
            result += str1[i].lower()
    print(result)
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
    str1 = " P y t h o n "
    result = str1.replace(" ", "")
    print(result)
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
        Pyhon (The character 't' at index 2 was removed)
    """
    print("Exercise 14. N-th Character Removal")
    str1 = "Python"
    i = 2
    head = str1[:i]
    tail = str1[i+1:]
    result = "".join([str1[:i], str1[i+1:]])
    message = f"{result} (The character 't' at index 2 was removed)"
    print(message)
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
    str1 = "username@company.com"
    sep = "@"
    partition_tuple = str1.partition(sep)
    print(partition_tuple)
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
    file_name = "report_final_v2.pdf"
    offset = file_name.find(".")
    file_name_len = len(file_name)
    file_extension = file_name[offset + 1:file_name_len]

    # from website
    extension = file_name.split(".")[-1]

    print(f"{file_extension}")
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
    Could this be done with a regular expression???
    """
    print("Exercise 17. Sort Lowercase First")
    str1 = "PyNaTive"
    head = ""
    tail = ""
    for char in str1:
        if char >= "a" and char <= "z":
            head += char
        else:
            tail += char
    result = "".join([head, tail])
    print(result)
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
    str1 = "P@#yn26at^&i5ve"
    alpha_count = 0
    digits_count = 0
    symbols_count = 0
    for char in str1:
        if char.isalpha():
            alpha_count += 1
        else:
            if char.isdigit():
                digits_count += 1
            else:
                symbols_count += 1
    message = f"Total counts of chars, digits, and symbols: Chars = {alpha_count} Digits =  {digits_count} Symbol = {symbols_count}"
    print(message)

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

    def build_string_from_two_inputs(s1, s2):
        s1_len = len(s1)
        s2_len = len(s2)
        # Use length of the bigger string
        length = max(s1_len, s2_len)
        result = ""
        # Reverse s2 to make it easier to pick characters from the end
        s2 = s2[::-1]
        # build the single string from the two inputs
        for i in range(length):
            if i < s1_len:
                result += s1[i]
            if i < s2_len:
                result += s2[i]
        return result

    print("Exercise 19. Create a mixed string using alternating characters")
    s1 = "Abc"
    s2 = "Xyz"
    result = build_string_from_two_inputs(s1, s2)
    print(result)

    print("Test of two strings of unequal length")
    s3 = "Whale"
    s4 = "Rhododendron"
    result = build_string_from_two_inputs(s3, s4)
    print(result)
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
    str1 = "PYnative29@#8496"
    number_list = []
    for char in str1:
        if char.isdigit():
            number_list.append(int(char))
    total = sum(number_list)
    average = total/len(number_list)
    print(f"Sum is {total}")
    print(f"Average is {average:.3}")
    print()
    pass



