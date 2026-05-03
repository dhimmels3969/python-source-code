
from src.common_library import helper_functions as hf
import list_exercises.exercises as list1
import list_exercises.exercises_02 as list2


class Driver():

    """
    Driver Class

    Implements run function which executes multiple functions in the list_exercises folder.

    TODO:
        Set up a dictionary to control which function gets executed and which functions get bypassed.
    """
    def __init__(self):
        pass

    def run(self):
        print("#####################################################")
        print("List Exercises - 1 through 10")
        print("#####################################################")
        results = list1.exercise_01_basic_list_operations()
        results = list1.exercise_02_perform_list_manipulation()
        results = list1.exercise_03_calculate_stats()
        results = list1.exercise_04_find_min_and_max()
        results = list1.exercise_05_calculate_product()
        results = list1.exercise_06_count_evens_and_odds()
        results = list1.exercise_07_reverse_a_list()
        results = list1.exercise_08_sort_list_of_numbers()
        results = list1.exercise_09_create_copy_of_list()
        results = list1.exercise_10_combine_two_lists()


        print("")
        print("#####################################################")
        print("List Exercises - 11 through 20")
        print("#####################################################")
        results = list2.exercise_11_list_slicing()
        results = list2.exercise_12_swap_elements_in_list()
        results = list2.exercise_13_access_nested_lists()
        results = list2.exercise_14_check_for_specific_item()
        results = list2.exercise_15_find_longest_string_in_list()
        results = list2.exercise_16_transform_each_item_in_list()
        results = list2.exercise_17_count_occurrences()
        results = list2.exercise_18_remove_all_occurrences()
        results = list2.exercise_19_remove_empty_strings()
        results = list2.exercise_20_remove_duplicates_from_list()

        print("")
        print("#####################################################")
        print("List Exercises - 21 through 30")
        print("#####################################################")


        print("")
        print("#####################################################")
        print("List Exercises - 31 through 40")
        print("#####################################################")


        print("")
        print("#####################################################")
        print("List Exercises - 41 through 45")
        print("#####################################################")



        print("\nLoop Exercises - end")
        pass