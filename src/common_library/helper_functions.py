import os
import subprocess
import platform
import calendar
from datetime import datetime
from itertools import repeat
import random
from pathlib import Path


#
# Routines used in multiple places
#



#########################################################################
####   File handling routines
#########################################################################


#########################################################################
def build_file_name(root_dir, subfolders, file_name):
    """
    This function builds a file name.
    Args:
        file_name (string): name of the file the user wants to read.
    Returns:
        a file name
    Assumption:
        The source code is in an src folder and there is a data folder at the same level
        as the src folder and the file exists in the data folder.
    """

    # Get the directory of the current source file
    try:

        # current_dir = os.path.dirname(__file__)
        current_dir = root_dir

        # Construct the path to the JSON file in the /data directory
        json_path = os.path.join(current_dir, subfolders, file_name)

        # Normalize the path (optional but recommended)
        json_path = os.path.normpath(json_path)

        # return the config information to the calling function
        return json_path
    except Exception as error:
        raise error


#########################################################################
def file_exists(file_name):
    """
    This function builds a file name.
    Args:
        file_name (string): name of the file to analyze..
    Returns:
        true if the file exists, False otherwise
    """

    # Get the directory of the current source file
    try:
        file_path = Path(file_name)
        return file_path.exists()
    except Exception as error:
        raise error



#########################################################################
####   File handling routines - Enf of Section
#########################################################################



#########################################################################
def get_positive_int_from_user(prompt):
    incomplete = True
    final_result = None
    while incomplete:
        user_number = input(prompt)
        try:
            user_number = int(user_number)
            if user_number > 0:
                incomplete = False
                final_result = user_number
            else:
                print("Number must be greater than 0. Please try again.")

        except ValueError:
            print("Previous value was invalid. Enter a number.")
    return final_result







#########################################################################
def build_dictionary(input_object):
    results_dictionary = {}
    for item in input_object:
        if item not in results_dictionary:
            results_dictionary[item] = 1
        else:
            results_dictionary[item] += 1
    return results_dictionary



#########################################################################
def is_prime(n):
    """
    Use the Sieve of Eratosthenes Algorithm to determine if a number is prime.
    :param n:
    :type n:
    :return:
    :rtype:
    """
    if n < 2:
        return False

    sieve = [True] * (n + 1)
    sieve[0] = sieve[1] = False

    for i in range(2, int(n**0.5) + 1):
        if sieve[i]:
            for j in range(i * i, n + 1, i):
                sieve[j] = False

    return sieve[n]


#########################################################################
def is_prime_number(n):
    """
    Use the Sieve of Eratosthenes Algorithm to determine if a number is prime.
    :param
        n: the number to be analyzed for primeness
    :type
        n  integer:
    :return:
        n if n is a prime number
        None otherwise
    :rtype:
        integer
    """
    if n < 2:
        return -1

    sieve = [True] * (n + 1)
    sieve[0] = sieve[1] = False

    for i in range(2, int(n**0.5) + 1):
        if sieve[i]:
            for j in range(i * i, n + 1, i):
                sieve[j] = False

    final_result = -1
    if sieve[n]:
        final_result = n
    return final_result



#########################################################################
def clear_screen():
    system = platform.system()
    try:
        subprocess.run('cls' if platform.system() == "Windows" else 'clear', shell=True)
    except Exception as e:
        print(f"An error occurred while clearing the screen: {e}")


def calculate_past_or_future_date(**kwargs):
    ########################################################
    # ----------------------------------------------------------------------------
    # initially valid kwargs are
    #	months = ##
    # ----------------------------------------------------------------------------
    # Raise an error if months not provided in **kwargs
    try:
        input_date_in = kwargs["input_date"]
    except KeyError as error:
        print(f"Required parameter [input_date] not provided. Ending program.")
        print(f"Error: {error}")
        print(f"Ending program.")
        raise error

    try:
        months_to_add_in = kwargs["months"]
    except KeyError as error:
        print(f"Required parameter [months] not provided. Ending program.")
        print(f"Error: {error}")
        print(f"Ending program.")
        raise error

    # ----------------------------------------------------------------------------
    # Calculate the number of months to add or subtract  = number_months % 12
    months_to_add = months_to_add_in % 12
    # Calculate the number of years  to add or subtract  = number_months // 12
    years_to_add = months_to_add_in // 12

    # Compare the day of the month of the base date with the number of days in the
    # month of the resolved date. If base date day of month > number of days in the
    # resolved month increment number months by 1 and set new day of month
    # equal to base date day of month - number days in the resolved month
    resolved_year = input_date_in.year + years_to_add
    resolved_month = input_date_in.month + months_to_add
    resolved_day = input_date_in.day
    if resolved_month > 12:
        resolved_year += 1
        resolved_month = resolved_month % 12
    calendar_info = calendar.monthrange(resolved_year, resolved_month)
    if input_date_in.day > calendar_info[1]:
        resolved_month += 1
        resolved_day = input_date_in.day - calendar_info[1]
    final_result = datetime(resolved_year, resolved_month, resolved_day)
    # ----------------------------------------------------------------------------
    return final_result


#########################################################################
def shuffle(list_size):
    """
    Generate a randomly shuffled list
    :param list_size:  size of the list to create
    :type list_size:   integer
    :return:           a list of integers in random order
    :rtype:            list of integers
    # TODO: allow the user to specify  the type of elements in the list.
    # TODO: do not limit it to integers.
    """
    results = list(repeat(-1, list_size))
    for i in range(0, len(results)):
        while True:
            spin = random.randint(0, len(results) - 1)
            if results[spin] == -1:
                break
        results[spin] = i
    return results
