import json
import logging
import math
from collections import namedtuple

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
    Point = namedtuple("Point", ["x", "y"])
    point_a = Point(3, 7)
    point_b = Point(10, 4)
    logger.info(f"  Attribute Access, point_a: {point_a.x}, {point_a.y}")
    logger.info(f"  Index Access, point_b: {point_b[0]}, {point_b[1]}")
    distance = math.sqrt((point_a.x - point_b.x)**2 + (point_a.y - point_b.y)**2)
    logger.info(f"  Distance between point_a and point_b: {distance}")
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
    Employee = namedtuple("Employee", ["name", "department", "salary"])
    Employee_records = []
    employees = [
        ("George", "Engineering", 100_000)
        , ("Mary", "Medical", 125_000)
        , ("Drew", "Medical", 95_000)
        , ("Lawrence", "Medical", 127_500)
        , ("Catherine X", "Medical", 145_000)
        , ("Catherine G", "Engineering", 115_875)
        , ("Tony", "Engineering", 120_000)
        , ("Silas", "Engineering", 125_000)
        , ("Wilma", "Engineering", 130_000)
        , ("Frank N", "Legal", 400_000)
        , ("Steve R", "Legal", 350_000)
        , ("William", "Legal", 625_000)
    ]
    for item in employees:
        Employee_records.append(Employee(*item))
    engineering_employees = [e for e in Employee_records if e.department == "Engineering"]
    logger.info(f"  -------- Engineering Employees --------")
    logger.info("")
    logger.info(f"  Department       Name            Salary")
    logger.info(f"  ---------------- --------------- ---------")
    for empl in engineering_employees:
        logger.info(f"  {empl.department:<16} {empl.name:<16} {empl.salary:>8,}")

    salaries = [e.salary for e in engineering_employees]
    logger.info(f"  Total Salaries for {engineering_employees[0].department} employees: ${sum(salaries):,} ")
    average_salary = sum(salaries) / len(salaries)
    logger.info(f"  Average Salary for {engineering_employees[0].department} employees: ${average_salary:,.0f} ")
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
        does not recognize them as dictionaries. Converting to a dict first is
        the standard bridge between the lightweight namedtuple record model
        and JSON-based APIs, configuration files, or database serialization layers.
    Given Input:
        A Product namedtuple with fields name, category, price, and in_stock.
    Expected Output:
        The namedtuple printed as a dict, then as a JSON string.
    """
    logger.info(f"Exercise 23: Convert namedtuple to Dictionary")
    Product = namedtuple("Product", ["name", "category", "price", "in_stock"])
    # Products = [
    #     Product("broccoli", "vegetable", 1.50, 50)
    #     , Product("celery", "vegetable", 1.12, 100)
    #     , Product("red potato", "vegetable", 2.29, 500)
    #     , Product("grapefruit", "fruit", 3.00, 500)
    #     , Product("tangerine", "fruit", 1.89, 500)
    #     , Product("cherries", "fruit", 3.75, 1000)
    #     , Product("saffron", "spices", 300, 32)
    # ]
    # for product in Products:
    #     product._asdict()

    product = Product("saffron", "spices", 300, 32)
    productDict = product._asdict()
    logger.info(f"  Product: {product}")
    productJson = json.dumps(productDict)
    logger.info(f"  ProductJson: {productJson}")

    # recreate the namedTuple from the dictionary
    productFromDict = Product(**productDict)
    results = (product == productFromDict)
    message = f"  Are the original product and the producted created from productDict equal?  {results}"
    logger.info(message)
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
    Listing = namedtuple("Listing", ["title", "price", "available", "rating"])
    original = Listing("1313 Mockingbird Lane", 875000, True, 4.9)
    version_1 = original._replace(available=False, rating = 3.99)
    version_2 = original._replace(available=True, price = 837500, rating = 7.4)
    logger.info(f"  Original Listing: {original}")
    logger.info(f"  Version 1 (first copy): {version_1}")
    logger.info(f"  Version 2 (second copy): {version_2}")
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
    Config = namedtuple("Config"
                        , ["host", "port", "debug", "timeout", "max_retries"]
                        , defaults=(False, 30, 3))

    configs = [
        Config("microsoft.com", 22),
        Config("google.com", 22, timeout=900, debug=True)
    ]

    for config in configs:
        # logger.info(f"  Config: {config}")
        # From PyNative...Display each field clearly
        logger.info("  Config field display and analysis:")
        for field, value in config._asdict().items():
            source = "(default)" if field in Config._field_defaults and \
                                    value == Config._field_defaults[field] else "(provided)"
            logger.info(f"    {field:15s}: {str(value):6s} {source}")
        logger.info(f"")
    pass