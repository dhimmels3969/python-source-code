
from src.common_library import helper_functions as hf
from pathlib import Path
import random
import string

#
# https://pynative.com/python-input-and-output-exercise/
# Exercises 21 - 237
#

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



#########################################################################################
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



#########################################################################################
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



#########################################################################################
def exercise_21_read_specific_lines_from_file(root_dir, items_to_keep):
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
    print("Exercise 21. Read a file and display only the fourth line of the content.")
    # file_path = build_file_name("test.txt")
    file_path = hf.build_file_name(root_dir, "data", "test.txt")
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



#########################################################################################
def exercise_22_check_empty_file(root_dir):
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
    print("Exercise 22. Check if file is empty.")
    file_path = hf.build_file_name(root_dir, "data", "test.txt")
    myFile = Path(file_path)
    size = myFile.stat().st_size
    status = "not"
    if size == 0:
        status = ""
    message = f"{myFile.name} is {status} empty."
    print(message)

    file_path = hf.build_file_name(root_dir, "data", "empty_log.txt")
    myFile = Path(file_path)
    size = myFile.stat().st_size
    status = "not"
    if size == 0:
        status = ""
    message = f"{myFile.name} is {status} empty."
    print(message)
    pass



#########################################################################################
def exercise_22_check_empty_zilch_file(root_dir):
    """
    See if we can reference a sub-folder while building a file name
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
    print("Exercise 22.1:   Check if file is empty.")

    file_path = hf.build_file_name(root_dir, r"data\input_output_exercises", "empty_zilch_log.txt")
    myFile = Path(file_path)
    size = myFile.stat().st_size
    status = "not"
    if size == 0:
        status = ""
    message = f"{myFile.name} is {status} empty."
    print(message)

    file_path = hf.build_file_name(root_dir, r"data\input_output_exercises", "random_quotes.txt")
    myFile = Path(file_path)
    size = myFile.stat().st_size
    status = "not"
    if size == 0:
        status = ""
    message = f"{myFile.name} is {status} empty. Size is {size} bytes."
    print(message)
    print()
    pass




#########################################################################################
def exercise_23_delete_file(root_dir):
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
    file_path = hf.build_file_name(root_dir, "data", "delete_test.txt")
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