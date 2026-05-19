
import os
import subprocess
import platform

#
# Routines used in multiple places
#



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