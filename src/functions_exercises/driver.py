import functions_exercises.exercises as f1
import functions_exercises.exercises_02 as f2
#
# https://pynative.com/python-functions-exercise-with-solutions/
# Driver Program... called from main driver program
#

global global_var
global_var = 10

class Driver():

    """
    Driver Class

    Implements run function which executes multiple functions in the loop_exercises folder.

    TODO:
        Set up a dictionary to control which function gets executed and which functions get bypassed.
    """
    def __init__(self):
        pass


    def run(self):

        print()
        print("#####################################################")
        print("Functions Exercises - 1 through 10")
        print("#####################################################")

        results = f1.exercise_01_create_function_with_parameters()
        results = f1.exercise_02_variable_length_arguments()
        result = f1.exercise_03_return_multiple_values()
        result = f1.exercise_04_functions_default_argument()
        result = f1.exercise_05_inner_function_example()
        result = f1.exercise_06_recursion_addition()
        result = f1.exercise_07_assign_function_different_name()
        results = f1.exercise_08_generate_list(4, 30)
        results = f1.exercise_09_find_max_in_list()
        results = f1.exercise_10_keyword_positional_arguments()

        print()
        print("#####################################################")
        print("Functions Exercises - 11 through 18")
        print("#####################################################")
        results = f2.exercise_11_function_with_keyword_args()
        results = f2.exercise_12_modify_global_variables()
        results = f2.exercise_13_recursion_factorial()
        results = f2.exercise_14_square_number_using_lambda()
        results = f2.exercise_15_filter_list_using_lambda()
        results = f2.exercise_16_transform_list_using_lambda()
        results = f2.exercise_17_sort_complex_data_using_lambda()
        results = f2.exercise_18_pass_a_function_to_a_higher_order_function()

        pass


