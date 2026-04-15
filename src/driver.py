
import input_output_exercises.exercises as io_ex
import loop_exercises.driver as loop_exercise_driver



# https://pynative.com/python-input-and-output-exercise/#h-exercise-2-format-output-string
#
# for help with f-strings
#   https://fstring.help/cheat/
#   https://www.pythonmorsels.com/string-formatting/

def driver(src_dir):
    print("Driver - start")

    loop_driver = loop_exercise_driver.Driver()
    loop_driver.run()




    # exercise_22_check_empty_file
    if 1 == 0:
        results = loop.exercise_04_calculate_sum()
        results = loop.exercise_02_display_negative_numbers()
        results = loop.exercise_03_loop_completion_test()
        results = loop.exercise_01_print_numbers_using_while(10)

        results = io_ex.exercise_23_delete_file(src_dir)
        results = io_ex.create_text_block()
        results = io_ex.exercise_10_center_aligned_text()
        results = io_ex.exercise_11_pad_with_zeroes()
        results = io_ex.exercise_22_check_empty_file()
        #
        items_to_keep = [3]
        results = io_ex.exercise_21_read_specific_lines_from_file(items_to_keep)
        #

        results = io_ex.ex_19_write_list_to_text_file()
        results = io_ex.ex_18_read_file_store_content_in_list()
        results = io_ex.ex_20_find_number_of_lines()
        results = io_ex.ex_16_interactive_menu()
        #  issue with exercise 17... return to it later (2026-04-02)
        results = io_ex.ex_17_login_test()

        results = io_ex.ex_15_tabular_output()
        results = io_ex.ex_13_format_currency(1250500.7)
        results = io_ex.ex_09_display_right_aligned_output()
        results = io_ex.ex_08_percentage_display()
        results = io_ex.ex_06_hexadecimal_representation()
        results = io_ex.exercises_03_04_display_hex_and_octal()
        results = io_ex.exercise_12_format_string()
        results = io_ex.exercise_05_multiple_input_test()
        results = io_ex.exercise_06_write_file()
        results = io_ex.process_floats_from_user(5)
        print(results)

        myResults = io_ex.display_float_with_two_decimal_places(458.541315)
        myResults = io_ex.display_float_with_two_decimal_places(458.545001)
        myResults = io_ex.display_float_with_two_decimal_places(458.544999)
        myResults = io_ex.format_octal_print_statement(8)
        myResults = io_ex.format_octal_print_statement(42007)
        myResults = io_ex.format_print_statement()

        myResults = io_ex.exercise_01_process_two_numbers_driver(250000)
        # print(myResults)
        print("=======================================================")

    print("Driver - complete")