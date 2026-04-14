import os
import re
# from html.parser import incomplete
from shlex import join
import locale
import pwinput
import getpass
from pathlib import Path
import secrets
import random
import string
from typing import List, Tuple, Optional

locale.setlocale(locale.LC_ALL, '')


####
#### https://pynative.com/python-input-and-output-exercise/
#### 3/28/2026 7:58 AM
####


def exercise_01_process_two_numbers_driver(limit):
    keep_going = True
    while keep_going:
        final_results = process_two_numbers(limit)
        print(final_results)
        print("================================\n\n")
        choice = input("Do you want to continue? (y/n): ")
        if choice.lower() == "n":
            keep_going = False

def process_two_numbers(limit):
    """
    Practice Problem: Write a Python function that accepts two integer numbers. If the product of the two numbers is less than or equal to 1000, return their product; otherwise, return their sum.
    Exercise Purpose: Learn basic control flow and the use of if-else statements. Understand how code decisions change output based on a mathematical threshold.
    Given Input:
        •	Case 1: number1 = 20, number2 = 30
        •	Case 2: number1 = 40, number2 = 30
    Expected Output:
        •	The result is 600
        •	The result is 70

    :return:
    :rtype:
    """
    incomplete = True
    arguments = []
    while incomplete:
        number = input("Enter a number: ")
        try:
            user_input_num = int(number)
            arguments.append(user_input_num)
            if arguments.__len__() > 1:
                incomplete = False
        except ValueError:
            print("Invalid item. Please enter a whole number. Try again.")

        # if isinstance(int(number), int):

    result = arguments[0] * arguments[1]
    if result > limit:
        result = arguments[0] + arguments[1]
    final_results = f"The result is {result}"
    return final_results


def format_print_statement():
    """
    Exercise 2: Format Output String
    Write a program to display four string “My, “Name“, “Is“, “James” as “My**Name**Is**James“.

    Use the print() function to format the given words in the specified format. Display the ** separator between each string.

    Given:

    str1 = 'My'
    str2 = 'Name'
    str3 = 'Is'
    str4 = 'James'
    Expected Output:

    For example: print('your code') should display My**Name**Is**James
    """
    s1 = 'My'
    s2 = 'Name'
    s3 = 'Is'
    s4 = 'James'
    print(s1, s2, s3, s4, sep="**")
    return None

def format_octal_print_statement(number_in):
    """
        Exercise 3: Display Decimal Number to Octal using print() function
        Given:
            num = 8
        Expected Output:
            The octal representation of the decimal number 8 is 10.
    """
    print("The octal representation of the decimal number %s is %o" % (number_in, number_in))
    print(f"[F strings] The octal representation of the decimal number {number_in} is {number_in:o}")
    return None

def display_float_with_two_decimal_places(num):
    """
    Exercise 4/7: Display Float Number with 2 Decimal Places
    Given:
        num = 458.541315
    Expected Output:
        458.54
    """
    print("Number in: %s, with 2 decimal places %.2f" % (num, num))
    print(f"[F strings] Number in: {num}, with 2 decimal places {num:.2f}")
    pass

def process_floats_from_user(size_of_list):
    """
    Exercise 5: Accept a list of 5 float numbers as an input from the user
    Expected Output:
        [78.6, 78.6, 85.3, 1.2, 3.5]

    :return:
    :rtype:
    """
    incomplete = True
    arguments = []
    while incomplete:
        number = input("Enter a number: ")
        try:
            user_input_num = float(number)
            arguments.append(user_input_num)
            if arguments.__len__() >= size_of_list:
                incomplete = False
        except ValueError:
            print("Invalid item. Please enter either an integer or a decimal number. Try again.")

        # if isinstance(int(number), int):

    final_results = arguments
    return final_results

def build_file_name(src_dir, file_name):
    """
    This function builds a file name.
    Args:
        file_name (string): name of the file the user wants to read.
    Returns:
        a file name
    Assumption:
        The source code is in an src folder and there is a data folder at the same level
        as the src folder and the file exists in the data folder.
    """

    # Get the directory of the current source file
    try:

        # current_dir = os.path.dirname(__file__)
        current_dir = src_dir

        # Construct the path to the JSON file in the /data directory
        json_path = os.path.join(current_dir, '..', 'data', file_name)

        # Normalize the path (optional but recommended)
        json_path = os.path.normpath(json_path)

        # return the config information to the calling function
        return json_path
    except Exception as error:
        raise error



def exercise_06_write_file():
    """
    Exercise 6: Write all content of a file into a new file by skipping line number 5
    Create a test.txt file and add the below content to it.
    Given test.txt file:
        line1
        line2
        line3
        line4
        line5
        line6
        line7
    Expected Output: new_file.txt
        line1
        line2
        line3
        line4
        line6
        line7
    :return:
    :rtype:
    """
    file_path = build_file_name("test.txt")
    with open(file_path, 'r') as file:
        lines_in_the_file = file.readlines()
    #### filter out line 5 (index = 4)
    items_to_skip = [4]
    #### create the output list
    lines_to_write = [x for i, x in enumerate(lines_in_the_file) if i not in items_to_skip]

    #### write the data to an output file
    #### first build the name of the file
    file_path = build_file_name("test_out.txt")
    #### open the file and write the data
    with open(file_path, 'w') as file_out:
        file_out.writelines(lines_to_write)

    pass


def exercise_05_multiple_input_test():
    """
    Exercise 7: Accept any three string from one input() call
        Write a program to take three names as input from the user in a single call to the input() function.
        Expected Output
            Enter three string Emma Jessa Kelly
            Name1: Emma
            Name2: Jessa
            Name3: Kelly

    :return:
    :rtype:
    https://pythonguides.com/split-strings-with-multiple-delimiters-in-python/
    """
    names_in = input("Enter 3 names separated by spaces: ")
    print("Using split string function")
    names_out = names_in.split(" ")
    print(names_out)

    print("\nUsing regular expressions")
    #### list of delimiters inside [] + specifies multiple occurrences
    separators = r"[,;~:]+\s*"
    names_in = input("Enter 3 names using separators(comma semi-colon tilde colon): ")
    names_out = re.split(separators, names_in)
    print(names_out)
    print("\n")
    pass

def exercise_12_format_string():
    """
    Exercise 8: Format variables using string.format() method
        Write a program to use the string.format() method to format
        the following three variables according to the expected output.

        Given:
            totalMoney = 1000
            quantity = 3
            price = 450
        Expected Output:
            I have 1000 dollars so I can buy 3 football for 450.00 dollars.
    """
    totalMoney = 1000
    quantity = 3
    price = 450
    n_t_t = 16384

    txt = "I have ${:,.0f} dollars so I can buy {:n} football(s) for ${:,.2f} dollars."
    print(txt.format(totalMoney, quantity, price))
    # print("\n")
    txt = "The number {:n} is {:X} in hexadecimal, {:o} in octal, and {:b} in binary."
    print(txt.format(n_t_t, n_t_t, n_t_t, n_t_t))

    pass

def exercises_03_04_display_hex_and_octal():
    """
    ----------------------------------------------------------------------------------
        Exercise 3. Convert decimal number to octal
        Practice Problem: Accept an integer from the user and display it as an octal number (Base 8).
        Exercise Purpose: Computers often use different numbering systems (Hexadecimal, Octal, Binary). This exercise demonstrates how to use “Format Specifiers” in strings to automatically convert values between number systems for display.
            Given Input: Decimal: 8
            Expected Output:
                The octal number of decimal number 8 is 10
    ----------------------------------------------------------------------------------
        Exercise 4. Binary representation
        Practice Problem: Accept an integer from the user and display its value in binary format (Base 2).
        Exercise Purpose: Computers process everything in binary. This exercise shows how to use Python’s built-in formatting to visualize how a decimal number is represented at the hardware level using only 0s and 1s.
        Given Input:
            Decimal Number: 45
        Expected Output:
            The binary representation of 45 is 101101
    ----------------------------------------------------------------------------------
    :return:
    :rtype:
    """
    print("\nDisplay decimal as octal")
    number = input("Enter a decimal number: ")
    incomplete = True
    while incomplete:
        try:
            #### verify user entered a valid float
            user_input_num = float(number)
            txt = "The octal of decimal number {:n} is {:o}."
            print(txt.format(user_input_num, int(number)))
            incomplete = False
        except ValueError:
            print("Invalid item. Please enter either an integer or a decimal number. Try again.")

    print("\nDisplay decimal as binary")
    number = input("Enter a decimal number: ")
    incomplete = True
    while incomplete:
        try:
            #### verify user entered a valid float
            user_input_num = float(number)
            txt = "The binary representation of number {:n} is {:b}."
            print(txt.format(user_input_num, int(number)))
            incomplete = False
        except ValueError:
            print("Invalid item. Please enter either an integer or a decimal number. Try again.")
    pass

def ex_06_hexadecimal_representation():
    """
    Exercise 6. Hexadecimal representation
        Practice Problem: Accept an integer and display its value in hexadecimal format (Base 16).
        Exercise Purpose: Hexadecimal is widely used in computing for memory addresses
            and color codes (e.g., #FFFFFF). This exercise teaches you how to bridge
            the gap between human-readable decimals and developer-centric hex values.
        Given Input:
            Decimal Number: 255
        Expected Output:
            The hexadecimal value is ff
    """
    print("\nDisplay integer as hexadecimal")
    number = input("Enter a whole number: ")
    incomplete = True
    while incomplete:
        try:
            #### verify user entered a valid float
            user_input_num = int(number)
            txt = "The hexadecimal representation of number {:n} is {:x}."
            print(txt.format(user_input_num, user_input_num))
            incomplete = False
        except ValueError:
            print("Invalid item. Please enter an integer. Try again.")
    pass


def ex_08_percentage_display():
    """
    Exercise 8. Percentage display
    Practice Problem: Ask the user for a numerator and a denominator.
        Calculate the percentage (numerator/denominator * 100) and
        display it with exactly two decimal places followed by a percent sign.
    Exercise Purpose: In this exercise, you will learn about string interpolation.
        You will practice combining math results with symbols like % and
        learn how to control the number of decimal places so your answers look neat.
    Given Input:
        Numerator: 22
        Denominator: 29
    Expected Output:
        The result is: 75.86%
    :return:
    :rtype:
    """

    incomplete = True
    number = input("Enter a whole number for the numerator: ")
    while incomplete:
        try:
            #### verify user entered a valid integer
            numerator = int(number)
            incomplete = False
        except ValueError:
            print("Invalid item. Please enter a whole number. Try again.")

    incomplete = True
    number = input("Enter a whole number for the denominator: ")
    while incomplete:
        try:
            #### verify user entered a valid integer
            denominator = int(number)
            incomplete = False
        except ValueError:
            print("Invalid item. Please enter a whole number. Try again.")

    result = (numerator / denominator)
    txt = "The result is: {:.2%}"
    print(txt.format(result))
    pass


def ex_09_display_right_aligned_output():
    """
    Practice Problem: Ask the user for a word and a number. Print the word
        right-aligned in a total field width of 20 characters, followed by the number.
    Exercise Purpose: Good design is important. When you create text-based
        reports, lining up columns makes them easier to read. In this exercise,
        you will learn how to use Alignment Flags to set aside space on the screen
        and move text to the left, right, or center.
    Given Input:
        Word: “Python”
        Number: 3.12
    Expected Output:
        Python 3.14

    References: https://stackoverflow.com/questions/20309255/how-to-pad-a-string-to-a-fixed-length-with-spaces
    :return:
    :rtype:
    """
    word = input("Enter a word: ")
    number = input("Enter a number: ")
    result = " ".join([word, number])
    txt = "{:>20}"
    print("--------------------")
    print(txt.format(result))

    pass

def ex_13_format_currency(dollar_amount):
    """
    Exercise 13. Currency formatting with commas
        Practice Problem: Display a large number as currency, including a dollar sign, commas for thousands, and two decimal places.
        Exercise Purpose: Financial applications require strict formatting. This exercise combines three concepts: prefixing, grouping (using commas), and precision to create a professional-grade money display.
        Given Input:
            Amount: 1250500.7
        Expected Output:
            Total Balance: $1,250,500.70
    :return:
    :rtype:
    """
    # Set the locale to the user's default
    locale.setlocale(locale.LC_ALL, '')
    # Format a number as a currency string
    print("-------------------------------------\nCurrency test \n-------------------------------------")
    currency_string = locale.currency(dollar_amount, grouping=True)
    print(currency_string)
    print("-------------------------------------")

    pass

def ex_15_tabular_output():
    """
    Exercise 15. Tabular output from lists
    Practice Problem: You have two lists: names = ["Alice", "Bob", "Charlie"]
        and scores = [85, 92, 78]. Print these as a table with aligned columns.
    Exercise Purpose: This exercise introduces “Parallel Iteration.”
        It teaches you how to step through two related lists simultaneously
        and format them to look like an organized database table.
    Given Input:
        names = ["Alice", "Bob", "Charlie"]
        scores = [85, 92, 78]
    Expected Output:
        Name       Score
        ----------------
        Alice      85
        Bob        92
        Charlie    78

    :return:
    :rtype:
    """
    s3 = "Name            Score"
    s4 = "--------------- ---------"
    print(s3)
    print(s4)

    names = ["Alice", "Bob", "Charlie"]
    scores = [85, 92, 78]
    for name, score in zip(names, scores):
        result = "{:<15}{:< 8}"
        print(result.format(name, score))

    # for i in range(len(names)):
    #     result = "{:<15}{:< 8}"
    #     print(result.format(names[i], scores[i]))
    pass

#####################################################################
#### Exercise 16
#####################################################################\
def ex_16_display_menu():
    print("============================================")
    print("1. Say Hello")
    print("2. Calculate Square")
    print("3. Exit")
    print("")
    return None

def ex_16_choice_02():
    incomplete = True
    while incomplete:
        try:
            number = int(input("Enter a number: "))
            result = number ** 2
            print(result)
            print("")
            incomplete = False
        except ValueError:
            print("Please enter a number")

    return None

def ex_16_interactive_menu():
    """
    Exercise 16. Interactive menu
    Practice Problem: Create a menu that offers three options:
        “1. Say Hello”,
        “2. Calculate Square”, and
        “3. Exit”.
        The program should perform the action based on the number the user types.
    Exercise Purpose: This is the foundation of “Command Line Interfaces” (CLI).
        It teaches you how to map user input to specific logic blocks
        using conditional statements, turning a linear script into an interactive application.
    Given Input:
            Choice: 2
            Number to square: 5
    Expected Output:
            Enter choice (1-3): 2
            Enter number to square: 5
            The square is: 25
    :return:
    :rtype:
    """
    exitNotSelected = True
    ex_16_display_menu()
    while exitNotSelected:
        choice = input("Enter choice (1-3): ")
        if choice not in ["1", "2", "3"]:
            print("Invalid Choice, please try again.")
            ex_16_display_menu()
            continue
        else:
            if choice == "3":
                exitNotSelected = False
                break
            if choice == "1":
                print("Hello")
            if choice == "2":
                ex_16_choice_02()
            ex_16_display_menu()
            continue
    print("Session complete.")
    pass
#####################################################################
#####################################################################
#####################################################################


def ex_17_login_test():
    """
    Exercise 17. Masked password input (getpass)
    Practice Problem: Write a script that asks a user for their username using
        standard input and their password using masked input
        (where the characters don’t appear on the screen).
    Exercise Purpose: Security is paramount. Using input() for passwords is a
        major vulnerability because the password remains visible in the terminal’s
        scrollback buffer. The getpass module is the standard way to handle sensitive
        credentials by suppressing local echo.
    Given Input:
        Username: admin
        Password: SecretPassword123 (invisible during typing)
    Expected Output:
        Enter Username: admin
        Password:
        Login successful for admin!
    :return:
    :rtype:
    """

    print("-------------------------------------")

    # pswd = pwinput.pwinput(prompt="Enter password: ", mask="*")
    getpass.getpass(prompt="Enter login password: ", stream=None)
    pass


def ex_18_read_file_store_content_in_list():
    """
    Exercise 18. Read a file and store its content in a list
    Practice Problem: Read an existing file test.txt and store every line as an individual element in a Python list.
    Exercise Purpose: It’s the first step in “Data Parsing”, taking raw text from a disk and converting
        it into a structured format (a list) that Python can easily sort, filter, or search.
    Given Input:
        A file test.txt with multiple lines.
    Expected Output:
        ['Line 1', 'Line', 'Line']

    :return:
    :rtype:
    """
    file_path = build_file_name("names.txt")
    with open(file_path, 'r') as file:
        lines_in_the_file = file.readlines()
    print(lines_in_the_file)
    pass

def ex_19_write_list_to_text_file():
    """
    Exercise 19. Write list of strings to a file
    Practice Problem: Take a list of favorite fruits and save each fruit
        onto a new line in a file named fruits.txt.
    Exercise Purpose: In data science or web dev, you often process data in memory (as a list)
        and then need to “persist” it (save it to a disk). This exercise teaches you how to export
        structured Python data into a permanent text format.
    Given Input:
        fruit_list = ["Apple", "Banana", "Cherry", "Date"]
    Expected Output:
        A file fruits.txt created with each fruit on its own line.

    :return:
    :rtype:
    """
    fruit_list = ["Apple", "Banana", "Cherry", "Date"]
    file_path = build_file_name("fruits.txt")
    with open(file_path, 'w') as file:
        for fruit in fruit_list:
            file.write(fruit)
            file.write("\n")
    pass

def ex_20_find_number_of_lines():
    """
    Practice Problem: Write a program that opens an existing text file
        and calculates exactly how many lines of text it contains.
    Exercise Purpose: This is a fundamental “Data Auditing” task. Before you process a log file
        or a dataset, you need to know its size. This exercise teaches you how to iterate
        through a file object efficiently.
    Given Input:
        A file sample.txt with 12 lines of text.


    :return:
    :rtype:
    """

    file_path = build_file_name("names.txt")
    with open(file_path, 'r') as file:
        lines_in_the_file = file.readlines()
    print(f"{file_path} contains {lines_in_the_file.__len__()} lines of text.")
    pass

def exercise_21_read_specific_lines_from_file(items_to_keep):
    """
    Exercise 21. Read line number 4 from a file
    Practice Problem: Open a file and display only the fourth line of the content.
    Exercise Purpose: Sometimes files are massive (gigabytes in size), and you only
        need a specific snippet. This exercise reinforces the idea that file lines
        can be treated like a list, allowing for direct, indexed access.
    Given Input: A file test.txt containing:
        Line 1
        Line 2
        Line 3
        Line 4
        Line 5
    Expected Output:
        Line 4
    :return:
    :rtype:
    """
    file_path = build_file_name("test.txt")
    with open(file_path, 'r') as file:
        lines_in_the_file = file.readlines()

    #### trim the newline characters at the end of each line
    for i in range(lines_in_the_file.__len__() - 1):
        lines_in_the_file[i] = lines_in_the_file[i].strip("\n")
    # for item in lines_in_the_file:
    #     item = item.strip("\n")
    #### filter out line 5 (index = 4)
    #### pass the list of items to keep into the function
    #### create the output list
    lines_to_write = [x for i, x in enumerate(lines_in_the_file) if i in items_to_keep]
    print(lines_to_write)
    pass

def exercise_22_check_empty_file():
    """
    Exercise 22. Check if file is empty
    Practice Problem: Write a script that checks a file’s metadata. If the file size is 0 bytes
        , print “File is empty”; otherwise, print the size in bytes.
    Exercise Purpose: Sometimes a file exists but contains no data (common in failed
        downloads or interrupted logs). This exercise introduces the os module
        and “system metadata”—information about a file rather than the content inside it.
    Given Input:
        An empty file named empty_log.txt.
    Expected Output:
        Checking empty_log.txt...
        Status: File is empty.
    """
    file_path = build_file_name("test.txt")
    myFile = Path(file_path)
    size = myFile.stat().st_size
    status = "not"
    if size == 0:
        status = ""
    message = f"{myFile.name} is {status} empty."
    print(message)

    file_path = build_file_name("empty_log.txt")
    myFile = Path(file_path)
    size = myFile.stat().st_size
    status = "not"
    if size == 0:
        status = ""
    message = f"{myFile.name} is {status} empty."
    print(message)


    pass


def exercise_10_center_aligned_text():
    """
    Exercise 10. Center-aligned text
    Practice Problem: Display a string centered within a 40-character field,
        using hyphens (-) as the padding character.
    Exercise Purpose: Centering text is a common way to make headers or dividers
        in console reports. In this exercise, you will learn about the “Fill”
        and “Align” parts of f-string formatting.
    Given Input: Text:
        “REPORT SUMMARY”
    Expected Output:
        -------------REPORT SUMMARY-------------

        # Center (^) with hyphen (-) as fill in a width of 40
            formatted_title = f"{title:-^40}"
            print(formatted_title)
    """
    # Prompt the user for inout
    DEFAULT_LENGTH = 40
    OVERFLOW_LENGTH = 10
    message = input("Enter some text: ")
    if message.__len__() < DEFAULT_LENGTH - 2:
        pad_length = (DEFAULT_LENGTH - len(message)) / 2
    else:
        pad_length = OVERFLOW_LENGTH
    # ruler = "-"*40
    # print(ruler)
    ruler = "         1111111111222222222233333333334\n1234567890123456789012345678901234567890"
    print(ruler)
    filler = "-"*int(pad_length)
    result = f"{filler}{message}{filler}"
    print(result)
    # ruler = "-"*50
    # print(ruler)

    pass


def exercise_11_pad_with_zeroes():
    """
    Exercise 11: Padding with zeros
    Practice Problem: Ask the user for a number. Print this number padded with
        leading zeros so the total width is exactly 5 digits.
    Exercise Purpose: This method is important when you need to create
        standardized IDs, serial numbers, or digital clock displays, such as
        showing “09” instead of “9” minutes. It shows you how to set a
        specific number format no matter the original input size.
    Given Input:
        Number: 42
    Expected Output:
        00042
    """
    # Set the locale to the user's default
    number = input("Enter a number between 0 and 9999: ")
    # > results in leading zeroes, < results in trailing zeroes
    result = "With leading zeroes.... {:>025}"
    print(result.format(number))

    result = "With trailing zeroes... {:<025}"
    print(result.format(number))
    # Pad with leading zeroes to 5 places
    print("-------------------------------------")
    pass

def convert_string_to_blocks(source_data: string, block_size: int) -> list:
    """

    :param source_data:
    :type source_data:
    :param block_size:
    :type block_size:
    :return:
    :rtype:
    """
    # Set up
    results_list = []
    incomplete = True
    eof = False
    end_point = len(source_data)
    start = 0
    pointer_index = 0
    # begin the loop
    while incomplete:
        # determine how many bytes to take and where to skip to
        s = start + (block_size * pointer_index)
        e = s + block_size
        # compare the end point of the next chunk to the end of the source
        # if the next end point is past the end of the source
        #   move the input back
        if e > end_point:
            e = end_point
            eof = True

        # take a chunk out of the input
        chunk = source_data[s:e]
        # append the chunk to the results list
        results_list.append(chunk)

        if eof:
            #   if eof the work is complete... exit the loop
            incomplete = False
        else:
            # increment the counter
            pointer_index += 1
            
    # return the results list to the caller
    return results_list


def generate_random_text(size):
    """
    Generate a random block of text with the given size.
    Characters include letters, digits, punctuation, and spaces.
    """
    if not isinstance(size, int) or size <= 0:
        raise ValueError("Size must be a positive integer.")

    # Define the character set: letters, digits, punctuation, and space
    # charset = string.ascii_letters + string.digits + string.punctuation + " "
    charset = string.ascii_letters + string.digits + "_"

    # Generate random characters securely
    # return ''.join(secrets.choice(charset) for _ in range(size))
    return ''.join(random.choice(charset) for _ in range(size)).upper()

def create_text_block():
    try:
        # Get user input
        size_input = input("Enter the size of the random text: ").strip()

        # Validate and convert to integer
        if not size_input.isdigit():
            print("Error: Please enter a positive integer.")
            return

        size = int(size_input)
        if size <= 0:
            print("Error: Size must be greater than zero.")
            return

        # Get user input
        block_size_input = input("Enter the block size for formatting text: ").strip()
        # Validate and convert to integer
        if not block_size_input.isdigit():
            print("Error: Please enter a positive integer.")
            return

        block_size = int(block_size_input)
        if block_size <= 0:
            print("Error: Block size must be greater than zero.")
            return
        
        # Generate and display the random text
        random_text = generate_random_text(size)
        results = convert_string_to_blocks(random_text, block_size)
        print("\nGenerated Random Text:\n")
        print(random_text)
        print("\nFormatted Results: \n")
        for item in results:
            print(item)

        print("\nEnd of routine.")

    except Exception as e:
        print(f"An error occurred: {e}")

    return results


def exercise_23_delete_file(src_dir):
    """
    Exercise 23. Delete a specific file
    Practice Problem: Write a program that asks the user for a filename
        and deletes it from the folder. Caution: This operation is permanent.
    Exercise Purpose: File system maintenance. This exercise shows you how Python
        can perform high-level administrative tasks. It also emphasizes the importance
        of “High Risk” operations and the need to always verify the user’s intent.
    Given Input: Filename to delete: old_data.csv
    Expected Output:
        Are you sure you want to delete 'old_data.csv'? (y/n): y
        File 'old_data.csv' has been deleted.
    """

    # Create a file to test the delete functionality
    #### write the data to an output file
    file_payload = create_text_block()

    #### first build the name of the file
    file_path = build_file_name(src_dir, "delete_test.txt")
    p = Path(file_path)
    #### open the file and write the data
    with open(p, 'w') as file_out:
        for line in file_payload:
            file_out.write(line)
            file_out.write("\n")
    # Prompt the user to delete the file
    message = f"Are you sure you want to delete '{p}'? (y/n):"
    user_response = input(message).strip()
    if user_response.upper() == "y".upper():
        p.unlink()

    # print a message
    if p.exists():
        message = f"File {p} was not deleted."
    else:
        message = f"File {p} was deleted."
    print(message)


    print("exercise_23_delete_file complete.")
    pass