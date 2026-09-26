import logging
import os
from pathlib import Path
from source_code.common_library import helper_functions as hf

#
# https://pynative.com/python-os-sys-module-exercises/
# Exercises 1 through 10
#


logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)



#########################################################################################
def exercise_01_print_current_directory():
    """
    Exercise 1: Print Current Directory
    Problem Statement:
        Write a Python program that prints the current working
        directory to the console.
    Purpose:
        This exercise introduces the os module and its most
        fundamental function. Knowing how to retrieve the
        current working directory is a foundational skill for
        file I/O operations, path construction, and building
        scripts that need to locate resources relative to
        where they run.
    Given Input:
        No input required. The function reads the environment
        directly.
    Expected Output:
        /home/user/projects (the actual path will vary
        based on your system)
    """
    logger.info("Exercise 1: Print Current Directory")
    current_directory = Path(os.getcwd())
    logger.info(f"  current working directory: {current_directory}")
    pass



#########################################################################################
def exercise_02_list_directory_contents():
    """
    Exercise 2: List Directory Contents
    Problem Statement:
        Write a Python program that lists all files and folders
        in a given directory path.
    Purpose:
        This exercise teaches you to inspect a directory’s
        contents programmatically. It is a core skill for
        building file managers, automation scripts, batch
        processors, and any tool that needs to discover
        what files are available at runtime.
    Given Input:
        path = "." (the current directory)
    Expected Output:
        A printed list of all file and folder names
        in the specified directory (output varies
        by system).
    """
    logger.info("Exercise 2: List Directory Contents")
    pass



#########################################################################################
def exercise_03_create_directory():
    """
    Exercise 3: Create a Directory
    Problem Statement:
        Write a Python program that creates a new folder called
        test_folder in the current working directory, only if
        it does not already exist.
    Purpose:
        Creating directories programmatically is essential
        for setting up output folders, organising generated
        files, and building scripts that prepare a workspace
        before writing data. Checking for existence first
        prevents crashes from duplicate creation.
    Given Input:
        folder_name = "test_folder"
    Expected Output:
        Folder 'test_folder' created successfully. or
        Folder 'test_folder' already exists.
    """
    logger.info("Exercise 3: Create a Directory")
    pass



#########################################################################################
def exercise_04_create_nested_directories():
    """
    Exercise 4: Create Nested Directories
    Problem Statement:
        Write a Python program that creates a nested directory
        structure a/b/c in the current working directory, even if
        some or all of the parent directories do not yet exist.
    Purpose:
        Real-world scripts frequently need to create deep folder
        hierarchies in a single step – for example, when organising
        output by date (logs/2025/06/10) or project structure.
        os.makedirs() handles this without requiring manual
        creation of each level.
    Given Input:
        nested_path = "a/b/c"
    Expected Output:
        Nested directories 'a/b/c' created successfully.
    """
    logger.info("Exercise 4: Create Nested Directories")
    pass



#########################################################################################
def exercise_05_rename_file():
    """
    Exercise 5: Rename a File
    Problem Statement:
        Write a Python program that renames a file called old.txt
        to new.txt in the current directory, with a check to
        confirm the source file exists before attempting the rename.
    Purpose:
        Renaming files is a common task in file management scripts,
        data pipelines, and backup utilities. This exercise reinforces
        safe file handling by combining existence checks with the
        rename operation, preventing runtime errors on missing files.
    Given Input:
        A file named old.txt must exist in the current directory.
    Expected Output:
        Renamed 'old.txt' to 'new.txt' successfully. or
        Source file 'old.txt' does not exist.
    """
    logger.info("Exercise 5: Rename a File")
    pass



#########################################################################################
def exercise_06_delete_file():
    """
    Exercise 6: Delete a File
    Problem Statement:
        Write a Python program that deletes a file called temp.txt
        from the current directory, but only after verifying that
        the file actually exists.
    Purpose:
        Safe file deletion is a critical skill in automation and
        cleanup scripts. Blindly calling a delete function without
        checking for existence will raise an exception and halt
        your program. This exercise builds the habit of defensive
        file operations.
    Given Input:
        A file named temp.txt (created in the script for testing).
    Expected Output:
        File 'temp.txt' deleted successfully. or
        File 'temp.txt' not found.
    """
    logger.info("Exercise 6: Delete a File")
    pass



#########################################################################################
def exercise_07_delete_directory_tree():
    """
    Exercise 7: Delete a Directory Tree
    Problem Statement:
        Write a Python program that creates a nested directory
        structure cleanup/a/b, adds a dummy file inside it, then
        removes the entire tree including all contents.
    Purpose:
        Removing a directory and all of its contents is a frequent
        requirement in test teardown, temporary file cleanup,
        and build scripts. This exercise demonstrates the
        difference between os.rmdir() (empty directories only)
        and shutil.rmtree() (recursive deletion).
    Given Input:
        Directory tree cleanup/a/b with a file cleanup/a/b/note.txt
        inside (created in the script).
    Expected Output:
        Directory tree 'cleanup' removed successfully.
    """
    logger.info("Exercise 7: Delete a Directory Tree")
    pass



#########################################################################################
def exercise_08_check_if_path_exists():
    """
    Exercise 8: Check Path Existence
    Problem Statement:
        Write a Python program that checks whether a given file
        or directory path exists on the system and prints a
        descriptive message indicating the result.
    Purpose:
        Before performing any file operation – reading, writing,
        deleting, or renaming – it is good practice to verify that
        the target path actually exists. This exercise builds the
        habit of defensive path checking, which prevents
        FileNotFoundError crashes in production scripts.
    Given Input:
        path = "sample.txt" (created in the script for testing)
    Expected Output:
        Path 'sample.txt' exists. or
        Path 'sample.txt' does not exist.
    """
    logger.info("Exercise 8: Check Path Existence")
    pass



#########################################################################################
def exercise_09_split_file_extension():
    """
    Exercise 9: Split File Extension
    Problem Statement:
        Write a Python program that takes a filename string and
        extracts both the base name and the file extension
        separately.
    Purpose:
        Parsing filenames is a routine task in file processing
        pipelines – for example, when filtering files by type, renaming
        files while preserving extensions, or routing files to different
        handlers based on format. This exercise introduces the clean
        , OS-aware way to split a filename.
    Given Input:
        filename = "report_2025.pdf"
    Expected Output:
        Base: report_2025 and Extension: .pdf
    """
    logger.info("Exercise 9: Split File Extension")
    pass



#########################################################################################
def exercise_10_get_file_size():
    """
    Exercise 10: Get File Size
    Problem Statement:
        Write a Python program that creates a file with
        some content and then prints its size in bytes.
    Purpose:
        Checking file size is useful in scripts that enforce size
        limits, monitor disk usage, validate that a file was
        written correctly, or decide whether to process a file.
        This exercise shows how to retrieve file metadata
        without opening the file itself.
    Given Input:
        A file named data.txt containing the text
        Hello, Python! (created in the script).
    Expected Output:
        File size: 14 bytes
    """
    logger.info("Exercise 10: Get File Size")
    pass



