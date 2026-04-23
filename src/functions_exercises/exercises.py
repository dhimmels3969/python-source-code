
#
# https://pynative.com/python-functions-exercise-with-solutions/
# Exercises 1 through 10
#




#########################################################################################
def demo(name, age):
    print(f"{name} {age}")
    return None

def exercise_01_create_function_with_parameters():
    """
    Exercise 1. Create a Function with Parameters
    Practice Problem: Write a function called demo() that accepts two parameters:
        a name and an age. The function should print these values directly to the console.
    Exercise Purpose: This is the foundation of modular programming. It teaches
        how to pass data from the main program into a function’s local scope,
        allowing the same logic to be reused with different datasets.
    Given Input:
        name = "Kelly"
        age = 25
    Expected Output:
        Kelly 25
    """
    print("Exercise 1. Create a Function with Parameters")
    demo("Kelly", 25)
    pass



#########################################################################################
def func1(*args):
    print("Printing values:")
    for arg in args:
        print(arg)
    print()

def exercise_02_variable_length_arguments():
    """
    Exercise 2. Variable Length of Arguments (*args)
    Practice Problem: Create a function func1() such that it can accept a
        variable number of arguments and print all of them. Whether you
        pass two numbers or five, the function should handle them all without error.
    Exercise Purpose: In real-world programming (like logging or mathematical operations),
        you often don’t know how many inputs a user will provide. Using *args allows
        your function to be flexible and “future-proof.”
    Read: variable length of arguments in functions
    Given Input:
        Call 1: func1(20, 40, 60)
        Call 2: func1(80, 100)
    Expected Output:
        Printing values:
        20
        40
        60
        Printing values:
        80
        100
    """
    print("Exercise 2. Variable Length of Arguments (*args)")
    func1(20, 40, 60)
    func1(80, 100)
    pass



#########################################################################################

def calculation(a, b):
    return a + b, a-b


def exercise_03_return_multiple_values():
    """
    Exercise 3. Return Multiple Values from a Function
    Practice Problem: Write a function calculation() that accepts two variables
        and calculates both addition and subtraction. The function must return
        both results in a single return statement.
    Exercise Purpose: Unlike many languages (like C or Java) where a function
        typically returns only one value, Python allows “Tuple Unpacking.” This
        makes it incredibly efficient to retrieve multiple pieces of processed data at once.
    Given Input:
        a = 40
        b = 10
    Expected Output:
        50, 30
    """
    print("Exercise 3. Return Multiple Values from a Function")
    (add_result, subtraction_result) = calculation(40, 10)
    print(f"{add_result}, {subtraction_result}")
    print()
    pass



#########################################################################################
def show_employee(name, salary = 9000):
    print(f"Name: {name}, Salary: {salary}")

def exercise_04_functions_default_argument():
    """
    Exercise 4. Function with Default Argument
    Practice Problem: Create a function show_employee() that accepts
        an employee’s name and salary. If the salary is not provided in
        the function call, the function should automatically assign a
        default value of 9000.
    Exercise Purpose: Default arguments are essential for creating APIs
        or functions where certain settings are “standard.” It allows the
        function to be called with less information, making the code cleaner
        and reducing errors when data is missing.
    Given Input:
        Case 1: name="Ben", salary=12000
        Case 2: name="Jessa"(salary missing)
    Expected Output:
        Name: Ben salary: 12000
        Name: Jessa salary: 9000
    """
    print("Exercise 4. Function with Default Argument")
    show_employee("Ben", 12000)
    show_employee("Jessa")
    print()
    pass



#########################################################################################
def wrapper(a, b):
    def inner_func(a,b):
        return a + b
    result = inner_func(a, b)
    return result + 5

def exercise_05_inner_function_example():
    """
    Exercise 5. Create an Inner Function
    Practice Problem: Create an outer function that accepts two parameters, a and b.
        Inside, create an inner function that calculates the addition of a and b.
        The outer function should then add 5 to that sum and return the final result.
    Exercise Purpose: This introduces “Nested Functions” and “Encapsulation.”
        Inner functions are hidden from the global scope, meaning they can only
        be accessed by the outer function. This is the first step toward understanding
        Python Decorators and Closures.
    Given Input:
        a = 5
        b = 10
    Expected Output:
        20
    """
    print("Exercise 5. Create an Inner Function")
    result = wrapper(5, 10)
    print(f"{result}")
    print()
    pass



#########################################################################################
def addition(num):
    # solution from pynative.com
    if num:
        # Recursive Case: add current num to the result of addition(num - 1)
        return num + addition(num - 1)
    else:
        # Base Case: stop at 0
        return 0
#############################################################################
def addition_alt(limit, counter = 0, cumulative_total = 0):
    if counter >= limit:
        return cumulative_total
    else:
        counter += 1
        cumulative_total += counter
        return addition_alt(limit, counter, cumulative_total)
#############################################################################
def exercise_06_recursion_addition(limit=10):
    """
    Exercise 6. Create a Recursive Function
    Practice Problem: Write a recursive function addition() that calculates
        the sum of numbers from 0 to 10. A recursive function is a function that
        calls itself to solve smaller instances of the same problem.
    Exercise Purpose: Recursion is a fundamental computer science concept used
        to solve complex problems by breaking them into simpler sub-problems.
        It is essential for understanding algorithms like tree traversals and sorting.
        This exercise focuses on the “Base Case” (when to stop) and
        the “Recursive Case” (how to progress).
    Given Input:
        num = 10
    Expected Output:
        55
    """
    print("Exercise 6. Create a Recursive Function")
    sum = addition_alt(limit)
    print(f"{sum}")

    res = addition(10)
    print(res)
    pass



#########################################################################################
def display_student(name, age):
        print(name, age)

def exercise_07_assign_function_different_name():
    """
    Exercise 7. Assign a Different Name to Function and Call It
    Practice Problem: Assign a different name to the function display_student(name, age)
        and call it using the new name. For example, assign it to a variable called show_student.
    Exercise Purpose: In Python, functions are “first-class objects.” This means they
        can be treated like any other variable—passed as arguments, returned from other
        functions, or renamed. This is useful for aliasing long function names or passing
        logic into different modules.
    Given Input:
        def display_student(name, age):
            print(name, age)
    Expected Output:
        Emma 26
    """
    print("Exercise 7. Assign a Different Name to Function and Call it")
    student_info = display_student
    student_info("Emma", 26)
    print()
    pass



#########################################################################################
def build_a_list(lower, upper):
    final_result = []
    for i in range(lower, upper + 1):
        if i % 2 == 0:
            final_result.append(i)
    return final_result


def exercise_08_generate_list(lower, upper):
    """
    Exercise 8. Generate a List of Even Numbers (Range Function)
    Practice Problem: Create a function that generates a list of all even
        numbers between 4 and 30.
    Exercise Purpose: This exercise teaches the use of the range() function and how to
        convert range objects into lists. Understanding how to generate sequences of
        data is vital for data processing and automated loops.
    Expected Output:
        [4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28]
    """
    print("Exercise 8. Generate a List of Even Numbers (Range Function)")
    final_result = build_a_list(lower, upper)
    print(f"{final_result}")
    print()
    pass




#########################################################################################
def find_max_value(list_to_parse):
    max_value = 0
    for item in list_to_parse:
        if item > max_value:
            max_value = item
    return max_value

def exercise_09_find_max_in_list():
    """
    Exercise 9. Find the Largest Item in a List
    Practice Problem: Create a function that takes a list of numbers as input and
        returns the largest item from that list without using the built-in max()
        function (to practice manual logic).
    Exercise Purpose: Finding a maximum value is one of the most common tasks
        in programming (e.g., finding the highest price, the top score, or the
        oldest record). Implementing this manually builds an understanding of
        “Accumulator Patterns”—keeping track of a state while iterating through data.
    Given Input:
        x = [4, 6, 8, 24, 12, 2]
    Expected Output:
        24
    """
    print("Exercise 9. Find the Largest Item in a List")
    x = [4, 6, 8, 24, 12, 2]
    final_result = find_max_value(x)
    print(f"{final_result}")
    print()
    pass



#########################################################################################
def describe_pet(animal_type, pet_name):
    message = f"I have a pet {animal_type}.\nMy {animal_type}'s name is {pet_name}"
    print(message)

def exercise_10_keyword_positional_arguments():
    """
    Exercise 10. Call Function using Positional and Keyword Arguments
    Practice Problem: Define a function describe_pet(animal_type, pet_name) that prints a
        description of a pet. Call this function twice: once using positional
        arguments and once using keyword arguments.
    Exercise Purpose: This exercise demonstrates the flexibility of Python’s
        calling conventions. Positional arguments rely on the order of the data,
        while Keyword arguments use the parameter names to ensure data goes to
        the right place regardless of order.
    Given Input:
        # Call 1 (Positional): "hamster", "Harry"
        # Call 2 (Keyword): animal_type="dog", pet_name="Willie"
    Expected Output:
        I have a hamster.
        My hamster's name is Harry.
        I have a dog.
        My dog's name is Willie.
    """
    print("Exercise 10. Call Function using Positional and Keyword Arguments")
    describe_pet("hamster", "Harry")
    describe_pet(pet_name="Willie", animal_type="dog")
    print()
    pass



