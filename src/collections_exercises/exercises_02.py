import logging
#
# https://pynative.com/python-collections-module-exercises/
# Exercises 21 through 25
#


logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)



#########################################################################################
def exercise_21_create_namedtuple():
    """
    Exercise 21: Create a namedtuple
    Problem Statement:
        Write a Python program that defines a Point namedtuple with
        fields x and y, creates two instances, and accesses their
        coordinates using both attribute access and positional index access.
    Purpose:
        A namedtuple gives a plain tuple named fields, making code that
        passes coordinate pairs, RGB values, or simple records significantly
        more readable than using raw index numbers. It is immutable,
        memory-efficient, and fully compatible with code that expects
        regular tuples, making it a zero-overhead upgrade over anonymous
        tuples.
    Given Input:
        Two points – Point(3, 7) and Point(10, 4).
    Expected Output:
        Coordinates accessed by attribute name and by index,
        plus the distance between the two points.
    """
    logger.info(f"Exercise 21: Create a namedtuple")
    pass


#########################################################################################
def exercise_22_namedtuple_lightweight_record():
    """
    Exercise 22: namedtuple as a Lightweight Record
    Problem Statement:
        Write a Python program that defines an Employee namedtuple with fields
        name, department, and salary, creates a list of employee records, and
        prints all employees belonging to a specific department.
    Purpose:
        Namedtuples are an excellent lightweight alternative to full classes or
        dictionaries for storing structured records when no methods or mutability
        are needed. This pattern is widely used for database row representations
        , CSV record models, API response objects, and configuration entries
        where clarity and low overhead matter.
    Given Input:
        A list of five Employee records across three departments. Filter for "Engineering".
    Expected Output:
        Name and salary of every employee in the Engineering department, one per line.
    """
    logger.info(f"Exercise 22: namedtuple as a Lightweight Record")
    pass



#########################################################################################
def exercise_23_convert_namedtuple_to_dict():
    """
    Exercise 23: Convert namedtuple to Dictionary
    Problem Statement:
        Write a Python program that creates a namedtuple instance and converts
        it to a regular dictionary using the _asdict() method, then
        demonstrates how to use the resulting dictionary for JSON
        serialization.
    Purpose:
        Namedtuples cannot be directly serialized to JSON because json.dumps()
        does not recognise them as dictionaries. Converting to a dict first is
        the standard bridge between the lightweight namedtuple record model
        and JSON-based APIs, configuration files, or database serialization layers.
    Given Input:
        A Product namedtuple with fields name, category, price, and in_stock.
    Expected Output:
        The namedtuple printed as a dict, then as a JSON string.
    """
    logger.info(f"Exercise 23: Convert namedtuple to Dictionary")
    pass


#########################################################################################
def exercise_24_replace_field_value():
    """
    Exercise 24: Replace a Field Value
    Problem Statement:
        Write a Python program that creates a namedtuple instance representing a
        product listing and uses the _replace() method to produce updated copies
        with changed field values, without modifying the original instance.
    Purpose:
        Because namedtuples are immutable, _replace() is the correct way to create
        a modified version of an existing record – analogous to using
        dataclasses.replace() for dataclasses or spread syntax in JavaScript.
        This pattern is common in functional programming workflows where data
        is never mutated in place.
    Given Input:
        A Listing namedtuple with fields title, price, available, and rating.
    Expected Output:
        Original listing printed, then two modified copies with updated fields,
        confirming the original is unchanged.
    """
    logger.info(f"Exercise 24: Replace a Field Value")
    pass



#########################################################################################
def exercise_25_namedtuple_default_values():
    """
    Exercise 25: namedtuple with Default Values
    Problem Statement:
        Write a Python program that defines a Config namedtuple using the
        defaults parameter so that some fields have fallback values and
        can be omitted at instantiation, then creates instances with
        and without the optional fields.
    Purpose:
        Default values make namedtuples practical for configuration objects,
        optional record fields, and function return types where some fields
        may not always be populated. This feature was added in Python 3.6.1
        and removes the need to subclass or use __new__ tricks to achieve
        optional fields.
    Given Input:
        A Config namedtuple with required fields host and port, and
        optional fields debug (default False), timeout (default 30),
        and max_retries (default 3).
    Expected Output:
        A fully specified config and a minimal config printed side by side,
        showing default values filling in the omitted fields.
    """
    logger.info(f"Exercise 25: namedtuple with default values")
    pass