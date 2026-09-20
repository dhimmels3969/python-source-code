import logging
from pathlib import Path
from src.common_library import helper_functions as hf

#
# https://pynative.com/python-os-sys-module-exercises/
# Exercises 1 through 10
#


logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)



#########################################################################################
def exercise_11_read_environment_variable():
    """
    Exercise 11: Read an Environment Variable
    Problem Statement:
        Write a Python program that reads the system’s PATH
        environment variable and prints its value. If the
        variable is not found, print a default fallback message.
    Purpose:
        Environment variables are the standard way to
        pass configuration into programs without hardcoding
        values. Reading them is essential for writing scripts
        that behave differently across development, staging,
        and production environments, or that respect
        system-level settings.
    Given Input:
        No input required. The value is read from the operating
        system environment.
    Expected Output:
        The value of the PATH variable (a long colon-separated
        string on Unix or semicolon-separated on Windows).
    """
    logger.info("Exercise 11: Read an Environment Variable")
    pass



#########################################################################################
def exercise_12_set_environment_variable():
    """
    Exercise 12: Set an Environment Variable
    Problem Statement:
        Write a Python program that sets a custom environment variable
        called APP_MODE to the value development, then reads it back
        and prints it.
    Purpose:
        Setting environment variables at runtime lets scripts configure
        themselves or communicate settings to child processes. This is
        a common pattern in web frameworks, CLI tools, and test
        harnesses that need to switch between modes without changing
        source code.
    Given Input:
        No external input. The variable is defined within the script.
    Expected Output:
        APP_MODE is set to: development
    """
    logger.info("Exercise 12: Set Environment Variable")
    pass



#########################################################################################
def exercise_13_list_environment_variables():
    """
    Exercise 13: List All Environment Variables
    Problem Statement:
        Write a Python program that prints all currently available
        environment variables, displaying each name and its value
        on a separate line in a readable format.
    Purpose:
        Inspecting the full environment is helpful when debugging
        configuration issues, auditing what a script can see at
        runtime, or exploring a new system. This exercise also
        reinforces how to iterate over a dictionary-like object.
    Given Input:
        No input required. The data is read from the live
        process environment.
    Expected Output:
        A list of all environment variable names and
        values, one per line (output varies by system).
    """
    logger.info("Exercise 13: List All Environment Variables")
    pass



#########################################################################################
def exercise_14_get_current_process_id():
    """
    Exercise 14: Get Current Process ID
    Problem Statement:
        Write a Python program that retrieves and prints the
        process ID (PID) of the currently running Python script.
    Purpose:
        The process ID uniquely identifies a running program
        on the operating system. It is useful in logging,
        debugging multi-process applications, creating unique
        temporary filenames, and communicating between processes.
        This exercise introduces basic process introspection
        using the os module.
    Given Input:
        No input required. The PID is provided by the operating system.
    Expected Output:
        Current Process ID: 12345 (the actual number will vary
        each time the script runs)
    """
    logger.info("Exercise 14: Get Current Process ID")
    pass



#########################################################################################
def exercise_15_run_shell_command():
    """
    Exercise 15: Run a Shell Command
    Problem Statement:
        Write a Python program that runs a shell command using os.system()
        and prints the exit code returned by the command.
    Purpose:
        Running shell commands from within Python is a common requirement in
        automation scripts, build tools, and system administration utilities.
        This exercise introduces os.system() as the simplest way to invoke
        a command and inspect whether it succeeded or failed.
    Given Input:
        No external input required. The command is hardcoded in the script.
    Expected Output:
        The output of the shell command printed to the terminal,
        followed by Exit code: 0
    """
    logger.info("Exercise 15: Run a Shell Command")
    pass



#########################################################################################
def exercise_16_walk_directory_tree():
    """
    Exercise 16: Walk a Directory Tree
    Problem Statement:
        Write a Python program that recursively lists all files
        in a directory and its subdirectories, printing the full
        path of each file found.
    Purpose:
        Traversing an entire directory tree is essential for tasks
        such as bulk file processing, searching for specific files,
        calculating total disk usage, and building file indexing
        tools. os.walk() handles all the recursion automatically,
        making it far simpler than writing your own recursive function.
    Given Input:
        A sample directory tree created in the script: walk_demo/
        with two subdirectories each containing a
        text file.
    Expected Output:
        Full path of every file found inside the directory tree,
        one per line.
    """
    logger.info("Exercise 16: Walk a Directory Tree")
    pass



#########################################################################################
def exercise_17_join_paths_safely():
    """
    Exercise 17: Join Paths Safely
    Problem Statement:
        Write a Python program that constructs a file path from
        separate components using os.path.join() and prints the
        resulting path.
    Purpose:
        Hardcoding path separators like / or \ makes scripts brittle
        and platform-specific. Using os.path.join() is the correct,
        portable approach that automatically uses the right
        separator for the operating system the script runs on.
    Given Input:
        base = "projects", subfolder = "python_exercises"
        , filename = "solution.py"
    Expected Output:
        projects/python_exercises/solution.py (on Unix) or
        projects\python_exercises\solution.py (on Windows)
    """
    logger.info("Exercise 17: Join Paths Safely")
    pass



#########################################################################################
def exercise_18_get_absolute_path():
    """
    Exercise 18: Get Absolute Path
    Problem Statement:
        Write a Python program that takes a relative file path and
        converts it to its full absolute path.
    Purpose:
        Relative paths depend on the current working directory, which can
        change during a script’s execution. Converting to an absolute
        path early on locks in the location and prevents hard-to-debug
        errors when functions change directories mid-run or when paths
        are passed to other modules.
    Given Input:
        relative_path = "data/report.csv"
    Expected Output:
        A full absolute path such as /home/user/projects/data/report.csv
        (varies by system and working directory)
    """
    logger.info("Exercise 18: Get Absolute Path")
    pass



#########################################################################################
def exercise_19_print_python_version():
    """
    Exercise 19: Print Python Version
    Problem Statement:
        Write a Python program that displays the current Python
        version in two formats: as a human-readable string and
        as a structured named tuple with individual version
        components.
    Purpose:
        Knowing the Python version at runtime is essential for
        writing scripts that conditionally use features only
        available in certain versions. It is also a standard first l
        ine of defence when debugging environment issues across
        different machines or deployment targets.
    Given Input:
        No input required. The version is provided by the
        Python interpreter.
    Expected Output:
        Python version: 3.11.4 (main, ...) and Major: 3 Minor: 11
        Micro: 4 (values vary by installation)
    """
    logger.info("Exercise 19: Print Python Version")
    pass



#########################################################################################
def exercise_20_read_command_line_arguments():
    """
    Exercise 20: Read Command-Line Arguments
    Problem Statement:
        Write a Python program that reads arguments passed to it
        from the command line and prints each argument with its
        index position.
    Purpose:
        Command-line arguments are the primary way to pass inputs
        to standalone scripts without hardcoding values or using
        interactive prompts. This exercise introduces sys.argv,
        which is the foundation for building CLI tools, utility
        scripts, and programs that integrate into shell pipelines.
    Given Input:
        Run the script from the terminal as:
        python solution.py hello world 42
    Expected Output:
        Each argument printed with its index, starting with
        the script name at index 0.
    """
    logger.info("Exercise 20: Read Command-Line Arguments")
    pass



