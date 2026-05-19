from src.common_library import helper_functions as hf


#
# Exercises found at web page https://pynative.com/python-date-and-time-exercise/
# Exercises 11 through 20
#



##############################################################################
def exercise_11_subtract_week_from_date():
    """
    Exercise 11: Subtract a Week From a Given Date
    Problem Statement: Write a Python program to subtract one week from
        a given date and print the resulting date.
    Purpose: This exercise introduces timedelta, Python’s built-in class
        for representing a duration or difference between two dates.
        Subtracting fixed intervals from dates is a common need in
        scheduling, deadline tracking, and generating historical date ranges.
    Given Input:
        date = datetime(2025, 3, 15)
    Expected Output:
        Date after subtracting one week: 2025-03-08 00:00:00
    """
    print("Exercise 11: Subtract Week From a Given Date")
    pass



##############################################################################
def exercise_12_add_week_to_date():
    """
    Exercise 12: Add Week to Given Date
    Problem Statement: Write a Python program to add one week to a
        given date and print the resulting date.
    Purpose: This exercise reinforces the use of timedelta for forward
        date arithmetic – a pattern used frequently in reminder systems,
        subscription renewals, appointment scheduling, and expiry
        date calculations.
    Given Input:
        date = datetime(2025, 3, 15)
    Expected Output:
        Date after adding one week: 2025-03-22 00:00:00
    """
    print("Exercise 12: Add Week to Given Date")
    pass



##############################################################################
def exercise_13_calculate_days_between_dates():
    """
    Exercise 13: Calculate Days Between Two Dates
    Problem Statement: Write a Python program to calculate the number
        of days between two given dates.
    Purpose: This exercise shows how to measure the elapsed time between
        two points in time – a calculation needed in age computations,
        project duration tracking, invoice due-date checks, and any
        feature that works with date ranges.
    Given Input:
        date1 = datetime(2025, 1, 1) and
        date2 = datetime(2025, 3, 15)
    Expected Output:
        Days between dates: 73
    """
    print("Exercise 13: Calculate Days Between Two Dates")
    pass



##############################################################################
def exercise_14_convert_unix_timestamp():
    """
    Exercise 14: Convert Unix Timestamp to Datetime
    Problem Statement: Given a Unix timestamp (e.g., 1672531200),
        convert it into a human-readable Python datetime object.
    Purpose: This exercise shows how to interpret Unix timestamps,
        which are integers representing the number of seconds elapsed
        since January 1, 1970 (UTC). They appear throughout APIs,
        server logs, databases, and file systems, making this
        conversion an essential real-world skill.
    Given Input:
        timestamp = 1672531200
    Expected Output:
        Datetime from timestamp: 2023-01-01 00:00:00
    """
    print("Exercise 14: Convert Unix Timestamp to Datetime")
    pass



##############################################################################
def exercise_15_get_iso_week_number():
    """
    Exercise 15: Get ISO Week Number
    Problem Statement: Find the ISO week number for a specific
        date (e.g., January 1st, 2026).
    Purpose: This exercise introduces the ISO 8601 week numbering system,
        where weeks run Monday to Sunday and the first week of the year
        is defined as the week containing the first Thursday. ISO week
        numbers are widely used in business reporting, payroll systems,
        and European calendar conventions.
    Given Input:
        date = datetime(2026, 1, 1)
    Expected Output:
        ISO week number: 1
    """
    print("Exercise 15: Get ISO Week Number")
    pass



##############################################################################
def exercise_16_subtract_hours_minutes_from_current_time():
    """
    Exercise 16: Subtract 5 Hours and 30 Minutes
    Problem Statement: Take the current time and subtract exactly 5 hours
        and 30 minutes from it using timedelta.
    Purpose: This exercise helps you practice using timedelta for time
        arithmetic, a skill essential in scheduling, time zone conversions,
        and log analysis where offsets from a reference time
        are commonly needed.
    Given Input:
        Current datetime (e.g., datetime.now())
    Expected Output:
        5 hours and 30 minutes before now: 2025-07-15 08:45:00.123456
        (actual value will vary)
    """
    print("Exercise 16: Subtract 5 Hours and 30 Minutes")
    pass



##############################################################################
def exercise_17_leap_year_check():
    """
    Exercise 17: Check for Leap Year
    Problem Statement: Write a function that takes a year as input
        and returns True if it is a leap year and False otherwise,
        using the calendar module.
    Purpose: This exercise introduces the calendar module and
        Boolean-returning functions, while reinforcing the concept of
        leap year logic used in date calculations, calendar
        applications, and scheduling systems.
    Given Input:
        year = 2024
    Expected Output:
        2024 is a leap year: True
    """
    print("Exercise 17: Check for Leap Year")
    pass



##############################################################################
def exercise_18_calculate_age_in_days():
    """
    Exercise 18: Calculate Age in Days
    Problem Statement: Input a birthdate and calculate exactly
        how many days old a person is today.
    Purpose: This exercise practices date subtraction and working with
        timedelta objects, skills used in age verification systems,
        health apps, and any application that needs to measure elapsed
        time between two dates.
    Given Input:
        birthdate = date(1995, 6, 15)
    Expected Output:
        Age in days: 10992 (actual value will vary based on today’s date)
    """
    print("Exercise 18: Calculate Age in Days")
    pass



##############################################################################
def exercise_19_difference_in_seconds():
    """
    Exercise 19: Difference in Seconds
    Problem Statement: Calculate the total number of seconds between
        two specific datetime objects.
    Purpose: This exercise teaches you to extract the total elapsed
        time in seconds from a timedelta, a technique used in performance
        benchmarking, event duration tracking, and countdown timers.
    Given Input:
        dt1 = datetime(2025, 1, 1, 9, 0, 0) and
        dt2 = datetime(2025, 1, 1, 11, 45, 30)
    Expected Output:
        Difference in seconds: 9930.0
    """
    print("Exercise 19: Difference in Seconds")
    pass



##############################################################################
def exercise_20_print_monthly_calendar():
    """
    Exercise 20: Print a Monthly Calendar
    Problem Statement: Accept a year and a month from the user and print
        a formatted text calendar for that month.
    Purpose: This exercise introduces the calendar module’s text rendering
        capabilities, useful for building CLI tools, report generators,
        and any interface that needs to display human-readable date grids.
    Given Input:
        year = 2025, month = 7
    Expected Output:
                 July 2025
            Mo Tu We Th Fr Sa Su
                1  2  3  4  5  6
             7  8  9 10 11 12 13
            14 15 16 17 18 19 20
            21 22 23 24 25 26 27
            28 29 30 31
    """
    print("Exercise 20: Print a Monthly Calendar")
    pass




