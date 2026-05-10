from src.common_library import helper_functions as hf


#
# Exercises found at web page https://pynative.com/python-dictionary-exercise-with-solutions/
# Exercises 11 through 20
#

##############################################################################
def exercise_11_check_for_specific_value():
    """
    Exercise 11: Check Value Existence
    Problem Statement: Write a Python program to verify whether a specific value
        is present anywhere in a dictionary.
    Purpose: Checking for value existence is common in validation workflows —
        for example, confirming that a username, status code, or category is
        already recorded before inserting a duplicate entry.
    Given Input:
        roles = {"alice": "admin", "bob": "editor", "carol": "viewer"}
        — check if "editor" and "manager" are present
    Expected Output:
        'editor' exists as a value: True
        'manager' exists as a value: False
    """
    def role_found(dict, value):
        return value in dict.values()

    print("Exercise 11: Check Value Existence")
    roles = {"alice": "admin", "bob": "editor", "carol": "viewer"}
    print(f"'editor' exists as a value: {role_found(roles, "editor")}")
    print(f"'manager' exists as a value: {role_found(roles, "manager")}")
    pass



##############################################################################
def exercise_12_sum_all_values():
    """
    Exercise 12: Sum All Values
    Problem Statement: Write a Python program to calculate the total of all
        numerical values stored in a dictionary.
    Purpose: Summing dictionary values is a fundamental aggregation
        operation used in budgeting, scorekeeping, inventory totals,
        and any scenario where a collection of labelled numeric measurements
        must be combined into a single figure.
    Given Input:
        expenses = {"rent": 1200, "food": 300, "transport": 150, "utilities": 200}
    Expected Output:
        Total expenses: 1850
    """
    print("Exercise 12: Sum All Values")
    expenses = {"rent": 1200, "food": 300, "transport": 150, "utilities": 200}
    total_expenses = sum(expenses.values())
    print(f"Total expenses: {total_expenses}")
    pass



##############################################################################
def exercise_13_extract_subset_of_keys():
    """
    Exercise 13: Extract Subset of Keys
    Problem Statement: Write a Python program to create a new dictionary
        containing only a specified subset of keys from an existing dictionary.
    Purpose: Extracting a key subset is essential when preparing data for display
        , serialisation, or an API call, you often need to expose only certain
        fields from a larger record while keeping the original intact.
    Given Input:
        user = {"id": 42, "username": "jdoe", "email": "jdoe@example.com", "password": "s3cr3t"
            , "joined": "2021-03-15"} — extract only ["id", "username", "email"]
    Expected Output:
        {'id': 42, 'username': 'jdoe', 'email': 'jdoe@example.com'}
    """
    print("Exercise 13: Extract Subset of Keys")
    user = {"id": 42, "username": "jdoe", "email": "jdoe@example.com", \
            "password": "s3cr3t", "joined": "2021-03-15"}
    keys_to_keep = ["walrus", "id", "username", "email"]
    # if a key is not found in the dictionary a key will be generated with a value of None.
    # Fliter out the missing key with an if statement in the dictionary comprehension.
    revised_user = {k: user.get(k) for k in keys_to_keep if user.get(k) != None}
    print(revised_user)
    pass



##############################################################################
def exercise_14_map_two_lists():
    """
    Exercise 14: Map Two Lists (zip)
    Problem Statement: Write a Python program that uses zip() to combine a list
        of keys and a list of values into a single dictionary.
    Purpose: Mapping two parallel lists into a dictionary with zip() is a pattern
        that appears constantly when processing tabular data, for example, pairing
        a header row with a data row read from a CSV file to produce
        a named-field record.
    Given Input:
        attributes = ["brand", "model", "year", "color"] and
        details = ["Honda", "Civic", 2023, "silver"]
    Expected Output:
        {'brand': 'Honda', 'model': 'Civic', 'year': 2023, 'color': 'silver'}
    """
    print("Exercise 14: Map Two Lists")
    attributes = ["brand", "model", "year", "color"]
    details = ["Honda", "Civic", 2023, "silver"]
    car_dictionary = dict(zip(attributes, details))
    print(car_dictionary)
    pass



##############################################################################
def exercise_15_count_character_frequencies():
    """
    Exercise 15: Count Character Frequencies
    Problem Statement: Write a Python program to count how many times each
        character appears in a given string, storing the results in a dictionary.
    Purpose: Character frequency counting is a foundational technique used
        in text analysis, data compression algorithms, cryptography, and
        natural language processing, making it an essential pattern to master early.
    Given Input:
        text = "hello world"
    Expected Output:
        {'h': 1, 'e': 1, 'l': 3, 'o': 2, ' ': 1, 'w': 1, 'r': 1, 'd': 1}
    """
    print("Exercise 15: Count Character Frequencies")
    text = "hello world"
    # character_counts = Counter(text)
    character_counts = {}
    for character in text:
        character_counts[character] = character_counts.get(character, 0) + 1
    print(character_counts)
    pass



##############################################################################
def exercise_16_modify_nested_dictionary():
    """
    Exercise 16: Modify Nested Dictionary
    Problem Statement: Write a Python program to change a specific value
        inside a dictionary that is nested within another dictionary.
    Purpose: Modifying nested dictionary values is a routine task when updating
        records in hierarchical data structures such as configuration objects,
        user profiles, or JSON documents loaded from an API.
    Given Input:
        company = {"name": "TechCorp", "location": {"city": "Berlin", "country": "Germany"}} —
        change the city to "Munich"
    Expected Output:
        {'name': 'TechCorp', 'location': {'city': 'Munich', 'country': 'Germany'}}
    """
    print("Exercise 16: Modify Nested Dictionary")
    company = {"name": "TechCorp", "location": {"city": "Berlin", "country": "Germany"}}
    updated_city = "Munich"
    company["location"]["city"] = updated_city
    print(company)
    pass



##############################################################################
def exercise_17_update_deeply_nested_key():
    """
    Exercise 17: Update Deeply Nested Key
    Problem Statement: Write a Python program to update a value located multiple
        levels deep inside a nested dictionary structure.
    Purpose: Real-world data such as configuration files, JSON API payloads,
        or document-store records is often nested three or more levels deep.
        This exercise trains you to navigate and update such structures
        confidently without disturbing surrounding data.
    Given Input:
        data = {"school": {"department": {"class": {"teacher": "Mr. Smith", "students": 30}}}}
        — update students to 35
    Expected Output:
        {'school': {'department': {'class': {'teacher': 'Mr. Smith', 'students': 35}}}}
    """
    print("Exercise 17: Update Deeply Nested Key")
    data = {"school": {"department": {"class": {"teacher": "Mr. Smith", "students": 30}}}}
    data["school"]["department"]["class"]["students"] = 35
    print(data)
    pass



##############################################################################
def exercise_18_dictionary_comprehension():
    """
    Exercise 18: Dictionary Comprehension
    Problem Statement: Write a Python program to generate a dictionary of the
        squares of numbers from 1 to 10 using a dictionary comprehension in a single line.
    Purpose: Dictionary comprehensions offer a concise, readable alternative to
        building dictionaries with loops. Mastering this syntax is valuable for
        data transformation tasks where keys and values are derived
        from a common iterable.
    Given Input:
        Numbers 1 through 10 (generated with range())
    Expected Output:
        {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81, 10: 100}
    """
    print("Exercise 18: Dictionary Comprehension")
    results = {i: i ** 2 for i in range(1,11)}
    print(results)
    pass



##############################################################################
def exercise_19_filter_dictionary():
    """
    Exercise 19: Filter Dictionary
    Problem Statement: Write a Python program to create a new dictionary containing
        only the key-value pairs from an existing dictionary where the value meets
        a specified condition.
    Purpose: Filtering dictionaries by value is a common data-cleaning and
        reporting operation. for example, keeping only high-scoring entries,
        retaining active records, or isolating items above a threshold before
        further processing.
    Given Input:
        scores = {"Alice": 82, "Bob": 45, "Carol": 91, "Dave": 58, "Eve": 73}
        — keep only scores greater than 60
    Expected Output:
        {'Alice': 82, 'Carol': 91, 'Eve': 73}
    """
    print("Exercise 19: Filter Dictionary")
    scores = {"Alice": 82, "Bob": 45, "Carol": 91, "Dave": 58, "Eve": 73}
    passing_score = 60
    filtered_dictionary = {item[0]: item[1] for item in scores.items() if item[1] > passing_score}
    print(filtered_dictionary)
    pass



##############################################################################
def exercise_20_find_key():
    """
    Exercise 20: Key of Minimum Value
    Problem Statement: Write a Python program to find the key associated with
        the smallest numerical value in a dictionary.
    Purpose: Locating the key of a minimum value is essential in ranking and
        optimisation tasks such as identifying the lowest-priced item, the
        least-visited page, or the team member with the fewest assigned tasks.
    Given Input:
        stock = {"apples": 34, "bananas": 12, "oranges": 57, "grapes": 8, "mangoes": 23}
    Expected Output:
        Lowest stock item: grapes
    """
    print("Exercise 20: Find Key")
    stock = {"apples": 34, "bananas": 12, "oranges": 57, "grapes": 8, "mangoes": 23}
    # lowest_stock_item = min(stock.values())
    lowest_item = min(stock.items(), key=lambda item: item[1])
    print(f"Lowest stock item: {lowest_item[0]}")
    pass




