from src.common_library import helper_functions as hf


#
# Exercises found at web page https://pynative.com/python-date-and-time-exercise/
# Exercises 21 through 30
#



##############################################################################
def exercise_21_calculate_future_date():
    """
    Exercise 21: Calculate the Date 4 Months From Today
    Problem Statement: Calculate and display the date that falls
        exactly 4 months from the current date.
    Purpose: This exercise teaches month-based date arithmetic, a common
        requirement in billing cycles, subscription renewals, and
        project deadline calculations where timedelta alone is
        insufficient because months vary in length.
    Given Input:
        Current date (e.g., date.today())
    Expected Output:
        Date 4 months from today: 2025-11-15 (actual value will vary)
    """
    print("Exercise 21: Calculate the Date 4 Months From Today")
    pass



##############################################################################
def exercise_22_find_first_day_of_month():
    """
    Exercise 22: Find the First Day of the Month
    Problem Statement: For any given date, write a script to find
        the date of the first day of that specific month.
    Purpose: This exercise practices date manipulation with replace(),
        commonly used in financial reporting, monthly aggregations,
        and generating date ranges that start at the beginning of
        a billing or calendar period.
    Given Input:
        given_date = date(2025, 8, 17)
    Expected Output:
        First day of the month: 2025-08-01
    """
    print("Exercise 22: Find the First Day of the Month")
    pass



##############################################################################
def exercise_23_find_last_day_of_month():
    """
    Exercise 23: Find the Last Day of the Month
    Problem Statement: Determine the last day of the current
        month (e.g., 28, 29, 30, or 31).
    Purpose: This exercise shows how to query month-end dates
        using the calendar module, a requirement in payroll systems,
        invoice due-date calculations, and any logic that must
        handle months of varying lengths including leap year
        Februaries.
    Given Input:
        Current date (e.g., date.today())
    Expected Output:
        Last day of current month: 2025-07-31 (actual value will vary)
    """
    print("Exercise 23: Find the Last Day of the Month")
    pass



##############################################################################
def exercise_24_find_next_date():
    """
    Exercise 24: Find the Date of the Next Monday
    Problem Statement: Write a script that calculates the date of
        the upcoming Monday, regardless of what today’s date is.
    Purpose: This exercise practices weekday arithmetic using
        timedelta and weekday(), skills used in scheduling tools,
        weekly report generators, and calendar applications that
        need to align dates to specific days of the week.
    Given Input:
        Current date (e.g., date.today())
    Expected Output:
        Next Monday: 2025-07-21 (actual value will vary)
    """
    print("Exercise 24: Find the Next Monday")
    pass



##############################################################################
def exercise_25_round_time_to_nearest_hour():
    """
    Exercise 25: Round Time to the Nearest Hour
    Problem Statement: Write a program that takes a datetime object
        and rounds it to the closest full hour.
    Purpose: This exercise practices minute-based time arithmetic
        and conditional rounding logic, techniques applied in time
        series analysis, billing rounded to the nearest hour, and
        event logging systems that bucket timestamps.
    Given Input:
        dt = datetime(2025, 7, 15, 14, 35, 0)
    Expected Output:
        Rounded to nearest hour: 2025-07-15 15:00:00
    """
    print("Exercise 25: Round Time to Nearest Hour")
    pass



##############################################################################
def exercise_26_list_all_sundays():
    """
    Exercise 26: List All Sundays in a Year
    Problem Statement: Generate a list of all dates that
        fall on a Sunday for the year 2026.
    Purpose: This exercise practices iterating over a date range and
        filtering by weekday, a technique used in scheduling systems,
        retail planning, and any application that needs to enumerate
        specific days across a calendar year.
    Given Input:
        year = 2026
    Expected Output:
        A list of all 52 Sunday dates in 2026, starting with 2026-01-04 and ending with 2026-12-27.
    """
    print("Exercise 26: List All Sundays in a Year")
    pass



##############################################################################
def exercise_27_calculate_working_days_between_dates():
    """
    Exercise 27: Calculate Business Days Between Two Dates
    Problem Statement: Calculate the number of days between
        two dates, excluding Saturdays and Sundays.
    Purpose: This exercise teaches weekday filtering over a date
        range, an essential skill in HR systems, project management
        tools, SLA tracking, and financial applications where
        only working days count toward deadlines.
    Given Input:
        start = date(2025, 7, 1) and
        end = date(2025, 7, 31)
    Expected Output:
        Business days between 2025-07-01 and 2025-07-31: 23
    """
    print("Exercise 27: Calculate Working Days Between Two Dates")
    pass



##############################################################################
def exercise_28_convert_local_time_to_utc():
    """
    Exercise 28: Convert Local Time to UTC
    Problem Statement: Take a local datetime object and convert it
        to Coordinated Universal Time (UTC).
    Purpose: This exercise introduces timezone-aware datetime
        objects and UTC conversion, a foundational skill for building
        globally distributed applications, APIs, databases, and any
        system that stores or transmits timestamps across time zones.
    Given Input:
        A naive local datetime representing IST (UTC+5:30), e.g., datetime(2025, 7, 15, 10, 30, 0)
    Expected Output:
        Local (IST): 2025-07-15 10:30:00+05:30 and UTC: 2025-07-15 05:00:00+00:00
    """
    print("Exercise 28: Convert Local Time to UTC")
    pass



##############################################################################
def exercise_29_current_time_by_city():
    """
    Exercise 29: Get Current Time in a Specific City
    Problem Statement: Use the zoneinfo (or pytz) library to print the
        current time in “Asia/Tokyo” and “America/New_York”.
    Purpose: This exercise demonstrates how to retrieve and display the current
        time across multiple time zones simultaneously, a core requirement in
        world clocks, international meeting schedulers, trading dashboards,
        and global customer support tools.
    Given Input:
        No input required. Uses datetime.now() with a timezone argument.
    Expected Output:
        Current times in both cities, formatted clearly
        (actual values will vary by when the program is run).
    """
    print("Exercise 29: Get Current Time in a Specific City")
    pass



##############################################################################
def exercise_30_working_days_check():
    """
    Exercise 30: Calculate Date After N Working Days
    Problem Statement: Given a start date, find the date that occurs
        after 10 working days, skipping weekends.
    Purpose: This exercise combines weekday checking with iterative
        date advancement, a pattern used in contract management, delivery
        estimation, legal deadline calculators, and any workflow
        where turnaround times are measured in business days rather
        than calendar days.
    Given Input:
        start_date = date(2025, 7, 1) and n = 10
    Expected Output:
        Date after 10 working days from 2025-07-01: 2025-07-15
    """
    print("Exercise 30: Calculate Date After N Working Days")
    pass




