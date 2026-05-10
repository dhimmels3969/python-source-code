from src.common_library import helper_functions as hf


#
# Exercises found at web page https://pynative.com/python-dictionary-exercise-with-solutions/
# Exercises 1 through 10
#

##############################################################################
def exercise_01_basic_dictionary_operations():
    """
    Exercise 1: Basic Dictionary Operations
    Problem Statement: Write a Python program to add a new key-value pair
        to a dictionary, modify an existing value, and access a specific key.
    Purpose: Learn and practice the most fundamental dictionary operations
        such as insertion, update, and lookup, which form the backbone of working
        with key-value data in Python.
    Given Input:
        student = {"name": "Alice", "age": 20, "grade": "B"}
    Expected Output:
        {"name": "Alice", "age": 21, "grade": "B", "city": "New York"}
        and Name: Alice
    """
    print("Exercise 1: Basic Dictionary Operations")
    student = {"name": "Alice", "age": 20, "grade": "B"}
    # add key for city
    student["city"] = "New York"
    # update age
    student["age"] = 21
    print(student)
    print(f"Name: {student["name"]}")
    pass



##############################################################################
def exercise_02_dictionary_operations():
    """
    Exercise 2: Dictionary Operations
    Problem Statement: Write a Python program to remove a specific key
        from a dictionary, retrieve all key-value pairs, and check
        whether a given key exists.
    Purpose: To builds familiarity with essential dictionary methods pop(), items()
        , and the in operator, which are routinely used when processing and
        validating structured data.
    Given Input:
        car = {"brand": "Toyota", "model": "Camry", "year": 2022, "color": "blue"}
    Expected Output:
        {'brand': 'Toyota', 'model': 'Camry', 'year': 2022}
        dict_items([('brand', 'Toyota'), ('model', 'Camry'), ('year', 2022)])
        'brand' exists: True
        'color' exists: False
    """
    print("Exercise 2: Dictionary Operations")
    car = {"brand": "Toyota", "model": "Camry", "year": 2022, "color": "blue"}
    car.pop("color")
    print(car)
    print(car.items())
    print(f"brand exists: {"brand" in car.keys()}")
    print(f"color exists: {"color" in car.keys()}")
    pass



##############################################################################
def exercise_03_create_dictionary_from_lists():
    """
    Exercise 3: Dictionary from Two Lists
    Problem Statement: Write a Python program to create a dictionary by mapping
        two equal-length lists, one containing keys and the other containing values.
    Purpose: Learn how to construct a dictionary dynamically from existing data,
        a common pattern when importing tabular data, pairing labels with values,
        or building lookup tables.
    Given Input:
        keys = ["name", "age", "city"] and values = ["Bob", 25, "London"]
    Expected Output:
        {'name': 'Bob', 'age': 25, 'city': 'London'}
    """
    print("Exercise 3: Dictionary from Two Lists")
    keys = ["name", "age", "city"]
    values = ["Bob", 25, "London"]
    new_dictionary = dict(zip(keys, values))
    print(new_dictionary)
    pass



##############################################################################
def exercise_04_clear_dictionary():
    """
    Exercise 4: Clear Dictionary
    Problem Statement: Write a Python program to remove all items from a
        dictionary while keeping the dictionary object itself intact.
    Purpose: Understand the difference between clearing a dictionary and deleting it entirely,
        an important distinction when the same dictionary reference is shared across
        multiple parts of a program.
    Given Input:
        inventory = {"apples": 10, "bananas": 5, "oranges": 8}
    Expected Output:
        {}
    """
    print("Exercise 4: Clear Dictionary")
    inventory = {"apples": 10, "bananas": 5, "oranges": 8}
    inventory.clear()
    print(f"Dictionary after clearing is {inventory}")
    pass



##############################################################################
def exercise_05_merge_dictionaries():
    """
    Exercise 5: Merge Dictionaries
    Problem Statement: Write a Python program to combine two dictionaries into
        a single dictionary. If both dictionaries share a key, the value from
        the second dictionary should take precedence.
    Purpose: Merging dictionaries is a frequent task in configuration management,
        data aggregation, and API response handling, making it essential to know
        the available approaches and their precedence rules.
    Given Input:
        dict1 = {"a": 1, "b": 2} and dict2 = {"b": 3, "c": 4}
    Expected Output:
        {'a': 1, 'b': 3, 'c': 4}
    """
    print("Exercise 5: Merge Dictionaries")
    dict1 = {"a": 1, "b": 2}
    dict2 = {"b": 3, "c": 4}
    merged_dictionary = dict1 | dict2
    print(f"Results of merge: {merged_dictionary}")
    pass



##############################################################################
def exercise_06_access_nested_dictionary():
    """
    Exercise 6: Access Nested Dictionary
    Problem Statement: Write a Python program to retrieve a specific value
        from a dictionary that is nested inside another dictionary.
    Purpose: Nested dictionaries are widely used to represent structured
        data such as JSON responses, configuration files, and database
        records. This exercise trains you to navigate multiple levels0
         of key access.
    Given Input:
        person = {"name": "Carol", "address": {"city": "Paris", "zip": "75001"}}
    Expected Output:
        City: Paris
    """
    print("Exercise 6: Access Nested Dictionary")
    person = {"name": "Carol", "address": {"city": "Paris", "zip": "75001"}}
    city = person["address"]["city"]
    print(f"City: {city}")
    pass



##############################################################################
def exercise_07_access_key_in_nested_dictionary():
    """
    Exercise 7: Access ‘history’ Key From a Nested Dictionary
    Problem Statement: Write a Python program to access the value associated
        with the key 'history' from a dictionary nested within a larger data structure.
    Purpose: Understand multi-level dictionary traversal using a realistic data
        structure that resembles student records, course databases, or API payloads
        situations where a specific field must be extracted from deeply nested data.
    Given Input:
        student = {"name": "Dave", "grades": {"math": 88, "science": 92, "history": 75}}
    Expected Output:
        History grade: 75
    """
    print("Exercise 7: Access Nested Dictionary")
    student = {"name": "Dave", "grades": {"math": 88, "science": 92, "history": 75}}
    history_grade = student["grades"]["history"]
    print(f"History grade: {history_grade}")
    pass



##############################################################################
def exercise_08_initialize_dictionary_with_default_values():
    """
    Exercise 8: Initialize Dictionary with Default Values
    Problem Statement: Write a Python program to create a dictionary from a
        list of keys, assigning the same default value to every key.
    Purpose: Initializing dictionaries with default values is a common setup
        step in counting, scoring, and configuration tasks, it ensures every
        expected key exists before any data is processed.
    Given Input:
        keys = ["math", "science", "english", "history"] and default = 0
    Expected Output:
        {'math': 0, 'science': 0, 'english': 0, 'history': 0}
    """
    print("Exercise 8: Initialize Dictionary with Default Values")
    keys = ["math", "science", "english", "history"]
    default = 0
    new_dictionary = dict.fromkeys(keys, default)
    print(new_dictionary)
    pass



##############################################################################
def exercise_09_rename_key_in_dictionary():
    """
    Exercise 9: Rename a Key of Dictionary
    Problem Statement: Write a Python program to rename an existing key in a
        dictionary while preserving its associated value and the rest of
        the dictionary unchanged.
    Purpose: Renaming keys comes up frequently when normalizing data from
        external sources — such as API responses or CSV headers, to match
        the field names expected by your application.
    Given Input:
        employee = {"fname": "John", "age": 30, "dept": "Engineering"}
        — rename "fname" to "first_name"
    Expected Output:
        {'first_name': 'John', 'age': 30, 'dept': 'Engineering'}
    """
    print("Exercise 9: Rename Key In Dictionary")
    employee = {"fname": "John", "age": 30, "dept": "Engineering"}

    # remove key
    employee["first_name"] = employee.pop("fname")

    print(f"Dictionary item after rename: {employee}")
    pass



##############################################################################
def exercise_10_delete_list_of_keys():
    """
    Exercise 10: Delete a List of Keys
    Problem Statement: Write a Python program to remove multiple specific keys
        from a dictionary in one operation.
    Purpose: Bulk key removal is useful when filtering out sensitive fields before logging
        , stripping unwanted metadata from API responses, or trimming a record down to
        only the fields your application needs.
    Given Input:
        product = {"id": 101, "name": "Laptop", "price": 999, "stock": 50, "warehouse": "A3"}
        — remove keys ["stock", "warehouse"]
    Expected Output:
        {'id': 101, 'name': 'Laptop', 'price': 999}
    """
    print("Exercise 10: Delete List of Keys")
    product = {"id": 101, "name": "Laptop", "price": 999, "stock": 50, "warehouse": "A3"}
    items_to_delete = ["stock", "warehouse"]
    for item in items_to_delete:
        product.pop(item, None)
    print(f"Dictionary item after delete: {product}")
    pass





