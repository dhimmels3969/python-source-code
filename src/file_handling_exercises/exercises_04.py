from src.common_library import helper_functions as hf
from pathlib import Path
import string
import shutil
import os
import re

#
# Exercises found at web page https://pynative.com/python-file-handling-exercises/
# Exercises 31 through 34
#



##############################################################################
def exercise_31_read_write_binary_image_file(root_dir):
    """
    Exercise 31: Read and Write Binary Image File
    Problem Statement: Write a Python program to read a binary
        image file and write its contents to a new file,
        producing an exact duplicate of the original image.
    Purpose: This exercise deepens your understanding of binary
        file I/O beyond simple text files, illustrating how Python
        can handle any file format – images, audio, video, or
        executables – as a stream of raw bytes.
    Given Input:
        An existing image file photo.jpg on disk.
    Expected Output:
        A new file photo_copy.jpg created on disk, confirmed by
        printing Image copied to photo_copy.jpg
    Hints:
        Open the source image in binary read mode using "rb"
            and the destination in binary write mode using "wb".
        Read the full content with .read() and write
            it with .write().
        For large images, consider reading in chunks (e.g., 4096 bytes at a time)
            inside a while loop to avoid loading the entire file
            into memory at once.
    """
    print("Exercise 31: Read and Write Binary Image File")
    block_size = 4096
    file_path = hf.build_file_name(root_dir
                        , "data/file_handling_exercises"
                        , "mustard-seed-acre.jpg")
    file_path_out = hf.build_file_name(root_dir
                        , "data/file_handling_exercises/dummy"
                        , "mustard-seed-acre-copy.jpg")
    with open(file_path, 'rb') as file, open(file_path_out, 'wb') as file_out:
        while True:
            content = file.read(block_size)
            if not content:
                break
            file_out.write(content)

    # check out the file size for the original and the copy
    print(f"  Original ({Path(file_path).name}): {os.path.getsize(file_path)} bytes")
    print(f"      Copy ({Path(file_path_out).name}): {os.path.getsize(file_path_out)} bytes")
    pass


##############################################################################
def exercise_32_extract_unique_words(root_dir):
    """
    Exercise 32: Extract and Sort Unique Words from File
    Problem Statement: Write a Python program to read a text file,
        extract all unique words, sort them alphabetically,
        and print the result.
    Purpose: This exercise practises file reading, string
        normalization, set operations for deduplication, and
        sorting – key techniques in vocabulary building, text
        indexing, and content analysis tasks.
    Given Input:
        A file paragraph.txt containing: the cat sat on the mat the cat
    Expected Output:
        cat
        mat
        on
        sat
        the
    """
    print("Exercise 32: Extract and Sort Unique Words from File")
    word_list = []
    # unique_list = []
    input_file = hf.build_file_name(root_dir, "data/file_handling_exercises/", "paragraph.txt")
    with open(input_file, "r") as infile:
        lines = infile.readlines()

    for line in lines:
        word_list.extend(line.translate(str.maketrans("", "", string.punctuation)).lower().split())

    # convert the list to a set to remove duplicate items.
    unique_list = sorted(set(word_list))

    for word in unique_list:
        print(f"  {word}")
    pass


##############################################################################
def exercise_33_filter_log_file(root_dir):
    """
    Exercise 33: Filter Log File Lines Containing ERROR Keyword
    Problem Statement: Write a Python program to read a log file
        line by line and print (or save) only the lines that
        contain the keyword ERROR.
    Purpose: This exercise simulates a real-world log analysis
        task, practising line-by-line file reading, keyword
        filtering, and conditional output – skills central to
        system monitoring, debugging tools, and DevOps automation.
    Given Input:
        A file app.log with mixed log levels, where some lines contain ERROR.
    Expected Output:
        2024-01-01 10:02:05 ERROR Disk quota exceeded
        2024-01-01 10:07:45 ERROR Connection timeout
    """
    print("Exercise 33: Filter Log File Lines Containing ERROR Keyword")
    keyword = "ERROR"
    input_file = hf.build_file_name(root_dir, "data/file_handling_exercises/", "error.log")
    with open(input_file, "r") as infile:
        lines = infile.readlines()

    list_of_errors = [item for item in lines if keyword in item]
    for line in list_of_errors:
        print(f"  {line.strip()}")
    pass


##############################################################################
def exercise_34_split_large_file(root_dir):
    """
    Exercise 34: Split Large File into Smaller 10-Line Files
    Problem Statement: Write a Python program to read a large
        text file and split it into smaller files, each
        containing at most 10 lines, saving them as
        part_1.txt, part_2.txt, and so on.
    Purpose: This exercise practises chunked file processing
        and dynamic file creation – techniques used in data
        partitioning, batch upload preparation, and breaking
        large datasets into manageable pieces for
        parallel processing.
    Given Input:
        A file large_file.txt containing 25 lines of text.
    Expected Output:
        Created: part_1.txt (10 lines)
        Created: part_2.txt (10 lines)
        Created: part_3.txt (5 lines)
    """
    # def write_results_to_file(file_number, content):
    #     file_name = f"part_{file_number}.txt"
    #     file_path = hf.build_file_name(root_dir, "data/file_handling_exercises/dummy", file_name)
    #     with open(file_path, "w") as outfile:
    #         for line in content:
    #             outfile.write(line)
    #
    #     message = f"Created: {Path(file_path).name} ({len(content)} lines)"
    #     return message

    print("Exercise 34: Split Large File into Smaller 10-Line Files")
    # read in the file and load into a list
    block_size = 10

    input_files = hf.build_file_name(root_dir, "data/file_handling_exercises/", "lines.txt")
    with open(input_files, "r") as infile:
        lines = infile.readlines()
    # break the list into blocks and write each block to a separate file
    total_lines = len(lines)

    for i, start in enumerate(range(0, total_lines, block_size), start=1):
        block = lines[start:start + block_size]
        file_name = f"part_{i}.txt"
        output_filename = hf.build_file_name(root_dir, "data/file_handling_exercises/dummy", file_name)
        with open(output_filename, "w") as out:
            out.writelines(block)
        print(f"  Created: {output_filename} ({len(block)} lines)")

    # index = 0
    # results = []
    # process_complete = False
    # # Every time we read a range from the lines list it deletes lines in the file.
    # # Assign the list to a different list to see if we can preserve the content in the input file.
    # payload = lines
    # while True:
    #     lower_limit = index * block_size
    #     upper_limit = (index + 1) * block_size
    #     if upper_limit > len(lines):
    #         upper_limit = len(lines)
    #         process_complete = True
    #     block = lines[lower_limit:upper_limit]
    #     results.append(block)
    #     if process_complete:
    #         break
    #     else:
    #         index += 1
    #
    # final_results = list(enumerate(results, start = 1))
    # for index, result in final_results:
    #     message = write_results_to_file(index, result)
    #     print(f"  {message}")
    pass







