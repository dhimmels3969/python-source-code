
# import input_output_exercises.exercises as io_ex
from src.loop_exercises import driver as loop_exercise_driver
from src.input_output_exercises import driver as input_output_exercise_driver
from src.common_library import helper_functions as hf
from src.functions_exercises import driver as function_exercise_driver
from src.string_exercises import driver as string_exercise_driver
from src.data_structures_exercises import driver as data_structures_exercise_driver
from src.list_exercises import driver as list_exercises_driver
from src.dictionary_exercises import driver as dictionary_exercises_driver
from src.set_exercises import driver as set_exercise_driver
from src.tuple_exercises import driver as tuple_exercise_driver
from src.date_time_exercises import driver as date_time_exercise_driver
from src.object_oriented_exercises import driver as object_oriented_exercise_driver
from src.file_handling_exercises import driver as file_handling_exercise_driver
from src.wordle import driver as wordle_driver
import logging

# https://pynative.com/python-input-and-output-exercise/#h-exercise-2-format-output-string
#
# for help with f-strings
#   https://fstring.help/cheat/
#   https://www.pythonmorsels.com/string-formatting/

def driver(src_dir):
    logger = logging.getLogger(__name__)
    logger.info("Start main driver.")
    EXIT_OUT_OF_LOOP = "3"
    valid_choices = ["1", "2", "3"]

    #####################################################################
    def run_wordle(root):
        word_driver = wordle_driver.Driver(root)
        word_driver.run()
    #####################################################################


    #####################################################################
    def run_code_exercises(root):
        # io_driver = input_output_exercise_driver.Driver(src_dir)
        # io_driver.run()
        #
        # loop_driver = loop_exercise_driver.Driver()
        # loop_driver.run()

        func_driver = function_exercise_driver.Driver()
        func_driver.run()

        string_driver = string_exercise_driver.Driver()
        string_driver.run()

        data_structures_driver = data_structures_exercise_driver.Driver()
        data_structures_driver.run()

        list_exercise_driver  = list_exercises_driver.Driver()
        list_exercise_driver.run()

        dict_exercises_driver = dictionary_exercises_driver.Driver()
        dict_exercises_driver.run()

        set_exercises_driver = set_exercise_driver.Driver()
        set_exercises_driver.run()

        tuple_exercises_driver = tuple_exercise_driver.Driver()
        tuple_exercises_driver.run()

        date_time_exercises_driver = date_time_exercise_driver.Driver()
        date_time_exercises_driver.run()

        object_oriented_driver = object_oriented_exercise_driver.Driver(src_dir)
        object_oriented_driver.run()

        file_handling_driver = file_handling_exercise_driver.Driver(src_dir)
        file_handling_driver.run()

        return None
    #####################################################################

    #####################################################################
    def process_valid_request(choice):
        # Fixed dictionary: Stores function references (no parentheses!)
        request_switch = {
            "1": run_wordle,
            "2": run_code_exercises
        }

        # Retrieve the function from the dictionary
        operation_function = request_switch.get(choice)
        result = operation_function(src_dir)

        pass
    #####################################################################



    #####################################################################
    def main_driver_display_menu():
        print(50*"=")
        print("1. Play Wordle")
        print("2. Execute Code Exercises")
        print("3. Exit")
        print(50*"=")
        return None
    #####################################################################



    #####################################################################
    def display_message_box(message):
        print(50*"=")
        print(message)
        print(50*"=")
        return None
    #####################################################################



    #####################################################################
    def user_chose_to_end_session(choice):
        return choice == EXIT_OUT_OF_LOOP
    #####################################################################



    #####################################################################
    def main_driver():
        # hf.clear_screen()
        exit_not_selected = True
        while exit_not_selected:
            main_driver_display_menu()
            choice = input("Enter choice (1-3): ")
            if choice not in valid_choices:
                print("Invalid Choice, please try again.")
                # main_driver_display_menu()
                continue
            else:
                if user_chose_to_end_session(choice):
                    exit_not_selected = False
                    break
                else:
                    process_valid_request(choice)
                continue
        return None
    #####################################################################


    #####################################################################
    def start_here():

        display_message_box("**********     Main Driver - start      **********")
        #  The main loop for the project starts below...
        main_driver()
        display_message_box("**********     Main Driver - complete   **********")

        return None
    #####################################################################


    start_here()
    logger.info("End main driver.")