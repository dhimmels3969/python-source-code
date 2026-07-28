import json
import logging
from pathlib import Path
import math
from src.common_library import helper_functions as hf

#
# https://pynative.com/python-exception-handling-exercises/
# Exercises 1 through 10
#


logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)



#########################################################################################
def exercise_01_try_except_test():
    """
    Exercise 1: Basic Try-Except
    Problem Statement:
        Write a Python program that asks the user to enter a number.
        If the input is not a valid integer, raise a ValueError and
        display a helpful error message instead of crashing.
    Purpose:
        This exercise introduces the fundamental try/except pattern in
        Python. Handling invalid user input gracefully is one of the
        most common real-world uses of exception handling, and
        mastering it is a key step toward writing robust,
        user-friendly programs.
    Given Input:
        User enters "hello" when prompted for a number.
    Expected Output:
        Error: That was not a valid integer. Please enter a number.
    """
    logger.info(f"Exercise 1: Basic Try-Except")
    logger.info(f"  Please enter a number between 1 and 10:")
    rspns_01 = "hello"
    logger.info(f"  {rspns_01}")
    try:
        rspns_02 = int(rspns_01)
    except ValueError as e:
        logger.info(f"  ***Error: That was not a valid integer. Please enter a number.")
        logger.info(f"  ***{e}")
    pass



#########################################################################################
def exercise_02_division_error_prevention():
    """
    Exercise 2: Division Safety
    Problem Statement:
        Create a function safe_divide(a, b) that divides a by b.
        If b is zero, handle the ZeroDivisionError and return
        None instead of letting the program crash.
    Purpose:
        Division by zero is a classic runtime error that appears
        in financial calculations, data pipelines, and scientific
        code. This exercise teaches you to wrap risky arithmetic
        in exception handling and return a sentinel value when
        a valid result cannot be produced.
    Given Input:
        Call safe_divide(10, 0) and safe_divide(10, 2).
    Expected Output:
        None for the first call and 5.0 for the second.
    """
    def safe_divide(a, b):
        results = 0
        try:
            results = a / b
        except ZeroDivisionError:
            results = None
        return results

    logger.info(f"Exercise 2: Division Safety")
    a, b = 10, 0
    results = safe_divide(a, b)
    logger.info(f"  {a} / {b} = {results}")
    a, b = 10, 2
    results = safe_divide(a, b)
    logger.info(f"  {a} / {b} = {results}")
    pass



#########################################################################################
def exercise_03_file_not_found(root_dir):
    """
    Exercise 3: File Not Found
    Problem Statement:
        Write a program that tries to open a file that does not
        exist on disk. Catch the FileNotFoundError exception
        and display a clear, user-friendly message instead of
        showing a raw Python traceback.
    Purpose:
        File I/O is one of the most error-prone operations in any
        program. Learning to handle missing files gracefully makes
        your scripts production-ready and prevents cryptic crashes
        when the environment differs from what you expect.
    Given Input:
        Attempt to open "missing_file.txt" for reading.
    Expected Output:
        Error: The file 'missing_file.txt' was not found.
        Please check the filename and path.

        Error Message from system: "[Errno 2] No such file or directory: "
    """
    logger.info(f"Exercise 3: File Not Found")
    missing_file = hf.build_file_name(root_dir
                        , "data/exception_handling_exercises"
                        , "missing_file.txt")
    try:
        with open(missing_file, "r") as f:
            logger.info(f"  {missing_file} opened!")
    except FileNotFoundError as e:
        logger.info(f"  Error: The file 'missing_file.txt' was not found.")
        logger.info(f"  Please check the filename and path.")
        # logger.info(f"  {e}")
    pass



#########################################################################################
def exercise_04_index_out_of_range():
    """
    Exercise 4: Index Out of Range
    Problem Statement:
        Given a fixed list, ask the user to enter an index and print the
        element at that position. If the index is outside the valid range,
        catch the IndexError and display an informative message.
    Purpose:
        Accessing list elements by index is something Python developers
        do constantly. This exercise builds the habit of validating or
        protecting index-based access, which is critical in data processing,
        game development, and any code that works with sequences
        of unknown length.
    Given Input:
        items = ["apple", "banana", "cherry"] and the user enters index 5.
    Expected Output:
        Error: Index 5 is out of range. The list has 3 items
        (valid indices: 0 to 2).
    """
    logger.info(f"Exercise 4: Index Out of Range")
    items = ["apple", "banana", "cherry"]
    requested_index = len(items) + 2
    try:
        item = items[requested_index]
    except IndexError as e:
        logger.info(f"  Error: Index {requested_index} is out of range. The list has {len(items)} items.")
        logger.info(f"  (Valid Indices: 0 to {len(items) - 1}).")
    pass



#########################################################################################
def exercise_05_key_error_test():
    """
    Exercise 5: Key Error Handling
    Problem Statement:
        Given a dictionary of country capitals, ask the user to enter
        a country name and print the corresponding capital. If the
        country is not in the dictionary, catch the KeyError and
        display a helpful message.
    Purpose:
        Dictionary lookups are everywhere in Python: configuration parsing,
        JSON processing, API responses, and more. Knowing how to handle
        a missing key cleanly, rather than letting a KeyError crash your
        program, is an essential skill for working with real-world data.
    Given Input:
        capitals = {"France": "Paris", "Japan": "Tokyo", "Brazil": "Brasilia"}
        and the user enters "Germany".
    Expected Output:
        Error: 'Germany' was not found in the dictionary.
    """
    logger.info(f"Exercise 5: Key Error Handling")
    capitals = {"France": "Paris", "Japan": "Tokyo", "Brazil": "Brasilia"}
    requested_key = "Germany"
    try:
        capital = capitals[requested_key]
    except KeyError as e:
        logger.info(f"  Error: '{requested_key}' was not found in the dictionary.")
    pass



#########################################################################################
def exercise_06_type_error_prevention():
    """
    Exercise 6: Type Error Guard
    Problem Statement:
        Write a function add_values(a, b) that returns the sum of two
        values. If the arguments are of incompatible types (for example,
        a string and an integer), catch the TypeError and return a
        descriptive error message instead of crashing.
    Purpose:
        Python is dynamically typed, which means type mismatches only
        surface at runtime. This exercise teaches you to guard
        operations that assume specific types, a habit that becomes
        critical when processing data from external sources such as
        APIs, CSV files, or user forms where the shape of the data is not
        always guaranteed.
    Given Input:
        Call add_values(10, "20") and add_values(10, 20).
    Expected Output:
        Error: incompatible types for addition. for the first call and 30 for the second.
    """

    def add_values(a, b):
        results = ""
        try:
            results = a + b
        except TypeError as e:
            results = "Error: incompatible types for addition."
        return results

    logger.info(f"Exercise 6: Type Error Guard")
    message = add_values(10, "20")
    logger.info(f"  {message}")
    message = add_values(10, 20)
    logger.info(f"  {message}")
    pass



#########################################################################################
def exercise_07_multiple_exceptions():
    """
    Exercise 7: Multiple Exceptions
    Problem Statement:
        Write a function parse_and_divide(value, divisor) that converts
        value to a float and then divides it by divisor. Use a single
        try block that handles ValueError (bad conversion) and
        ZeroDivisionError (division by zero) with separate messages
        for each.
    Purpose:
        Real programs rarely face only one kind of failure. This
        exercise shows you how to stack multiple except clauses
        after one try block so each error type gets its own tailored
        response, keeping error-handling logic clear
        and maintainable.
    Given Input:
        Call parse_and_divide("abc", 2) and parse_and_divide("10", 0)
        and parse_and_divide("10", 2).
    Expected Output:
        Error: 'abc' cannot be converted to a number.
        Error: Cannot divide by zero.
        5.0
    """
    def parse_and_divide(value, divisor):
        results = ""
        try:
            converted_value = float(value)
            results = converted_value / divisor
        except ValueError as e:
            results = f"Error: '{value}' cannot be converted to a number."
        except ZeroDivisionError as e:
            results = f"Error: Cannot divide by zero."
        return results
        pass

    def test_parse_and_divide(value, divisor):
        results = parse_and_divide(value, divisor)
        logger.info(f"  {results}")

    logger.info(f"Exercise 7: Multiple Exceptions")
    test_parse_and_divide("abc", 2)
    test_parse_and_divide("10", 0)
    test_parse_and_divide("10", 2)
    pass



#########################################################################################
def exercise_08_finally_block_testing(root_dir):
    """
    Exercise 8: Finally Block
    Problem Statement:
        Write a function read_file(filename) that opens a file manually
        (without a with statement), reads its contents, and uses a
        finally block to ensure the file handle is always closed,
        whether the read succeeds or an exception is raised.
    Purpose:
        The finally block is Python’s mechanism for guaranteed cleanup.
        Understanding it is essential for managing resources such
        as file handles, database connections, and network sockets
        correctly, especially in older codebases or situations
        where the with statement is not available.
    Given Input:
        Call read_file("hello.txt") where the file exists, and
        then read_file("missing.txt") where it does not.
    Expected Output:
        File closed.
        Hello from the file!
        ---
        File closed.
        Error: 'missing.txt' not found.
    """
    def read_file(filename):
        results = ""
        try:
            with open(filename, "r") as f:
                results = "Hello from the file!"
        except FileNotFoundError as e:
            results = f"  Error: {Path(filename).name} not found."
        finally:
            logger.info(f"  File closed.")
            logger.info(f"  {results}")
        pass

    logger.info(f"Exercise 8: Finally Block")
    hello_file = hf.build_file_name(root_dir
                        , "data/file_handling_exercises"
                        , "hello_world.txt")
    read_file(hello_file)
    logger.info(f"  ------------------------------")
    missing_file = hf.build_file_name(root_dir
                        , "data/exception_handling_exercises"
                        , "missing_file.txt")
    read_file(missing_file)
    pass



#########################################################################################
def exercise_09_else_clause_testing():
    """
    Exercise 9: Else Clause
    Problem Statement:
        Write a function safe_sqrt(value) that converts user input
        to a float and calculates its square root. Use the
        try-except-else pattern so that a success message is
        printed only when no exception is raised, keeping success
        and error paths cleanly separated.
    Purpose:
        The else clause on a try block is one of Python’s less-known
        but very useful features. It keeps the “happy path” code out
        of the try block itself, which means only the risky operation
        is guarded and success logic is not accidentally shielded
        from other exceptions it might raise.
    Given Input:
        Call safe_sqrt("25") and safe_sqrt("abc").
    Expected Output:
        Success: the square root of 25.0 is 5.0
        Error: 'abc' is not a valid number.
    """
    def safe_sqrt(value):
        message = ""
        results = 0
        try:
            number_to_parse = float(value)
        except ValueError as e:
            message =  f"  Error: \"{value}\" is not a valid number."
        else:
            results = math.sqrt(number_to_parse)
            message = f"  the square root of {number_to_parse} is {results}."
        logger.info(f"  {message}")
        pass

    logger.info(f"Exercise 9: Else Clause")
    safe_sqrt("25")
    safe_sqrt("abc")
    pass



#########################################################################################
def exercise_10_nested_try_except(root_dir):
    """
    Exercise 10: Nested Try-Except
    Problem Statement:
        Write a function load_and_parse(filename, key) that opens
        a JSON file (outer try) and then looks up a key in the parsed
        data (inner try). Handle FileNotFoundError at the outer
        level and KeyError at the inner level so each failure
        is reported with an appropriate message.
    Purpose:
        Complex workflows often have multiple distinct failure points
        that require different recovery strategies. Nested try blocks
        let you apply fine-grained handling close to the source of
        each potential error, keeping the logic easier to reason about
        than a single flat block that catches everything.
    Given Input:
        A file data.json containing {"name": "Alice", "age": 30}.
        Call load_and_parse("data.json", "name"), then load_and_parse("data.json", "email"),
        then load_and_parse("missing.json", "name").
    Expected Output:
        Alice
        Error: key 'email' not found in the data.
        Error: file 'missing.json' does not exist.
    """
    def load_and_parse(filename, key):
        # open a JSON file (outer try)
        message = ""
        try:
            with open(filename) as data_file:
                data = json.load(data_file)
                # retrieve data using a key (inner try)
                try:
                    item = data[key]
                    message = item
                except KeyError as e:
                        message = f"Error: key \"{key}\" not found in the data."
        except FileNotFoundError as e:
            message = f"Error: \"{Path(filename).name}\" does not exist."
        return message
    logger.info(f"Exercise 10: Nested Try-Except")

    json_data = hf.build_file_name(root_dir
                        , "data/exception_handling_exercises"
                        , "data.json")

    missing_json_data = hf.build_file_name(root_dir
                        , "data/exception_handling_exercises"
                        , "missing.json")

    results = load_and_parse(json_data, "name")
    logger.info(f"  {results}")

    results = load_and_parse(json_data, "email")
    logger.info(f"  {results}")

    results = load_and_parse(missing_json_data, "name")
    logger.info(f"  {results}")
    pass





