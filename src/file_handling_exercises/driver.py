
from src.common_library import helper_functions as hf
from src.file_handling_exercises import exercises as fh_01
from src.file_handling_exercises import exercises_02 as fh_02
from src.file_handling_exercises import exercises_03 as fh_03
from src.file_handling_exercises import exercises_04 as fh_04

#
# Exercises found at web page https://pynative.com/python-file-handling-exercises/
# Driver program to call all methods
#

class Driver:

    """
    Driver Class

    Implements run function which executes multiple functions in the date_time_exercises folder.

    TODO:
        Set up a dictionary to control which function gets executed and which functions get bypassed.
    """
    def __init__(self, root):
        # pass the root directory to the class for file operations
        self.root = root
        pass


    def run(self):
        print()
        print("#####################################################")
        print("File Handling Programming Exercises - 1 through 10")
        print("#####################################################")
        results = fh_01.exercise_01_write_user_name_to_file(self.root)
        results = fh_01.exercise_02_read_and_print_file(self.root)
        results = fh_01.exercise_03_read_file_line_by_line(self.root)
        results = fh_01.exercise_04_read_file_into_list(self.root)
        results = fh_01.exercise_05_append_data_to_file(self.root)
        results = fh_01.exercise_06_clear_file_content(self.root)
        results = fh_01.exercise_07_write_text_to_new_file(self.root)
        results = fh_01.exercise_08_check_if_file_exists(self.root)
        results = fh_01.exercise_09_handle_missing_file(self.root)
        results = fh_01.exercise_10_count_lines_in_file(self.root)

        print("")
        print("#####################################################")
        print("File Handling Programming Exercises - 11 through 20")
        print("#####################################################")
        results = fh_02.exercise_11_count_total_words()
        results = fh_02.exercise_12_count_total_characters()
        results = fh_02.exercise_13_count_word_occurrences()
        results = fh_02.exercise_14_read_first_n_lines()
        results = fh_02.exercise_15_read_last_n_lines()
        results = fh_02.exercise_16_read_line_numbers_from_file()
        results = fh_02.exercise_17_find_longest_word()
        results = fh_02.exercise_18_letter_frequency()
        results = fh_02.exercise_19_search_for_words_in_file()
        results = fh_02.exercise_20_strip_whitespace()

        print("")
        print("#####################################################")
        print("File Handling Programming Exercises - 21 through 30")
        print("#####################################################")
        results = fh_03.exercise_21_convert_uppercase_and_lowercase()
        results = fh_03.exercise_22_find_replace()
        results = fh_03.exercise_23_get_file_size_kilobytes()
        results = fh_03.exercise_24_copy_file_using_binary_mode()
        results = fh_03.exercise_25_rename_single_file()
        results = fh_03.exercise_26_rename_multiple_files()
        results = fh_03.exercise_27_delete_a_file()
        results = fh_03.exercise_28_merge_multiple_files()
        results = fh_03.exercise_29_reverse_line_order()
        results = fh_03.exercise_30_list_all_files()


        print("")
        print("#####################################################")
        print("File Handling Programming Exercises - 31 through 34")
        print("#####################################################")
        results = fh_04.exercise_31_read_write_binary_image_file()
        results = fh_04.exercise_32_extract_unique_words()
        results = fh_04.exercise_33_filter_log_file()
        results = fh_04.exercise_34_split_large_file()


        print("")
        print("#####################################################")
        print("Object-Oriented Programming - end")
        print("#####################################################\n")

        pass