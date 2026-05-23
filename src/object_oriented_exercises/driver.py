import date_time_exercises.exercises
from src.common_library import helper_functions as hf
from src.object_oriented_exercises import exercises as oop_01
from src.object_oriented_exercises import exercises_02 as oop_02
from src.object_oriented_exercises import exercises_03 as oop_03

#
# Exercises found at web page https://pynative.com/python-object-oriented-programming-oop-exercise/
#


class Driver():

    """
    Driver Class

    Implements run function which executes multiple functions in the date_time_exercises folder.

    TODO:
        Set up a dictionary to control which function gets executed and which functions get bypassed.
    """
    def __init__(self):
        pass

    def run(self):
        print()
        print("#####################################################")
        print("Object-Oriented Programming Exercises - 1 through 10")
        print("#####################################################")
        results = oop_01.exercise_01_empty_class()
        results = oop_01.exercise_02_class_with_instance_attributes()
        results = oop_01.exercise_03_rectangle_class()
        results = oop_01.exercise_04_student_class_average_grade()
        results = oop_01.exercise_05_product_class()
        results = oop_01.exercise_06_bank_account_overdraft_protection()
        results = oop_01.exercise_07_light_class_state_toggle()
        results = oop_01.exercise_08_user_account_password_protection()
        results = oop_01.exercise_09_temperature_class()
        results = oop_01.exercise_10_notebook_class_display_notes()

        print("")
        print("#####################################################")
        print("Object-Oriented Programming - 11 through 20")
        print("#####################################################")
        results = oop_02.exercise_11_coffee_machine_class()
        results = oop_02.exercise_12_shared_class_attribures()
        results = oop_02.exercise_13_subclass_inheritance()
        results = oop_02.exercise_14_override_parent_method()
        results = oop_02.exercise_15_extend_child_class()
        results = oop_02.exercise_16_polymorphism_poc()
        results = oop_02.exercise_17_create_subclasses()
        results = oop_02.exercise_18_implement_subclasses()
        results = oop_02.exercise_19_subclasses_with_custom_attributes()
        results = oop_02.exercise_20_discounted_order_subclass()

        print("")
        print("#####################################################")
        print("Object-Oriented Programming - 21 through 30")
        print("#####################################################")
        results = oop_03.exercise_21_class_hierarchy_test()
        results = oop_03.exercise_22_identify_class_type()
        results = oop_03.exercise_23_type_checking()
        results = oop_03.exercise_24_implement_dunder_method()
        results = oop_03.exercise_25_implement_len_dunder_method()
        results = oop_03.exercise_26_property_getter_setter_poc()
        results = oop_03.exercise_27_callable_object_poc()
        results = oop_03.exercise_28_class_composition_check()
        results = oop_03.exercise_29_combine_composition_polymorphism_pox()
        results = oop_03.exercise_30_manage_state_transitions_poc()
        results = oop_03.exercise_31_manage_collection_of_objects_test()

        print("")
        print("#####################################################")
        print("Object-Oriented Programming - end")
        print("#####################################################\n")

        pass