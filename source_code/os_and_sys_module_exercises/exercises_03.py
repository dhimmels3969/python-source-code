import logging
from pathlib import Path
from source_code.common_library import helper_functions as hf

#
# https://pynative.com/python-os-sys-module-exercises/
# Exercises 1 through 10
#


logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)



#########################################################################################
def exercise_21_exit_program():
    """
    Exercise 21: Exit a Program
    Problem Statement:
        Write a Python program that checks whether a
        required command-line argument is provided
        and exits gracefully with a descriptive error
        message if it is missing.
    Purpose:
        Controlled program termination is a sign of
        well-written scripts. Rather than letting a program
        crash with a cryptic traceback, sys.exit() lets
        you stop execution cleanly, communicate the reason
        to the user, and signal success or failure to
        the calling shell or process manager.
    Given Input:
        Run without arguments (python solution.py) to
        trigger the exit, or with one argument
        (python solution.py Alice) to proceed normally.
    Expected Output: Error:
        Please provide a name as an argument. followed
        by exit, or Hello, Alice! if the argument
        is present.
    """
    logger.info("Exercise 21: Exit a Program")
    pass



#########################################################################################
def exercise_22_get_platform_info():
    """
    Exercise 22: Get Platform Info
    Problem Statement:
        Write a Python program that identifies the current operating
        system platform and prints a human-readable description of it.
    Purpose:
        Writing cross-platform scripts requires knowing which OS
        the code is running on so that platform-specific behaviour –
        such as choosing the right shell command, file separator,
        or config path – can be handled correctly. This exercise
        introduces the two most common ways to detect the platform
        at runtime.
    Given Input:
        No input required. The platform is detected from the runtime environment.
    Expected Output:
        Platform: linux and Detailed platform:
        Linux-5.15.0-x86_64 (values vary by system)
    """
    logger.info("Exercise 22: Get Platform Info")
    pass



#########################################################################################
def exercise_23_inspect_sys_dot_path():
    """
    Exercise 23: Inspect sys.path
    Problem Statement:
        Write a Python program that prints all the directories
        Python searches when looking for modules to import,
        displaying each directory on a separate line.
    Purpose:
        Understanding sys.path is essential for diagnosing
        ModuleNotFoundError problems, understanding how Python
        resolves imports, and knowing where to place custom
        modules so they can be imported without any configuration.
        This exercise builds a mental model of how Python’s
        import system works.
    Given Input:
        No input required. The path list is maintained
         by the Python interpreter.
    Expected Output:
        A numbered list of all directories in the module search
        path (output varies by system and virtual environment).
    """
    logger.info("Exercise 23: Inspect sys.path")
    pass



#########################################################################################
def exercise_24_add_to_sys_dot_path():
    """
    Exercise 24: Add to sys.path
    Problem Statement:
        Write a Python program that dynamically adds a custom directory
        to sys.path so that modules stored in that directory can be
        imported without installing them as packages.
    Purpose:
        There are situations where you need to import a module from
        a non-standard location – for example, a shared utilities
        folder, a sibling project directory, or a path determined
        at runtime. Modifying sys.path programmatically is the
        direct way to achieve this without changing environment
        variables or restructuring the project.
    Given Input:
        A custom directory path custom_modules containing a
        simple Python file greet.py (both created in the script).
    Expected Output:
        Hello from custom module!
    """
    logger.info("Exercise 24: Add to sys.path")
    pass



#########################################################################################
def exercise_25_get_recursion_limit():
    """
    Exercise 25: Get Recursion Limit
    Problem Statement:
        Write a Python program that retrieves and prints the maximum
        recursion depth allowed by the current Python interpreter.
    Purpose:
        Python limits how deeply functions can call themselves to
        prevent a stack overflow from consuming all available memory.
        Knowing this limit helps you understand why deeply
        recursive algorithms fail with a RecursionError and prepares
        you for the next exercise where the limit is adjusted.
    Given Input:
        No input required.
    Expected Output:
        Current recursion limit: 1000 (the default on most
        Python installations)
    """
    logger.info("Exercise 25: Get Recursion Limit")
    pass



#########################################################################################
def exercise_26_change_recursion_limit():
    """
    Exercise 26: Change Recursion Limit
    Problem Statement:
        Write a Python program that increases the recursion
        limit and then tests it by running a recursive
        function that would fail under the default limit.
    Purpose:
        Some legitimate algorithms – such as processing deeply
        nested JSON, traversing large trees, or implementing
        certain parsers – require a deeper call stack than
        Python’s default allows. This exercise shows how to
        raise the limit safely and why it should be done with care.
    Given Input:
        No input required. The recursion depth is set
        within the script.
    Expected Output:
        Old limit: 1000, New limit: 2000, and Recursion
        test with depth 1500: passed
    """
    logger.info("Exercise 26: Change Recursion Limit")
    pass



#########################################################################################
def exercise_27_script_info_logger():
    """
    Exercise 27: Script Info Logger
    Problem Statement:
        Write a Python program that collects information about
        itself – its filename, the current working directory,
        and the OS platform – and writes all of it to a log file
        called script_info.log.
    Purpose:
        Logging runtime context is a fundamental practice
        in production scripts and scheduled jobs. When something
        goes wrong, a log that captures where the script ran,
        on what platform, and under which filename gives you
        the starting point for diagnosis. This exercise combines
        sys and os together for the first time in a practical
        output task.
    Given Input:
        No input required. All values are derived
        from the runtime environment.
    Expected Output:
        A file script_info.log created in the current
        directory, and the log contents printed to the terminal.
    """
    logger.info("Exercise 27: Script Info Logger")
    pass



#########################################################################################
def exercise_28_directory_size_calculator():
    """
    Exercise 28: Directory Size Calculator
    Problem Statement:
        Write a Python program that calculates the total size
        of all files in a directory tree and displays the
        result in bytes, kilobytes, and megabytes.
    Purpose:
        Calculating disk usage is a practical task in backup
        tools, storage monitoring scripts, and deployment
         pipelines. This exercise combines os.walk() for
         recursion with os.path.getsize() for per-file
         measurement, reinforcing how the two functions
         work together.
    Given Input:
        A sample directory tree size_demo/ created
        in the script with a few files of varying sizes.
    Expected Output:
        Total size printed in bytes, KB, and MB (exact
        values depend on the test files created).
    """
    logger.info("Exercise 28: Directory Size Calculator")
    pass



#########################################################################################
def exercise_29_environment_config_loader():
    """
    Exercise 29: Environment Config Loader
    Problem Statement:
        Write a Python program that simulates loading application
        configuration by reading multiple environment variables
        with fallback defaults, then prints a formatted summary
        of the configuration to standard output.
    Purpose:
        Reading configuration from environment variables is the
        industry-standard approach for twelve-factor applications.
        It keeps secrets and environment-specific settings out
        of source code. This exercise combines os.environ.get()
        with sys.stdout to build a realistic config-loading
        pattern used in web apps, APIs, and CLI tools.
    Given Input:
        Environment variables APP_HOST, APP_PORT, and
        APP_DEBUG – set within the script to simulate
        a configured environment.
    Expected Output:
        A formatted configuration summary printed to
        stdout showing each key and its resolved value.
    """
    logger.info("Exercise 29: Environment Config Loader")
    pass



#########################################################################################
def exercise_30_recursive_file_finder():
    """
    Exercise 30: Recursive File Finder
    Problem Statement:
        Write a Python program that accepts a file extension as a
        command-line argument and recursively searches the current
        directory tree for all files matching that extension,
        printing the full path of each match.
    Purpose:
        This capstone exercise combines everything covered in the
        module: sys.argv for input, sys.exit() for validation,
        os.walk() for traversal, os.path.join() for path construction,
        and os.path.splitext() for extension matching. It mirrors a
        real-world utility script that you might use or build as
        part of a larger automation pipeline.
    Given Input:
        Run as python solution.py .txt from the terminal. A sample
        directory tree with mixed file types is created by the
        script for testing.
    Expected Output:
        Full paths of all .txt files found in the directory tree
        , followed by a count of matches.
    """
    logger.info("Exercise 30: Recursive File Finder")
    pass



