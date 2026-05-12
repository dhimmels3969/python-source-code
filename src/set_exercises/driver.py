from src.common_library import helper_functions as hf
from src.set_exercises import exercises as set1
from src.set_exercises import exercises_02 as set2
from src.set_exercises import exercises_03 as set3

#
# Exercises found at web page https://pynative.com/python-set-exercise-with-solutions/>
#

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
        print()
        print("#####################################################")
        print("Set Exercises - 1 through 10")
        print("#####################################################")
        results = set1.exercise_01_basic_set_operations()
        results = set1.exercise_02_clear_all_elements()
        results = set1.exercise_03_find_set_length()
        results = set1.exercise_04_empty_set_check()
        results = set1.exercise_05_union_of_sets()
        results = set1.exercise_06_set_intersection_check()
        results = set1.exercise_07_sets_difference_check()
        results = set1.exercise_08_symmetric_difference()
        results = set1.exercise_09_find_min_max()
        results = set1.exercise_10_sum_elements()


        print("")
        print("#####################################################")
        print("Set Exercises - 11 through 20")
        print("#####################################################")
        results = set2.exercise_11_add_elements()
        results = set2.exercise_12_update_with_multiple_iterables()
        results = set2.exercise_13_subset_superset_check()
        results = set2.exercise_14_disjoint_check()
        results = set2.exercise_15_difference_update()
        results = set2.exercise_16_intersection_update()
        results = set2.exercise_17_symmetric_difference_update()
        results = set2.exercise_18_remove_items()
        results = set2.exercise_19_pop_elements()
        results = set2.exercise_20_filter_set()

        print("")
        print("#####################################################")
        print("Set Exercises - 21 through 31")
        print("#####################################################")
        results = set3.exercise_21_common_elements_check()
        results = set3.exercise_22_count_unique_words()
        results = set3.exercise_23_convert_to_joined_string()
        results = set3.exercise_24_proper_subset_superset()
        results = set3.exercise_25_frozenset_check()
        results = set3.exercise_26_set_comprehension()
        results = set3.exercise_27_remove_duplicates_preserve_order()
        results = set3.exercise_28_multiset_difference()
        results = set3.exercise_29_tuples_test()
        results = set3.exercise_30_shallow_copy_test()
        results = set3.exercise_31_test_performance()
        print("#####################################################")
        print("Set Exercises - end")
        print("#####################################################\n")

        pass