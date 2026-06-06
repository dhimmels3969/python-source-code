#
# Exercises found at web page https://pynative.com/python-file-handling-exercises/
# Exercises 21 through 30
#



##############################################################################
def exercise_21_convert_uppercase_and_lowercase():
    """
    Exercise 21: Convert Uppercase to Lowercase and Vice Versa
    Problem Statement: Write a Python program to read a text file
        and swap the case of every letter – uppercase letters
        become lowercase and lowercase letters become uppercase –
        then save the result to a new file.
    Purpose: This exercise practises string transformation
        methods and file read-write workflows, reinforcing
        how to apply character-level operations across entire
        file content.
    Given Input:
        A file input.txt containing: Hello World
    Expected Output:
        A new file swapped.txt containing: hELLO wORLD
    """
    print("Exercise 21: Convert Uppercase to Lowercase and Vice Versa")
    pass


##############################################################################
def exercise_22_find_replace():
    """
    Exercise 22: Find and Replace a Word Throughout File
    Problem Statement: Write a Python program to read a text file,
        replace every occurrence of a specified word with a new
        word, and save the updated content back to the file.
    Purpose: This exercise demonstrates a practical file update
        pattern – reading, modifying in memory, and writing back –
        used in configuration management, template engines, and
        automated text editing tools.
    Given Input:
        A file story.txt containing I love Java. Java is great.,
        with the goal of replacing Java with Python.
    Expected Output:
        The file story.txt updated to: I love Python. Python is great.
    """
    print("Exercise 22: Find and Replace a Word Throughout File")
    pass


##############################################################################
def exercise_23_get_file_size_kilobytes():
    """
    Exercise 23: Get File Size in Kilobytes
    Problem Statement: Write a Python program to find and
        display the size of a given file in kilobytes (KB).
    Purpose: This exercise introduces the os module for file system
        perations and practises unit conversion – skills used in
        file management utilities, upload validators, and storage
        monitoring tools.
    Given Input:
        A file data.txt with a size of 2048 bytes.
    Expected Output:
        File size: 2.0 KB
    """
    print("Exercise 23: Get File Size in Kilobytes")
    pass


##############################################################################
def exercise_24_copy_file_using_binary_mode():
    """
    Exercise 24: Copy File Using Binary Mode
    Problem Statement: Write a Python program to copy the contents of
        one file to another using binary mode, so that the program
        works correctly for all file types including images, PDFs,
        and executables.
    Purpose: This exercise introduces binary file I/O, which is
        essential for handling non-text files. It reinforces the
        read-then-write pattern while highlighting the difference
        between text mode and binary mode in Python.
    Given Input:
        A source file source.txt (or any file type) to be
        copied to destination.txt.
    Expected Output:
        A new file destination.txt created with identical content to
        source.txt, confirmed by printing File copied successfully.
    """
    print("Exercise 24: Copy File Using Binary Mode")
    pass


##############################################################################
def exercise_25_rename_single_file():
    """
    Exercise 25: Rename a Single File
    Problem Statement: Write a Python program to rename a
        single file on disk using the os module.
    Purpose: This exercise introduces the os.rename() function
        for file system manipulation – a fundamental skill
        used in file management scripts, automated batch
        processors, and data pipeline utilities.
    Given Input:
        An existing file named old_name.txt on disk.
    Expected Output:
        File renamed successfully.
    """
    print("Exercise 25: Rename a Single File")
    pass


##############################################################################
def exercise_26_rename_multiple_files():
    """
    Exercise 26: Rename Multiple Files with Prefix
    Problem Statement: Write a Python program to rename all .txt files
        in a directory by adding a specified prefix to each filename.
    Purpose: This exercise combines directory listing, string
        manipulation, and file renaming in a loop – a pattern widely
        used in bulk file organisation, dataset preparation, and
        automated archiving workflows.
    Given Input:
        A directory containing notes.txt and data.txt, with the prefix 2024_.
    Expected Output:
        Renamed: notes.txt -> 2024_notes.txt
        Renamed: data.txt -> 2024_data.txt
    """
    print("Exercise 26: Rename Multiple Files with Prefix")
    pass


##############################################################################
def exercise_27_delete_a_file():
    """
    Exercise 27: Delete a File from Disk
    Problem Statement: Write a Python program to delete a specified
        file from disk, with a check to confirm the file exists
        before attempting deletion.
    Purpose: This exercise introduces safe file deletion practices
        using the os module – an important skill for cleanup scripts,
        temporary file management, and automated maintenance tools.
    Given Input:
        An existing file named temp.txt on disk.
    Expected Output:
        temp.txt has been deleted.
    """
    print("Exercise 27: Delete a File from Disk")
    pass


##############################################################################
def exercise_28_merge_multiple_files():
    """
    Exercise 28: Merge Two Files into One
    Problem Statement: Write a Python program to read the contents
        of two separate text files and write their combined content
        into a single new file.
    Purpose: This exercise practises reading from multiple sources
        and writing to a single destination – a pattern used in
        report generation, log aggregation, and document
        assembly pipelines.
    Given Input:
        Two files – file1.txt containing Hello from file 1.
        and file2.txt containing Hello from file 2.
    Expected Output:
        A new file merged.txt containing both lines,
        confirmed by printing Files merged into merged.txt
    """
    print("Exercise 28: Merge Two Files into One")
    pass


##############################################################################
def exercise_29_reverse_line_order():
    """
    Exercise 29: Reverse Line Order and Save to New File
    Problem Statement: Write a Python program to read all lines
        from a text file, reverse their order, and save the
        result to a new file.
    Purpose: This exercise practises reading lines into a list,
        applying list reversal, and writing back to a file –
        skills applicable in log analysis, data reordering,
        and text transformation utilities.
    Given Input:
        A file original.txt with three lines: Line 1, Line 2, Line 3.
    Expected Output:
        Line 3
        Line 2
        Line 1
    """
    print("Exercise 29: Reverse Line Order and Save to New File")
    pass


##############################################################################
def exercise_30_list_all_files():
    """
    Exercise 30: List All Files in Directory and Save
    Problem Statement: Write a Python program to list all files
        (not subdirectories) in a given directory and save
        their names to a text file.
    Purpose: This exercise combines directory traversal with file
        writing – a practical pattern used in file inventory
        scripts, backup tools, and project documentation
        generators.
    Given Input:
        A directory my_folder containing notes.txt,
        data.csv, and report.pdf.
    Expected Output:
        A file file_list.txt containing one filename per line,
        confirmed by printing File list saved to file_list.txt
    """
    print("Exercise 30: List All Files in Directory and Save")
    pass




