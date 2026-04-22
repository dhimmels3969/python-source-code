
import os

#
# Routines used in multiple places
#

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