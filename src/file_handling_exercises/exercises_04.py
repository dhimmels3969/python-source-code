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
    """
    print("Exercise 31: Read and Write Binary Image File")
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
    print("Exercise 34: Split Large File into Smaller 10-Line Files")
    pass







