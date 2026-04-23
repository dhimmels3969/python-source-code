from src.common_library import helper_functions as hf


#
# https://pynative.com/python-input-and-output-exercise/
# Exercises 11 - 20
#


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
    print("Exercise 11. Padding with zeros")
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



#########################################################################################
def ex_18_read_file_store_content_in_list(root_dir):
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
    print("Exercise 18. Read a file and store its content in a list")
    # file_path = build_file_name("names.txt")
    file_path = hf.build_file_name(root_dir, "data",  "names.txt")
    with open(file_path, 'r') as file:
        lines_in_the_file = file.readlines()
    print(lines_in_the_file)
    pass



#########################################################################################
def ex_19_write_list_to_text_file(root_dir):
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
    # file_path = build_file_name("fruits.txt")
    file_path = hf.build_file_name(root_dir, "data",  "names.txt")
    with open(file_path, 'w') as file:
        for fruit in fruit_list:
            file.write(fruit)
            file.write("\n")
    pass



#########################################################################################
def ex_20_find_number_of_lines(root_dir):
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

    # file_path = build_file_name("names.txt")
    file_path = hf.build_file_name(root_dir, "data", "names.txt")
    with open(file_path, 'r') as file:
        lines_in_the_file = file.readlines()
    print(f"{file_path} contains {lines_in_the_file.__len__()} lines of text.")
    pass
