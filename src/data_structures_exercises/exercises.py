from src.common_library import helper_functions as hf
import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)


#
# Exercises found at web page https://pynative.com/python-data-structure-exercise-for-beginners/
# Exercises 1 through 10
#



#######################################################################################################
def exercise_01_build_output_list_from_two_input_lists():
    """
    Exercise 1: List Creation using two lists
    Write a code to create a new list using odd-indexed elements from the
        first list and even-indexed elements from the second
    Given two lists, l1 and l2, write a program to create a third list
        l3 by picking an odd-index element from the list l1 and even index elements from the list l2.
    Given:
        l1 = [3, 6, 9, 12, 15, 18, 21]
        l2 = [4, 8, 12, 16, 20, 24, 28]
    Expected Output:
        Element at odd-index positions from list one
        [6, 12, 18]
        Element at even-index positions from list two
        [4, 12, 20, 28]
        Printing Final third list
        [6, 12, 18, 4, 12, 20, 28]
    """
    logger.info("Exercise 1: List Creation using two lists")
    l1 = [3, 6, 9, 12, 15, 18, 21]
    l2 = [4, 8, 12, 16, 20, 24, 28]
    l1_odds = l1[1::2]
    l2_evens = l2[0::2]
    output_list = l1_odds + l2_evens
    logger.info(f"  Element at odd-index positions from list one  {l1_odds}")
    logger.info(f"  Element at even-index positions from list two  {l2_evens}")
    logger.info(f"  Printing Final third list  {output_list}")
    pass



#######################################################################################################
def exercise_02_add_to_remove_from_list():
    """
    Exercise 2: Remove and add item in a list
    Write a program to remove the item present at index 4
        and add it to the 2nd position and at the end of the list.
    Given:
        list1 = [54, 44, 27, 79, 91, 41]
    Expected Output:
        List After removing element at index 4  [34, 54, 67, 89, 43, 94]
        List after Adding element at index 2  [34, 54, 11, 67, 89, 43, 94]
        List after Adding element at last  [34, 54, 11, 67, 89, 43, 94, 11]
    """
    logger.info("Exercise 2: Remove and add item in a list")
    # list1 = [54, 44, 27, 79, 91, 41]
    list1 = [34, 54, 67, 89, 11, 43, 94]
    item_to_remove = list1[4]
    list1.remove(item_to_remove)
    logger.info(f"  List After removing element at index 4  {list1}")
    list1.insert(2, item_to_remove)
    logger.info(f"  List After adding element at index 2  {list1}")
    list1.append(item_to_remove)
    logger.info(f"  List After adding element at last  {list1}")
    pass



#######################################################################################################
def exercise_03_slice_list():
    """
    Exercise 3: Slice list into 3 equal chunks and reverse each chunk
    Given:
        sample_list = [11, 45, 8, 23, 14, 12, 78, 45, 89]
    Expected Outcome:
        Chunk  1 [11, 45, 8]
        After reversing it  [8, 45, 11]
        Chunk  2 [23, 14, 12]
        After reversing it  [12, 14, 23]
        Chunk  3 [78, 45, 89]
        After reversing it  [89, 45, 78]
    """
    logger.info("Exercise 3: Slice list into 3 equal chunks and reverse each chunk")
    sample_list = [11, 45, 8, 23, 14, 12, 78, 45, 89]
    sample_size = len(sample_list) // 3
    offset = 0
    chunk_list = []
    for i in range(sample_size):
        chunk_list.append(sample_list[offset:offset + (sample_size)])
        offset += sample_size
    # display the results...
    for i in range(len(chunk_list)):
        item = chunk_list[i]
        logger.info(f"  Chunk {i + 1} : {item}")
        logger.info(f"  After reversing it  {item[::-1]}")
    pass



#######################################################################################################
def exercise_04_count_occurrences():
    """
    Exercise 4: Count the occurrence of each element from a list
    Write a program to iterate a given list and count the occurrence
        of each element and create a dictionary to show the count of each element.
    Given:
        sample_list = [11, 45, 8, 11, 23, 45, 23, 45, 89]
    Expected Output:
        Printing count of each item   {11: 2, 45: 3, 8: 1, 23: 2, 89: 1}
    """
    logger.info("Exercise 4: Count the occurrence of each element from a list")
    sample_list = [11, 45, 8, 11, 23, 45, 23, 45, 89]
    results_dictionary = hf.build_dictionary(sample_list)
    message = f"Printing count of each item  {results_dictionary}"
    logger.info(f"  {message}")
    pass



#######################################################################################################
def exercise_05_build_swt_from_paired_elements():
    """
    Exercise 5: Paired Elements from Two Lists as a Set
    Write a code to create a Python set such that it shows
        the element from both lists in a pair.
    Given:
        first_list = [2, 3, 4, 5, 6, 7, 8]
        second_list = [4, 9, 16, 25, 36, 49, 64]
    Expected Output:
        Result is  {(6, 36), (8, 64), (4, 16), (5, 25), (3, 9), (7, 49), (2, 4)}
    """
    logger.info("Exercise 5: Paired Elements from Two Lists as a Set")
    first_list = [2, 3, 4, 5, 6, 7, 8]
    second_list = [4, 9, 16, 25, 36, 49, 64]
    resultset = set(zip(first_list, second_list))
    message = f"Result is  {sorted(resultset)}"
    logger.info(f"  {message}")
    pass



#######################################################################################################
def exercise_06_set_intersection_and_removal():
    """
    Exercise 6: Set Intersection and Removal
    Write a code to find the intersection (common) of two sets
        and remove those elements from the first set.
    Given:
        first_set = {23, 42, 65, 57, 78, 83, 29}
        second_set = {57, 83, 29, 67, 73, 43, 48}
    Expected Output:
        Intersection is  {57, 83, 29}
        First Set after removing common element  {65, 42, 78, 23}
    """
    logger.info("Exercise 6: Set Intersection and Removal")
    first_set = {23, 42, 65, 57, 78, 83, 29}
    second_set = {57, 83, 29, 67, 73, 43, 48}
    third_set = first_set & second_set
    logger.info(f"  Intersection is  {third_set}")
    # remove the common elements (stored in third set) from the first set.
    for item in third_set:
        first_set.remove(item)
    logger.info(f"  First set after removing common element  {first_set}")
    pass



#######################################################################################################
def exercise_07_subset_superset_test():
    """
    Exercise 7: Subset or Superset of another set
    Write a code to checks if one set is a subset or superset
        of another set. If found, delete all elements from that set.
    Given:
        first_set = {27, 43, 34}
        second_set = {34, 93, 22, 27, 43, 53, 48}
    Expected Output:
        First set is subset of second set - True
        Second set is subset of First set -  False

        First set is Super set of second set -  False
        Second set is Super set of First set -  True

        First Set  set()
        Second Set  {67, 73, 43, 48, 83, 57, 29}
    """
    logger.info("Exercise 7: Subset or Superset of another set")
    first_set = {27, 43, 34}
    second_set = {34, 93, 22, 27, 43, 53, 48}
    # perform tests...
    s1_subset_of_s2 = first_set.issubset(second_set)
    s1_superset_of_s2 = first_set.issuperset(second_set)
    s2_subset_of_s1 = second_set.issubset(first_set)
    s2_superset_of_s1 = second_set.issuperset(first_set)
    # print results...
    logger.info(f"  First set is subset of second set - {s1_subset_of_s2}")
    logger.info(f"  Second set is subset of First set - {s2_subset_of_s1}")
    logger.info(f"  First set is Super set of second set - {s1_superset_of_s2}")
    logger.info(f"  Second set is Super set of First set - {s2_superset_of_s1}")

    if s1_subset_of_s2 or s2_superset_of_s1:
        first_set.clear()
    logger.info(f"  First set  {first_set}")
    logger.info(f"  Second set  {second_set}")
    pass



#######################################################################################################
def exercise_08_filter_list_against_dictionary():
    """
    Exercise 8: Filter List Against Dictionary Values
    Write a program to iterate a given list and check if a
        given element exists as a key’s value in a dictionary.
        If not, delete it from the list
    Given:
        roll_number = [47, 64, 69, 37, 76, 83, 95, 97]
        sample_dict = {'Jhon':47, 'Emma':69, 'Kelly':76, 'Jason':97}
    Expected Outcome:
        After removing unwanted elements from list [47, 69, 76, 97]
    """
    logger.info("Exercise 8: Filter List Against Dictionary")
    roll_number = [47, 64, 69, 37, 76, 83, 95, 97]
    sample_dict = {'Jhon': 47, 'Emma': 69, 'Kelly': 76, 'Jason': 97}

    #######################################################################################
    # create new list (from pyNative website
    # roll_number[:] = [item for item in roll_number if item in sample_dict.values()]
    #######################################################################################

    for i in range(len(roll_number) - 1, 0, -1):
        if roll_number[i] not in sample_dict.values():
            roll_number.remove(roll_number[i])
    logger.info(f"  After removing unwanted elements from list {roll_number}")
    pass



#######################################################################################################
def exercise_09_unique_dictionary_values():
    """
    Exercise 9: Extract Unique Dictionary Values to List
    Write a code to get all values from the dictionary
        and add them to a list but don’t add duplicates
    Given
    speed = {'jan': 47, 'feb': 52, 'march': 47, 'April': 44, 'May': 52, 'June': 53, 'july': 54, 'Aug': 44, 'Sept': 54}
    Expected Outcome:
        [47, 52, 44, 53, 54]
    """
    logger.info("Exercise 9: Unique Dictionary Values to List")
    speed = {'jan': 47, 'feb': 52, 'march': 47, 'April': 44, 'May': 52, 'June': 53, 'july': 54, 'Aug': 44, 'Sept': 54}
    final_results = []

    for value in speed.values():
        if value not in final_results:
            final_results.append(value)
    logger.info(f"  Unique List: {final_results}")
    pass



#######################################################################################################
def exercise_10_remove_duplicates_from_list():
    """
    Exercise 10: remove duplicates from a list
    Write a code to remove duplicates from a list and create
        a tuple and find the minimum and maximum number
    Given:
        sample_list = [87, 45, 41, 65, 94, 41, 99, 94]
    Expected Outcome:
        unique items [87, 45, 41, 65, 99]
        tuple (87, 45, 41, 65, 99)
        min: 41
        max: 99
    """
    logger.info("Exercise 10: Remove Duplicates from a list")
    sample_list = [87, 45, 41, 65, 94, 41, 99, 94]
    unique_list = []
    for item in sample_list:
        if item not in unique_list:
            unique_list.append(item)
    unique_set = tuple(unique_list)
    unique_set_min = min(unique_set)
    unique_set_max = max(unique_set)
    logger.info(f"  Unique Items: {unique_list}")
    logger.info(f"  tuple: {unique_set}")
    logger.info(f"  min: {unique_set_min}")
    logger.info(f"  max: {unique_set_max}")
    pass



