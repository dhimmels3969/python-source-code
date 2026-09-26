from source_code.constants import THREE_BLANK_LINES
from source_code.common_library import helper_functions as hf
from source_code.os_and_sys_module_exercises import exercises as os_01
from source_code.os_and_sys_module_exercises import exercises_02 as os_02
from source_code.os_and_sys_module_exercises import exercises_03 as os_03

import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
#
# Exercises found at web page https://pynative.com/python-os-sys-module-exercises/
# Driver program to call all methods
#

class Driver:

    """
    Driver Class

    Implements run function which executes multiple functions in the os_and_sys_module_exercises folder.

    TODO:
        Set up a dictionary to control which function gets executed and which functions get bypassed.
    """
    def __init__(self, userInput):
        self.parms = hf.parse_kwargs(userInput)
        self._name = "OS and Sys Module Exercises"
        pass


    def run(self):
        if self.parms["run"] == "False":
            logger.info(f"Skipping the {self._name} module...\n")
        else:
            logger.info(THREE_BLANK_LINES)
            logger.info("#####################################################")
            logger.info(f"{self._name} - 1 through 10")
            logger.info("#####################################################")
            results = os_01.exercise_01_print_current_directory()
            results = os_01.exercise_02_list_directory_contents()
            results = os_01.exercise_03_create_directory()
            results = os_01.exercise_04_create_nested_directories()
            results = os_01.exercise_05_rename_file()
            results = os_01.exercise_06_delete_file()
            results = os_01.exercise_07_delete_directory_tree()
            results = os_01.exercise_08_check_if_path_exists()
            results = os_01.exercise_09_split_file_extension()
            results = os_01.exercise_10_get_file_size()

            logger.info("")
            logger.info("#####################################################")
            logger.info(f"{self._name} - 11 through 20")
            logger.info("#####################################################")
            results = os_02.exercise_11_read_environment_variable()
            results = os_02.exercise_12_set_environment_variable()
            results = os_02.exercise_13_list_environment_variables()
            results = os_02.exercise_14_get_current_process_id()
            results = os_02.exercise_15_run_shell_command()
            results = os_02.exercise_16_walk_directory_tree()
            results = os_02.exercise_17_join_paths_safely()
            results = os_02.exercise_18_get_absolute_path()
            results = os_02.exercise_19_print_python_version()
            results = os_02.exercise_20_read_command_line_arguments()

            logger.info("")
            logger.info("#####################################################")
            logger.info(f"{self._name} - 21 through 30")
            logger.info("#####################################################")
            results = os_03.exercise_21_exit_program()
            results = os_03.exercise_22_get_platform_info()
            results = os_03.exercise_23_inspect_sys_dot_path()
            results = os_03.exercise_24_add_to_sys_dot_path()
            results = os_03.exercise_25_get_recursion_limit()
            results = os_03.exercise_26_change_recursion_limit()
            results = os_03.exercise_27_script_info_logger()
            results = os_03.exercise_28_directory_size_calculator()
            results = os_03.exercise_29_environment_config_loader()
            results = os_03.exercise_30_recursive_file_finder()

            logger.info("")
            logger.info("#####################################################")
            logger.info(f"{self._name} - end")
            logger.info("#####################################################\n")

        pass