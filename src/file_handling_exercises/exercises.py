from src.common_library import helper_functions as hf
import os
import datetime
import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
#
# Exercises found at web page https://pynative.com/python-file-handling-exercises/
# Exercises 1 through 10
#


##############################################################################
def file_handling_setup_dummy_directory(root_dir):
    # build the directory path (../data/file_handling_exercises/dummy)
    subfolder = "data/file_handling_exercises/dummy"
    current_dir = root_dir

    # Construct the path to the JSON file in the /data directory
    json_path = os.path.join(current_dir, subfolder)
    # Normalize the path (optional but recommended)
    json_path = os.path.normpath(json_path)
    # verify it exists by calling helper_functions.mkdir
    dummy_directory_exists = hf.mkdir(json_path)
    # print(f"  dummy_directory_exists: {dummy_directory_exists}")

    #########################################################################
    # 2026-06-14 check if notes_active.txt is found in the dummy directory
    # if not found copy it notes.txt in the file_handing_exercises folder
    #########################################################################
    source_file = hf.build_file_name(root_dir
                        , "data/file_handling_exercises"
                        , "notes.txt")
    target_file = hf.build_file_name(root_dir
                        , "data/file_handling_exercises/dummy"
                        , "notes_active.txt")
    if not hf.file_exists(target_file):
        with open(source_file, 'rb') as file:
            content = file.read()

        with open(target_file, 'wb') as file_out:
            file_out.write(content)

    pass



##############################################################################
def exercise_01_write_user_name_to_file(root_dir):
    """
    Exercise 1: Write UserName to File
    Problem Statement: Write a Python program that accepts a user’s
        name as input and writes it to a file called user.txt.
    Purpose: This exercise introduces you to writing data to a file
        using Python’s built-in open() function with write mode. It
        covers how user input can be persisted to disk, a
        fundamental concept in data storage and logging.
    Given Input:
        User enters their name at runtime, e.g. Alice
    Expected Output:
        A file named user.txt is created containing the entered name, e.g. Alice
    """
    logger.info("Exercise 1: Write User Name to File")
    #### get a user name... not sure how we'll do this when testing...
    while True:
        user_name = input("Enter your user name: ")
        if user_name.strip() > '':
            break
        else:
            logger.info("User name cannot be blank... please try again.")

    #### build the name of the output file
    file_path = hf.build_file_name(root_dir, "data/file_handling_exercises", "user.txt")
    #### open the file and write the data
    with open(file_path, 'w') as file_out:
        file_out.writelines(user_name)
    pass


##############################################################################
def exercise_02_read_and_print_file(root_dir):
    """
    Exercise 2: Read and Print Complete File
    Problem Statement: Write a Python program that opens a file
        called data.txt and prints its entire contents to the console.
    Purpose: This exercise teaches you how to open an existing file
        in read mode and retrieve all of its contents at once using
        read(). It is a foundational skill for processing configuration
        files, logs, and data files.
    Given Input:
        A file named data.txt containing: Hello, World!
    Expected Output:
        Hello, World!
    """
    logger.info("Exercise 2: Read and Print Complete File")
    file_path = hf.build_file_name(root_dir, "data/file_handling_exercises", "data.txt")
    with open(file_path, 'r') as file:
        lines_in_the_file = file.readlines()
    for line in lines_in_the_file:
        logger.info(f"    {line.strip()}")
    pass


##############################################################################
def exercise_03_read_file_line_by_line(root_dir):
    """
    Exercise 3: Read File Line by Line Using Loop
    Problem Statement: Write a Python program that reads a file
        called lines.txt and prints each line one at a time
        using a loop.
    Purpose: This exercise shows how to iterate over a file object
        directly, which is memory-efficient for large files. It is
        a common pattern used when processing log files, CSVs,
        or any line-structured text data.
    Given Input: A file named lines.txt containing:
        Line 1
        Line 2
        Line 3
    Expected Output:
        Line 1
        Line 2
        Line 3
    """
    logger.info("Exercise 3: Read File Line by Line Using Loop")
    file_path = hf.build_file_name(root_dir, "data/file_handling_exercises", "lines_ex_03.txt")
    with open(file_path, 'r') as file:
        lines_in_the_file = file.readlines()
    for line in lines_in_the_file:
        logger.info(f"    {line.strip()}")
    pass


##############################################################################
def exercise_04_read_file_into_list(root_dir):
    """
    Exercise 4: Read File Lines into a List
    Problem Statement: Write a Python program that reads all lines from a
        file called items.txt into a list and prints the list.
    Purpose: This exercise demonstrates how to load structured line-based
        file data into a Python list for further processing. This pattern
        is widely used when reading configuration entries, word lists,
        or simple datasets from files.
    Given Input: A file named items.txt containing:
        apple
        banana
        cherry
    Expected Output:
        ['apple\n', 'banana\n', 'cherry']
    """
    logger.info("Exercise 4: Read File Lines into a List")
    results = []
    file_path = hf.build_file_name(root_dir, "data/file_handling_exercises", "items.txt")
    with open(file_path, 'r') as file:
        lines_in_the_file = file.readlines()
    for line in lines_in_the_file:
        results.append(line)
    logger.info(f"    {results}")
    pass


##############################################################################
def exercise_05_append_data_to_file(root_dir):
    """
    Exercise 5: Append New Sentence to Existing File
    Problem Statement: Write a Python program that appends the sentence
        This is a new line. to an existing file called notes.txt
        without overwriting its current content.
    Purpose: This exercise teaches the difference between write mode
        and append mode. Append mode is essential when you need to add
        entries to a log file, journal, or any growing data file
        without destroying previously stored content.
    Given Input:
        A file named notes.txt already containing: Original content.
    Expected Output: File now contains:
        Original content.
        This is a new line.
    """
    logger.info("Exercise 5: Append New Sentence to Existing File")
    line_to_append = f"\n[{datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')}] This is a new line."

    file_path = hf.build_file_name(root_dir
                    , "data/file_handling_exercises/dummy"
                    , "notes_active.txt")
    #### open the file and write the data
    #### file writing modes: 'w' write over existing contents,
    #### 'a' append data to existing data
    with open(file_path, 'a') as file_out:
        file_out.writelines(line_to_append)
    pass


##############################################################################
def exercise_06_clear_file_content(root_dir):
    """
    Exercise 6: Clear All File Content
    Problem Statement: Write a Python program that clears all content
        from an existing file called temp.txt, leaving it as
        an empty file.
    Purpose: This exercise illustrates how opening a file in write
        mode truncates it immediately. Understanding this behavior
        is important to avoid accidental data loss and also useful
        when you intentionally need to reset a file, such as
        clearing a cache or resetting a log.
    Given Input:
        A file named temp.txt containing some existing text, e.g. Some old data.
    Expected Output:
        temp.txt exists but is completely empty (0 bytes).
    """
    def reload_temp_dot_txt():
        """
        write the data from lorem_ipsum.txt to temp.txt.
        """
        input_path = hf.build_file_name(root_dir, "data/file_handling_exercises", "lorem_ipsum.txt")
        output_path = hf.build_file_name(root_dir, "data/file_handling_exercises", "temp.txt")
        input_data = []
        with open(input_path, 'r') as file_in:
            for line in file_in:
                input_data.append(line)
        with open(output_path, 'w') as file_out:
            file_out.writelines(input_data)
        logger.info(f"    temp.txt reloaded")
        pass

    logger.info("Exercise 6: Clear All File Content")
    reload_temp_dot_txt()
    file_path = hf.build_file_name(root_dir, "data/file_handling_exercises", "temp.txt")
    file_size_bytes = os.path.getsize(file_path)
    logger.info(f"    File Size Before: {file_size_bytes} Bytes")
    #### open the file and write the data
    #### file writing modes: 'w' write over existing contents,
    #### 'a' append data to existing data
    with open(file_path, 'w') as file_out:
        pass
    file_size_bytes = os.path.getsize(file_path)
    logger.info(f"    File Size After: {file_size_bytes} Bytes")

    pass


##############################################################################
def exercise_07_write_text_to_new_file(root_dir):
    """
    Exercise 7: Write Text to New File
    Problem Statement: Write a Python program that creates a new file
        called output.txt and writes three lines of text to it.
    Purpose: This exercise reinforces writing multiple lines to a
        file and understanding how newline characters work in file
        output. It is a practical skill used in generating reports,
        saving results, and creating data export files
        programmatically.
    Given Input:
        No external input. The three lines to write are predefined in the program.
    Expected Output: A file named output.txt containing:
        First line
        Second line
        Third line
    """
    logger.info("Exercise 7: Write Text to New File")
    lines = ["First line", "Second line", "Third line"]
    file_path = hf.build_file_name(root_dir, "data/file_handling_exercises", "output.txt")
    with open(file_path, 'w') as file_out:
        line_count = 1
        for line in lines:
            file_out.write(line)
            # write a new line after every line except the last one in the list
            if line_count < len(lines):
                file_out.write("\n")
                line_count += 1
    pass


##############################################################################
def exercise_08_check_if_file_exists(root_dir):
    """
    Exercise 8: Check If File Exists
    Problem Statement: Write a Python program that checks whether a
        file called data.txt exists in the current directory and
        prints an appropriate message based on the result.
    Purpose: This exercise introduces the os.path module (or the
        modern pathlib alternative) for checking file existence
        before performing operations on it. This is a defensive
        programming practice that prevents crashes caused by
        attempting to open files that do not exist.
    Given Input:
        The filename data.txt is hardcoded. The file
        may or may not be present.
    Expected Output:
        File exists. if the file is present,
        or File does not exist. if it is not.
    """
    def display_search_results(file_to_find):
        if hf.file_exists(file_to_find):
            logger.info(f"    {file_to_find} - File Exists")
        else:
            logger.info(f"    {file_to_find} - File Does Not Exist")
        pass

    logger.info("Exercise 8: Check If File Exists")
    files_to_find = [
        hf.build_file_name(root_dir, "data/file_handling_exercises", "data.txt"),
        hf.build_file_name(root_dir, "data/file_handling_exercises", "data2.txt")
        ]
    for file in files_to_find:
        display_search_results(file)
    pass


##############################################################################
def exercise_09_handle_missing_file(root_dir):
    """
    Exercise 9: Handle Missing File with Try-Except
    Problem Statement: Write a Python program that attempts to open a
        file called missing.txt and gracefully handles the case where
        the file does not exist using a try-except block.
    Purpose: This exercise teaches you how to handle file-related
        exceptions in Python. Rather than letting your program crash
        with an unhandled error, you learn to anticipate failure
        conditions and respond with a meaningful message. This is
        essential for writing robust, production-ready
        file-handling code.
    Given Input:
        The filename missing.txt is hardcoded. The file does not
        exist in the current directory.
    Expected Output:
        Error: The file was not found.
    """
    logger.info("Exercise 9: Handle Missing File with Try-Except")
    try:
        input_path = hf.build_file_name(root_dir, "data/file_handling_exercises", "missing.txt")
        with open(input_path, 'r') as file_in:
            pass
    except FileNotFoundError as error:
        logger.error("    Error: The file was not found.")
    except Exception as error:
        logger.error(f"  {error}")
    pass


##############################################################################
def exercise_10_count_lines_in_file(root_dir):
    """
    Exercise 10: Count Total Lines in File
    Problem Statement: Write a Python program that opens a file
        called data.txt and counts the total number of
        lines it contains.
    Purpose: This exercise practices reading a file and applying
        counting logic to its contents. Line counting is a common
        task in log analysis, data validation, and text processing
        pipelines where you need to know the size or shape of
        a file before processing it.
    Given Input: A file named data.txt containing:
        Hello
        World
        Python
        File Handling
    Expected Output:
        Total lines: 4
    """
    logger.info("Exercise 10: Count Total Lines in File")
    input_path = hf.build_file_name(root_dir, "data/file_handling_exercises", "data.txt")
    with open(input_path, 'r') as file_in:
        results = file_in.readlines()
    logger.info(f"    Total Lines: {len(results)}")
    pass




