
from src.common_library import helper_functions as hf
import list_exercises.exercises as list1
import list_exercises.exercises_02 as list2
import list_exercises.exercises_03 as list3
import list_exercises.exercises_04 as list4


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
        results = list3.exercise_21_filter_using_list_comprehension()
        results = list3.exercise_22_concatenate_lists()
        results = list3.exercise_23_iterate_lists_simultaneously()
        results = list3.exercise_24_add_items_to_list()
        results = list3.exercise_25_replace_item_in_list()
        results = list3.exercise_26_find_item_in_list()
        results = list3.exercise_27_find_most_frequent_element()
        results = list3.exercise_28_extract_elements_from_list()
        results = list3.exercise_29_is_list_palindrome()
        results = list3.exercise_30_find_common_elements()

        print("")
        print("#####################################################")
        print("List Exercises - 31 through 40")
        print("#####################################################")
        results = list4.exercise_31_filter_by_value_length()
        results = list4.exercise_32_sorted_list_check()
        results = list4.exercise_33_list_to_dictionary_conversion()
        results = list4.exercise_34_list_differences()
        results = list4.exercise_35_remove_values_in_place()
        results = list4.exercise_36_extend_nested_list()
        results = list4.exercise_37_concatenate_lists()
        results = list4.exercise_38_flatten_nested_list()
        results = list4.exercise_39_flatten_deeply_nested_lists()
        results = list4.exercise_40_calculate_cumulative_sum()

        print("")
        print("#####################################################")
        print("List Exercises - 41 through 45")
        print("#####################################################")



        print("\nLoop Exercises - end")
        pass