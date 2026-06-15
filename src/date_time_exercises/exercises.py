from src.common_library import helper_functions as hf
from datetime import datetime, date, time
import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)


#
# Exercises found at web page https://pynative.com/python-date-and-time-exercise/
# Exercises 1 through 10
#



##############################################################################
def exercise_01_print_current_date_and_time():
    """
    Exercise 1: Print Current Date and Time
    Problem Statement: Write a Python program to print the
        current date and time.
    Purpose: This exercise introduces you to Python’s datetime module
        and shows how to retrieve the current system date and time –
        a fundamental skill used in logging, scheduling, and
        timestamping data.
    Given Input:
        No input required. The program reads the current system date and time.
    Expected Output:
        Current date and time: 2025-01-15 14:23:45.123456
        (output will vary based on when the program runs)
    """
    logger.info("Exercise 1: Print Current Date and Time")
    current_date = datetime.now()
    logger.info(f"  Current date and time: {current_date}")
    pass



##############################################################################
def exercise_02_format_datetime():
    """
    Exercise 2: Format DateTime
    Problem Statement: Write a Python program to format the current date
        and time into a human-readable string using a custom format.
    Purpose: This exercise teaches you how to use strftime() to control
        the display of date and time values – an essential skill for
        generating reports, file names, log entries, and user-facing
        timestamps.
    Given Input:
        No input required. Use the current date and time.
    Expected Output:
        Formatted: 15-Jan-2025 02:23:45 PM (output will vary based on when the program runs)
    """
    logger.info("Exercise 2: Format DateTime")
    timestamp = datetime.now().strftime('%d-%b-%Y %I.%M.%S %p')
    logger.info(f"  Formatted: {timestamp}")
    pass



##############################################################################
def exercise_03_find_day_of_week():
    """
    Exercise 3: Find Day of Week
    Problem Statement: Write a Python program to find the day of
        the week for a given date.
    Purpose: This exercise shows how to extract the weekday from a date –
        useful in scheduling applications, calendar tools, and any logic
        that depends on whether a day falls on a weekday or weekend.
    Given Input:
        date = datetime(2025, 1, 15)
    Expected Output:
        Day of the week: Wednesday
    """
    logger.info("Exercise 3: Find Day of Week")
    date = datetime(2025, 1, 15)
    logger.info(f"  Day of the week: {date.strftime('%A')}")
    pass



##############################################################################
def exercise_04_convert_datetime_to_string():
    """
    Exercise 4: Convert Datetime into String
    Problem Statement: Write a Python program to convert a datetime
        object into a string representation.
    Purpose: This exercise shows how to serialize a datetime object into
        a plain string, which is needed when storing dates in text files,
        databases, JSON payloads, or sending them over APIs.
    Given Input:
        dt = datetime(2025, 6, 15, 10, 30, 45)
    Expected Output:
        DateTime as string: 2025-06-15 10:30:45
    """
    logger.info("Exercise 4: Convert Datetime into String")
    dt = datetime(2025, 6, 15, 10, 30, 45)
    logger.info(f"  DateTime as string: {dt.strftime('%Y-%m-%d %I:%M:%S')}")
    pass



##############################################################################
def exercise_05_extract_components():
    """
    Exercise 5: Extract Components
    Problem Statement: Write a program to extract the Year, Month, Day
        , Hour, Minute, and Second as separate integers from a single
        datetime object.
    Purpose: This exercise teaches you how to access individual date and
        time components from a datetime object – useful when you need to
        perform calculations, comparisons, or conditional logic on
        specific parts of a timestamp.
    Given Input:
        dt = datetime(2025, 8, 20, 14, 35, 50)
    Expected Output:
        Year: 2025
        Month: 8
        Day: 20
        Hour: 14
        Minute: 35
        Second: 50
    """
    logger.info("Exercise 5: Extract Components")
    dt = datetime(2025, 8, 20, 14, 35, 50)
    logger.info(f"  Year: {dt.year}")
    logger.info(f"  Month: {dt.month}")
    logger.info(f"  Day: {dt.day}")
    logger.info(f"  Hour: {dt.hour}")
    logger.info(f"  Minute: {dt.minute}")
    logger.info(f"  Second: {dt.second}")
    pass



##############################################################################
def exercise_06_print_time_with_am_pm():
    """
    Exercise 6: Print Time with AM/PM
    Problem Statement: Format the current time to display in a 12-hour
        format with AM/PM (e.g., “02:30 PM”).
    Purpose: This exercise shows how to present time in the 12-hour
        clock format that is standard in many user-facing applications,
        notifications, and interfaces intended for general audiences.
    Given Input:
        No input required. Use the current system time.
    Expected Output:
        Current time: 02:30 PM (output will vary based on when the program runs)
    """
    logger.info("Exercise 6: Print Time with AM/PM")
    current_time = datetime.now()
    logger.info(f"  Current time: {current_time.strftime('%I.%M %p')}")
    pass



##############################################################################
def exercise_07_print_time_in_milliseconds():
    """
    Exercise 7: Print Current Time in Milliseconds
    Problem Statement: Write a Python program to print the current
        time including milliseconds.
    Purpose: This exercise shows how to access sub-second precision from
        a datetime object – important in performance profiling, event
        logging, benchmarking, and any application where millisecond-level
        accuracy matters.
    Given Input:
        No input required. Use the current system time.
    Expected Output:
        Current time with milliseconds: 14:23:45.123 (output will vary based
        on when the program runs)
    """
    logger.info("Exercise 7: Print Current Time with milliseconds")
    current_time = datetime.now()
    logger.info(f"  Current time with milliseconds: {current_time.strftime('%I:%M:%S.%f')}")
    pass



##############################################################################
def exercise_08_get_day_of_year():
    """
    Exercise 8: Get the Day of the Year
    Problem Statement: Calculate which day of the year it is
        (from 1 to 366) for any given date.
    Purpose: This exercise demonstrates how to derive the ordinal day
        of the year from a date – a useful calculation in scientific
        data analysis, day-of-year reporting, agricultural or
        financial calendars, and countdown timers.
    Given Input:
        date = datetime(2025, 3, 15)
    Expected Output:
        Day of the year: 74
    """
    logger.info("Exercise 8: Get Day of the Year")
    date = datetime(2025, 3, 15)
    logger.info(f"  Day of the year: {date.timetuple().tm_yday}")
    pass



##############################################################################
def exercise_09_combine_date_and_time():
    """
    Exercise 9: Combine Date and Time Objects
    Problem Statement: Create a date object and a time object separately
        , then combine them into a single datetime object using
        datetime.combine().
    Purpose: This exercise shows how to work with the date and time
        types independently before merging them – a pattern commonly
        used when date and time values arrive from different sources,
        such as separate form fields or database columns.
    Given Input:
        d = date(2025, 5, 20) and t = time(9, 45, 0)
    Expected Output:
        Combined datetime: 2025-05-20 09:45:00
    """
    logger.info("Exercise 9: Combine Date and Time Objects")
    d = date(2025, 5, 20)
    t = time(9, 45, 0)
    new_date = datetime.combine(d, t)
    logger.info(f"  Combined date: {new_date}")
    pass



##############################################################################
def exercise_10_convert_string_to_datetime():
    """
    Exercise 10: Convert String Into Datetime Object
    Problem Statement: Write a Python program to convert a date
        string into a datetime object.
    Purpose: This exercise teaches you how to parse date strings
        using strptime() – a critical skill when reading dates from
        CSV files, APIs, user input, or databases where dates arrive
        as plain text and must be converted for calculations
        or comparisons.
    Given Input:
        date_string = "20 January, 2025"
    Expected Output:
        DateTime object: 2025-01-20 00:00:00
    """
    logger.info("Exercise 10: Convert String Into Datetime Object")
    date_string = "20 January, 2025"
    try:
        results = datetime.strptime(date_string, "%d %B, %Y")
        logger.info(f"  DateTime object: {results.strftime("%Y-%m-%d %H:%M:%S")}")
    except ValueError as e:
        logger.error(f"  Date String is not in correct format... {e}")
    pass





