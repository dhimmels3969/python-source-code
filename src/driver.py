
# import input_output_exercises.exercises as io_ex
from src.loop_exercises import driver as loop_exercise_driver
from src.input_output_exercises import driver as input_output_exercise_driver
from src.functions_exercises import driver as function_exercise_driver
from src.string_exercises import driver as string_exercise_driver
from src.data_structures_exercises import driver as data_structures_exercise_driver
from src.list_exercises import driver as list_exercises_driver



# https://pynative.com/python-input-and-output-exercise/#h-exercise-2-format-output-string
#
# for help with f-strings
#   https://fstring.help/cheat/
#   https://www.pythonmorsels.com/string-formatting/

def driver(src_dir):
    print("Main Driver - start")

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

    print()
    print("Main Driver - complete")