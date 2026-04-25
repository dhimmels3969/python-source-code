
# import input_output_exercises.exercises as io_ex
import loop_exercises.driver as loop_exercise_driver
import input_output_exercises.driver as input_output_exercise_driver
import functions_exercises.driver as function_exercise_driver
import string_exercises.driver as string_exercise_driver



# https://pynative.com/python-input-and-output-exercise/#h-exercise-2-format-output-string
#
# for help with f-strings
#   https://fstring.help/cheat/
#   https://www.pythonmorsels.com/string-formatting/

def driver(src_dir):
    print("Driver - start")

    string_driver = string_exercise_driver.Driver()
    string_driver.run()

    func_driver = function_exercise_driver.Driver()
    func_driver.run()

    # io_driver = input_output_exercise_driver.Driver(src_dir)
    # io_driver.run()
    #
    # loop_driver = loop_exercise_driver.Driver()
    # loop_driver.run()

    print("Driver - complete")