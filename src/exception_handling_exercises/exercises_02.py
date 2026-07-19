import logging

#
# https://pynative.com/python-exception-handling-exercises/
# Exercises 11 through 20
#


logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)



#########################################################################################
def exercise_11_reraising_exceptions_test():
    """
    Exercise 11: Re-raising Exceptions
    Problem Statement: Write a function process_data(value) that converts
        a string to an integer. Catch any ValueError, log a message to
        the console, and then re-raise the same exception so the calling
        code can handle it at a higher level.
    Purpose: Catching an exception purely to re-raise it is a common
        pattern in layered applications. A lower-level function may need
        to record a log entry or clean up state without fully swallowing
        the error, while still allowing the caller to decide how to
        respond. This exercise shows exactly how to do that with a
        bare raise statement.
    Given Input:
        Call process_data("abc") from a wrapping try block in the main code.
    Expected Output:
        [log] process_data failed: invalid literal for int() with base 10: 'abc'
        [main] Caught re-raised exception: invalid literal for int() with base 10: 'abc'
    """
    logger.info("Exercise 11: Re-raising Exceptions")
    pass



#########################################################################################
def exercise_12_custom_exception_class():
    """
    Exercise 12: Custom Exception Class
    Problem Statement:
        Define a custom exception class InsufficientFundsError.
        Then create a BankAccount class with a withdraw(amount) method
        that raises InsufficientFundsError when the withdrawal
        amount exceeds the current balance. Handle the exception
        in the calling code.
    Purpose:
        Built-in exceptions are generic. Custom exceptions make
        your code self-documenting and allow callers to catch exactly
        the error your library or class can produce, without
        accidentally catching unrelated errors of the same
        built-in type. This pattern is standard in professional
        Python packages and frameworks.
    Given Input:
        Create a BankAccount with a balance of 100. Try to withdraw 150.
    Expected Output:
        Error: Cannot withdraw 150. Available balance: 100.
    """
    logger.info("Exercise 12: Custom Exception Class")
    pass



#########################################################################################
def exercise_13_exception_chaining():
    """
    Exercise 13: Exception Chaining
    Problem Statement:
        Write a function load_config(filename) that reads a JSON
        config file. If the file is missing, catch the FileNotFoundError
        and raise a higher-level ConfigurationError using raise
        ConfigurationError(...) from original_exception to preserve
        the original cause in the chain.
    Purpose:
        Exception chaining lets you translate low-level technical errors
        into meaningful domain-level errors without discarding the debugging
        context. A caller that receives a ConfigurationError knows exactly
        what went wrong in business terms, while the full original
        traceback is still accessible via __cause__ for developers who
        need it.
    Given Input:
        Call load_config("config.json") when the file does not exist.
    Expected Output:
        ConfigurationError: Could not load config file 'config.json'.
        Caused by: [Errno 2] No such file or directory: 'config.json'
    """
    logger.info("Exercise 13: Exception Chaining")
    pass



#########################################################################################
def exercise_14_validate_user_input():
    """
    Exercise 14: Validate User Input Loop
    Problem Statement:
        Write a program that repeatedly prompts the user to enter
        a positive integer. If the input is not a valid integer or
        is not positive, catch the exception or condition, display
        an error message, and ask again. The loop should only exit
        when valid input is received.
    Purpose:
        Real applications rarely get clean input on the first
        attempt. This exercise combines exception handling with
        a control loop to build a robust input routine – a pattern
        found in CLI tools, configuration wizards, and any
        program that interacts directly with a human user.
    Given Input:
        The user types abc, then -5, then 7 across three prompts.
    Expected Output:
        Enter a positive integer: abc
        Error: 'abc' is not a valid integer. Try again.
        Enter a positive integer: -5
        Error: -5 is not positive. Try again.
        Enter a positive integer: 7
        You entered: 7
    """
    logger.info("Exercise 14: Validate User Input Loop")
    pass



#########################################################################################
def exercise_15_context_manager_exception_test():
    """
    Exercise 15: Context Manager with Exceptions
    Problem Statement:
        Implement a custom context manager class SuppressError
        using __enter__ and __exit__ that silently suppresses
        a specific exception type passed at construction time.
        Demonstrate it suppressing a ValueError while letting a
        TypeError propagate normally.
    Purpose:
        Understanding what happens inside a with statement
        unlocks a powerful Python design pattern. Context
        managers are used everywhere – in file handling, database
        transactions, threading locks, and test frameworks. Knowing
        how __exit__ controls exception propagation lets you build
        your own resource-management and error-suppression
        utilities.
    Given Input:
        Use SuppressError(ValueError) as a context manager
        around a block that raises ValueError, then demonstrate
        that a TypeError raised inside a second block is
        not suppressed.
    Expected Output:
        Entering context...
        ValueError suppressed.
        Outside context - execution continued.
        Entering context...
        TypeError: unsupported operand type(s) for +: 'int' and 'str'
    """
    logger.info("Exercise 15: Context Manager with Exceptions")
    pass



#########################################################################################
def exercise_16_exception_hierarchy():
    """
    Exercise 16: Exception Hierarchy
    Problem Statement:
        Define a three-level exception hierarchy: AppError as the base,
        DatabaseError inheriting from it, and ConnectionError inheriting
        from DatabaseError. Raise a ConnectionError and show that
        catching DatabaseError or AppError also intercepts it, while
        catching an unrelated exception type does not.
    Purpose:
        Exception hierarchies are the backbone of professional Python
        library design. They let users of your code choose how broadly
        or narrowly to catch errors. A caller that wants to handle
        all database problems catches DatabaseError; one that wants
        only connectivity failures catches ConnectionError. This
        exercise makes that mechanism concrete.
    Given Input:
        Raise ConnectionError("host unreachable") and catch it
        three times – once with each level of the hierarchy – to
        show that all three work.
    Expected Output:
        Caught as ConnectionError: host unreachable
        Caught as DatabaseError: host unreachable
        Caught as AppError: host unreachable
    """
    logger.info("Exercise 16: Exception Hierarchy")
    pass



#########################################################################################
def exercise_17_logging_exceptions_test():
    """
    Exercise 17: Logging Exceptions
    Problem Statement:
        Configure Python’s logging module to write to a file called
        app.log. Write a function divide(a, b) that catches a
        ZeroDivisionError and uses logging.exception() to record
        the full traceback to the log file before returning None.
    Purpose:
        Printing errors to the console is fine for learning, but
        production code needs persistent, structured logs. Python’s
        built-in logging module provides log levels, file rotation,
        formatters, and – crucially – the ability to capture full
        tracebacks automatically. This exercise builds the habit of
        logging exceptions properly from the start.
    Given Input:
        Call divide(10, 0).
    Expected Output:
        Console: divide(10, 0) returned None
        app.log: ERROR:root:Division failed - ZeroDivisionError with full traceback
    """
    logger.info("Exercise 17: Logging Exceptions")
    pass



#########################################################################################
def exercise_18_retry_decorator():
    """
    Exercise 18: Retry Decorator
    Problem Statement:
        Write a @retry(times=3) decorator factory that re-runs the
        decorated function up to times attempts if it raises an
        exception. If all attempts fail, re-raise the last exception.
        Demonstrate it on a function that fails twice and succeeds
        on the third call.
    Purpose:
        Transient failures – network timeouts, temporary service
        unavailability, rate-limit responses – are a fact of life in
        distributed systems. A retry decorator is one of the most
        reused tools in a Python developer’s toolkit. Building it
        from scratch cements understanding of decorators, closures,
        and exception handling all at once.
    Given Input:
        A function flaky_call() that fails on the first two calls
        and succeeds on the third.
    Expected Output:
        Attempt 1 failed: temporary failure
        Attempt 2 failed: temporary failure
        Attempt 3 succeeded.
        Result: success
    """
    logger.info("Exercise 18: Retry Decorator")
    pass



#########################################################################################
def exercise_19_thread_safe_exception_handling():
    """
    Exercise 19: Thread-Safe Exception Handling
    Problem Statement:
        Launch five threads that each perform a division. Some will
        raise a ZeroDivisionError. Catch exceptions inside each
        thread and store them in a shared list protected by a
        threading.Lock. After all threads complete, iterate the
        list and report all failures.
    Purpose:
        Exceptions raised in a thread do not propagate to the
        main thread automatically – they simply terminate the
        thread silently unless you handle them explicitly. This
        exercise teaches the correct pattern for capturing
        and surfacing thread-level errors in concurrent
        Python programs.
    Given Input:
        Five threads dividing 10 by the values [2, 0, 5, 0, 1].
    Expected Output:
        Thread-1: 10 / 2 = 5.0
        Thread-3: 10 / 5 = 2.0
        Thread-5: 10 / 1 = 10.0
        Errors collected:
        Thread-2: division by zero
        Thread-4: division by zero
    """
    logger.info("Exercise 19: Thread-Safe Exception Handling")
    pass



#########################################################################################
def exercise_20_generator_exception_test():
    """
    Exercise 20: Exception in Generator
    Problem Statement:
        Write a generator function file_lines(filename) that yields lines
        from a file one at a time, handles IOError gracefully if the file
        cannot be opened, and supports receiving injected exceptions from
        outside using generator.throw(). Demonstrate injecting a RuntimeError
         mid-iteration to cancel reading early.
    Purpose:
        Generators are lazy pipelines, and like any pipeline they need to
        handle both internal errors (bad file) and external signals
        (cancel this operation). The throw() method is the standard way to
        push an exception into a running generator, and understanding it
        is essential for building cooperative async-style systems and robust
        data pipelines.
    Given Input:
        A file sample.txt with three lines. Yield the first line normally,
        then inject a RuntimeError before the second line is yielded.
    Expected Output:
        Line 1: Hello from line 1
        Generator cancelled: operation aborted
        Done.
    """
    logger.info("Exercise 20: Exception in Generator")
    pass





