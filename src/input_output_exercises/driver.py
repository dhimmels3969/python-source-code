
# from src.common_library import helper_functions as hf
import input_output_exercises.exercises as io_ex
import input_output_exercises.exercises_03 as io_ex_03

class Driver():

    """
    Driver Class

    Implements run function which executes multiple functions in the loop_exercises folder.

    TODO:
        Set up a dictionary to control which function gets executed and which functions get bypassed.
    """
    def __init__(self, root):
        # pass the root directory to the class for file operations
        self.root = root
        pass

    def run(self):
        print("#####################################################")
        print("Input Output Exercises - 1 through 10")
        print("#####################################################")


        myResults = io_ex.exercise_01_process_two_numbers_driver(250000)
        #
        myResults = io_ex.display_float_with_two_decimal_places(458.541315)
        myResults = io_ex.display_float_with_two_decimal_places(458.545001)
        myResults = io_ex.display_float_with_two_decimal_places(458.544999)
        myResults = io_ex.format_octal_print_statement(8)
        myResults = io_ex.format_octal_print_statement(42007)
        myResults = io_ex.format_print_statement()
        results = io_ex.process_floats_from_user(5)
        print(results)
        results = io_ex.exercises_03_04_display_hex_and_octal()
        results = io_ex.exercise_05_multiple_input_test()
        results = io_ex.exercise_06_write_file(self.root)
        results = io_ex.ex_06_hexadecimal_representation()
        results = io_ex.ex_08_percentage_display()
        results = io_ex.ex_09_display_right_aligned_output()

        print("#####################################################")
        print("Input Output Exercises - 11 through 20")
        print("#####################################################")

        results = io_ex.exercise_10_center_aligned_text()
        results = io_ex.exercise_11_pad_with_zeroes()
        results = io_ex.exercise_12_format_string()
        results = io_ex.ex_13_format_currency(1250500.7)
        results = io_ex.ex_15_tabular_output()
        results = io_ex.ex_16_interactive_menu()
        #  issue with exercise 17... return to it later (2026-04-02)
        # results = io_ex.ex_17_login_test()
        results = io_ex.ex_18_read_file_store_content_in_list(self.root)
        results = io_ex.ex_19_write_list_to_text_file(self.root)
        results = io_ex.ex_20_find_number_of_lines(self.root)



        print("#####################################################")
        print("Input Output Exercises - 21 through end")
        print("#####################################################")
        items_to_keep = [3]
        results = io_ex_03.exercise_21_read_specific_lines_from_file(self.root, items_to_keep)
        # #
        results = io_ex_03.create_text_block()
        results = io_ex_03.exercise_22_check_empty_file(self.root)
        results = io_ex_03.exercise_23_delete_file(self.root)

        print()
        print("#####################################################")
        print("Input Output Exercises - End of Section")
        print("#####################################################")
        print()


        pass