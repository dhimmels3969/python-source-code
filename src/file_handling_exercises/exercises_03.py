from src.common_library import helper_functions as hf
from pathlib import Path
import shutil
import os
import re


#
# Exercises found at web page https://pynative.com/python-file-handling-exercises/
# Exercises 21 through 30
#



##############################################################################
def exercise_21_convert_uppercase_and_lowercase(root_dir):
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
    def invert_case(line_in):
        line_out = ""
        for char in line_in:
            if char.isupper():
                line_out += char.lower()
            else:
                if char.islower():
                    line_out += char.upper()
                else:
                    line_out += char
        return line_out

    print("Exercise 21: Convert Uppercase to Lowercase and Vice Versa")
    file_path = hf.build_file_name(root_dir, "data/file_handling_exercises", "hello_world.txt")
    file_path_out = hf.build_file_name(root_dir, "data/file_handling_exercises/dummy", "hello_world_swapped.txt")

    with open(file_path, 'r') as file, open(file_path_out, 'w') as file_out:
        lines_in_the_file = file.readlines()
        for line in lines_in_the_file:
            results = invert_case(line)
            file_out.write(results)
    pass


##############################################################################
def exercise_22_find_replace(root_dir):
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
    file_path = hf.build_file_name(root_dir, "data/file_handling_exercises", "python.txt")
    results = ""
    with open(file_path, 'r') as file:
        content = file.read()
        results = content.replace("Java", "Python")

    with open(file_path, 'w') as file_out:
        file_out.write(results)
    pass


##############################################################################
def exercise_23_get_file_size_kilobytes(root_dir):
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
    KILOBYTES = 1024
    print("Exercise 23: Get File Size in Kilobytes")
    file_path = hf.build_file_name(root_dir, "data/file_handling_exercises", "lorem_ipsum.txt")
    file_size_bytes = os.path.getsize(file_path)
    file_size_kilobytes = file_size_bytes / KILOBYTES
    print(f"  File Size Lorem Ipsum: {file_size_bytes} Bytes")
    print(f"  File Size Lorem Ipsum: {file_size_kilobytes:.2f} Kilobytes")
    pass


##############################################################################
def exercise_24_copy_file_using_binary_mode(root_dir):
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
    file_path = hf.build_file_name(root_dir, "data/file_handling_exercises", "lorem_ipsum.txt")
    file_path_out = hf.build_file_name(root_dir, "data/file_handling_exercises/dummy", "lorem_ipsum_copy.txt")
    with open(file_path, 'rb') as file:
        content = file.read()

    with open(file_path_out, 'wb') as file_out:
        file_out.write(content)

    # get file size for both files
    file_size_bytes_original = os.path.getsize(file_path)
    file_size_bytes_copy = os.path.getsize(file_path_out)
    print(f"  Original        Copy")
    print(f"  {file_size_bytes_original}           {file_size_bytes_copy}")
    pass


##############################################################################
def exercise_25_rename_single_file(root_dir):
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
    file_path = hf.build_file_name(root_dir, "data/file_handling_exercises/dummy", "lorem_ipsum_copy.txt")
    file_path_out = hf.build_file_name(root_dir, "data/file_handling_exercises/dummy", "lorem_ipsum_copy_dest.txt")
    # rename the filw     lorem_ipsum_copy.txt -> lorem_ipsum_copy_dest.txt
    try:
        os.rename(file_path, file_path_out)
    except Exception as error:
        print(error)

    # display directory info for files containing lorem_ipsum
    file_list = [file for file in os.listdir("../data/file_handling_exercises/dummy") if "lorem" in file]
    print(f"  File list: {file_list}")

    # rename the file back to the original name
    # lorem_ipsum_copy_dest.txt -> lorem_ipsum_copy.txt
    os.rename(file_path_out, file_path)
    pass


##############################################################################
def exercise_26_rename_multiple_files(root_dir):
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
    def reset(root_dir, folder_):
        contents = [file for file in os.listdir(folder_) if
                    "lorem".lower() not in file.lower() and "swapped".lower() not in file.lower()]
        files_to_copy = ["notes.txt", "data.txt"]
        # delete files in the target folder
        for file in contents:
            target_file = hf.build_file_name(root_dir, "data/file_handling_exercises/dummy", file)
            os.remove(target_file)

        for file in files_to_copy:
            source_file = hf.build_file_name(root_dir, "data/file_handling_exercises/", file)
            # copy files from the src folder to the target folder
            target_file = hf.build_file_name(root_dir, "data/file_handling_exercises/dummy", file)
            shutil.copyfile(source_file, target_file)
        pass
    print("Exercise 26: Rename Multiple Files with Prefix")
    tgt_dir = "../data/file_handling_exercises/dummy"
    reset(root_dir, tgt_dir)
    contents = [file for file in os.listdir(tgt_dir) if "lorem" not in file and "swapped" not in file]
    prefix = "2024"

    for file in contents:
        revised_name = "_".join([prefix, file])
        file_path = hf.build_file_name(root_dir, "data/file_handling_exercises/dummy", file)
        file_path_out = hf.build_file_name(root_dir, "data/file_handling_exercises/dummy", revised_name)
        os.rename(file_path, file_path_out)
        print(f"  Renamed: {file} -> {revised_name}")
    pass


##############################################################################
def exercise_27_delete_a_file(root_dir):
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
    def reset(root_dir):
        # reload the file to be deleted to the dummy directory
        # copy lorem_ipsum.txt and rename to temp.txt  in the target folder
        files_to_copy = ["lorem_ipsum.txt"]
        target_file_name = "temp.txt"

        for file in files_to_copy:
            source_file = hf.build_file_name(root_dir, "data/file_handling_exercises/", file)
            # copy files from the src folder to the target folder
            target_file = hf.build_file_name(root_dir, "data/file_handling_exercises/dummy", target_file_name)
            shutil.copyfile(source_file, target_file)
        pass

    def delete_file(target_file):
        if Path(target_file).is_file():
            Path(target_file).unlink()
            print(f"  Requested file {target_file_name_valid} has been deleted.")
        else:
            print(f"  Requested file {target_file_name_invalid} not found and could not be deleted.")
        pass

    print("Exercise 27: Delete a File from Disk")
    reset(root_dir)
    target_file_name_valid = "temp.txt"
    target_file_name_invalid = "non_existent_temp.txt"
    ####
    requests = [hf.build_file_name(root_dir,
                "data/file_handling_exercises/dummy", target_file_name_invalid),
                hf.build_file_name(root_dir,
                "data/file_handling_exercises/dummy", target_file_name_valid)]
    for request in requests:
        delete_file(request)
    pass


##############################################################################
def exercise_28_merge_multiple_files(root_dir):
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
    input_files = [
        hf.build_file_name(root_dir, "data/file_handling_exercises/", "file1.txt"),
        hf.build_file_name(root_dir, "data/file_handling_exercises/", "file2.txt")
    ]
    output_file = hf.build_file_name(root_dir, "data/file_handling_exercises/dummy", "merged.txt")
    with open(output_file, "a") as outfile:
        for file in input_files:
            with open(file, "r") as infile:
                outfile.write(infile.read())
                outfile.write("\n")

    pass


##############################################################################
def exercise_29_reverse_line_order(root_dir):
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
    input_files = hf.build_file_name(root_dir, "data/file_handling_exercises/", "lines.txt")
    output_file = hf.build_file_name(root_dir, "data/file_handling_exercises/dummy",
                                     "lines_reversed.txt")
    with open(input_files, "r") as infile:
        lines = infile.readlines()
    reversed_lines = lines[::-1]
    with open(output_file, "w") as outfile:
        outfile.writelines(reversed_lines)
    pass


##############################################################################
def exercise_30_list_all_files(root_dir):
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
    myDirectory = "\\".join([str(root_dir), "data\\file_handling_exercises\\dummy\\"])
    myOutputList = hf.build_file_name(root_dir, "data/file_handling_exercises/dummy"
                                      , "file_list_exercise_30.txt")
    results = os.listdir(myDirectory)
    with open(myOutputList, "w") as outfile:
        for item in results:
            if Path(myDirectory + item).is_file():
                outfile.write(item + "\n")
    print(f"  File List saved to {myOutputList}")
    pass




