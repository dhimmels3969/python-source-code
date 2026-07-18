import date_time_exercises.exercises
from src.common_library import helper_functions as hf
from src.date_time_exercises import exercises as dt_01
from src.date_time_exercises import exercises_02 as dt_02
from src.date_time_exercises import exercises_03 as dt_03
import constants
import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

#
# Exercises found at web page https://pynative.com/python-date-and-time-exercise/
#


class Driver():

    """
    Driver Class

    Implements run function which executes multiple functions in the date_time_exercises folder.

    TODO:
        Set up a dictionary to control which function gets executed and which functions get bypassed.
    """
    def __init__(self, userInput):
        self.parms = hf.parse_kwargs(userInput)
        self._name = "Date Time Exercises"
        pass

    def run(self):
        if self.parms["run"] == "False":
            logger.info(f"Skipping the {self._name} module...\n")
        else:
            logger.info(constants.THREE_BLANK_LINES)
            logger.info("#####################################################")
            logger.info(f"{self._name} - 1 through 10")
            logger.info("#####################################################")
            results = dt_01.exercise_01_print_current_date_and_time()
            results = dt_01.exercise_02_format_datetime()
            results = dt_01.exercise_03_find_day_of_week()
            results = dt_01.exercise_04_convert_datetime_to_string()
            results = dt_01.exercise_05_extract_components()
            results = dt_01.exercise_06_print_time_with_am_pm()
            results = dt_01.exercise_07_print_time_in_milliseconds()
            results = dt_01.exercise_08_get_day_of_year()
            results = dt_01.exercise_09_combine_date_and_time()
            results = dt_01.exercise_10_convert_string_to_datetime()
    
    
    
    
            logger.info("")
            logger.info("#####################################################")
            logger.info(f"{self._name} - 11 through 20")
            logger.info("#####################################################")
            results = dt_02.exercise_11_subtract_week_from_date()
            results = dt_02.exercise_12_add_week_to_date()
            results = dt_02.exercise_13_calculate_days_between_dates()
            results = dt_02.exercise_14_convert_unix_timestamp()
            results = dt_02.exercise_15_get_iso_week_number()
            results = dt_02.exercise_16_subtract_hours_minutes_from_current_time()
            results = dt_02.exercise_17_leap_year_check()
            results = dt_02.exercise_18_calculate_age_in_days()
            results = dt_02.exercise_19_difference_in_seconds()
            results = dt_02.exercise_20_print_monthly_calendar()
    
    
            logger.info("")
            logger.info("#####################################################")
            logger.info(f"{self._name} - 21 through 30")
            logger.info("#####################################################")
            results = dt_03.exercise_21_calculate_future_date()
            results = dt_03.exercise_22_find_first_day_of_month()
            results = dt_03.exercise_23_find_last_day_of_month()
            results = dt_03.exercise_24_find_next_date()
            results = dt_03.exercise_25_round_time_to_nearest_hour()
            results = dt_03.exercise_26_list_all_sundays()
            results = dt_03.exercise_27_calculate_working_days_between_dates()
            results = dt_03.exercise_28_convert_local_time_to_utc()
            # results = dt_03.exercise_29_current_time_by_city()
            results = dt_03.exercise_29_current_time_by_city_pynative_solution()
            results = dt_03.exercise_30_working_days_check()
    
            logger.info("#####################################################")
            logger.info(f"{self._name} - end")
            logger.info("#####################################################")

        pass