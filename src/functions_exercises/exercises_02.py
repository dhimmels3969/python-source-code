
#
# https://pynative.com/python-functions-exercise-with-solutions/
# Exercises 11 through 18
#


global_var = 10

#########################################################################################
def print_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

def exercise_11_function_with_keyword_args():
    """
    Exercise 11. Create a Function with Keyword Arguments
    Practice Problem: Create a function print_info(**kwargs) that accepts an
        arbitrary number of keyword arguments and prints the key-value pairs.
    Exercise Purpose: While *args handles a list of values, **kwargs (keyword arguments)
        handles named data as a dictionary. This is standard practice in Python for functions
        that need to handle optional configuration settings or metadata.  The exercise
        requires you to create a function that can accept any number of keyword arguments.
        A keyword argument is where you specify the name of the argument along with its
        value (e.g., name="Alice", age=30). Inside the function, you need to access
        these arguments and print them in a key-value format.
    Given Input:
        print_info(name="Alice", age=30, city="New York")
    Expected Output:
        name: Alice
        age: 30
        city: New York
    """
    print("Exercise 11. Create a Function with Keyword Arguments")
    print_info(name="Alice", age=30, city="New York")
    print()
    pass



#########################################################################################
def exercise_12_modify_global_variables():
    """
    Exercise 12. Modifying Global Variables
    Practice Problem: Define a global variable global_var = 10. Write a function that
        successfully changes the value of this global variable to 20.
    Exercise Purpose: Normally, variables created inside a function
        are “Local”—they disappear when the function ends. To modify a variable
        that lives outside the function, you must use the global keyword. This
        exercise teaches you how to manage data persistence across different parts of your program.
    Given Input:
        global_var = 10
    Expected Output:
        Initial: 10
        Modified: 20
    """
    global global_var
    print("Exercise 12. Modifying Global Variables")
    print(f"Initial: {global_var}")
    global_var = 20
    print(f"Modified: {global_var}")
    pass



#########################################################################################
def factorial(num):
    # solution from pynative.com
    if num:
        # Recursive Case: add current num to the result of addition(num - 1)
        return num * factorial(num - 1)
    else:
        # Base Case: stop at 0
        return 1

def factorial_wrapper(num):
    results = factorial(num)
    print(f"Factorial of {num} is {results:,}")

def exercise_13_recursion_factorial():
    """
    Exercise 13. Recursive Factorial (Non-Negative Integers)
    Practice Problem: Write a recursive function to calculate the factorial of a non-negative integer.
    Exercise Purpose: Factorials (5! = 5 * 4 * 3 * 2 * 1) are the textbook example of recursion.
        This exercise reinforces the concept of a “Base Case” (stopping at 1) to prevent
        the function from running forever and crashing the memory stack.
    Given Input:
        number = 5
    Expected Output:
        The factorial of 5 is 120
    """
    print("Exercise 13. Recursive Factorial (Non-Negative Integers)")
    factorial_wrapper(5)
    factorial_wrapper(10)
    factorial_wrapper(21)
    print()
    pass



#########################################################################################
def exercise_14_square_number_using_lambda():
    """
    Exercise 14. Create a Lambda Function to Square a Number
    Practice Problem: Use the lambda keyword to create a small, anonymous function that
        takes one number and returns its square.
    Exercise Purpose: Sometimes you need a simple function for a split second
        (like when sorting a list or filtering data) and don’t want to write a full def block.
        Lambda functions are “one-liners” that make your code more concise and “Pythonic.”
    Given Input:
        number = 5
    Expected Output:
        25
    """
    print("Exercise 14. Square a Number")
    number = 5
    lsq = lambda x: x**2
    result = lsq(number)
    print(result)
    print()
    pass



#########################################################################################
def exercise_15_filter_list_using_lambda():
    """
    Exercise 15. Filter a List Using Lambda and filter()
    Practice Problem: Use the filter() function combined with a lambda to extract
        all even numbers from the list [1, 2, 3, 4, 5, 6, 7, 8, 9, 10].
    Exercise Purpose: The filter() function is a specialized tool for “weeding out” data.
        Instead of writing a bulky for loop with an if statement, filter() allows you
        to define a “rule” (the lambda) and apply it to an entire collection.
        This is a core concept in data science for cleaning datasets.
    Given Input:
        numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    Expected Output:
        [2, 4, 6, 8, 10]
    """
    print("Exercise 15. Filter a List Using Lambda and filter()")
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
    print(even_numbers)
    print()
    pass



#########################################################################################
def exercise_16_transform_list_using_lambda():
    """
    Exercise 16. Transform a List Using Lambda and map()
    Practice Problem: Use the map() function and a lambda to double every element
        in the list [1, 2, 3, 4, 5].
    Exercise Purpose: While filter removes items, map transforms them.
        It applies a specific operation to every single item in a list simultaneously.
        It’s like an assembly line where every item gets the same “upgrade” as it passes through.
    Given Input:
        numbers = [1, 2, 3, 4, 5]
    Expected Output:
        [2, 4, 6, 8, 10]
    """
    print("Exercise 16. Transform a List Using Lambda and map()")
    numbers = [1, 2, 3, 4, 5]
    doubled_numbers = list(map(lambda x: x * 2, numbers))
    print(doubled_numbers)
    print()
    pass



#########################################################################################
def exercise_17_sort_complex_data_using_lambda():
    """
    Exercise 17. Sort Complex Data with sorted() and Lambda
    Practice Problem: You have a list of tuples representing students and their grades:
        [("Alice", 88), ("Bob", 75), ("Charlie", 92)].
        Use the sorted() function and a lambda to sort this list based on the grades
        (the second element) in ascending order.
    Exercise Purpose: Real-world data is rarely just a simple list of numbers;
        it’s usually “messy” objects or tuples. This exercise teaches you how to tell
        Python exactly which part of a complex object it should use for sorting.
    Given Input:
        students = [("Alice", 88), ("Bob", 75), ("Charlie", 92)]
    Expected Output:
        [('Bob', 75), ('Alice', 88), ('Charlie', 92)]
    """
    print("Exercise 17. Sort Complex Data with sorted() and Lambda")
    students = [("Alice", 88), ("Bob", 75), ("Charlie", 92)]
    students_sorted_by_grade = sorted(students, key=lambda x: x[1])
    print(students_sorted_by_grade)
    print()
    pass



#########################################################################################
def exercise_18_pass_a_function_to_a_higher_order_function():
    """
    Exercise 18. Create a Higher-Order Function
    Practice Problem: Write a function apply_operation(func, x, y)
        that takes another function (func) and two numbers (x, y) as arguments.
        It should return the result of calling func(x, y). Show how this works
        by passing in different operations like addition and multiplication.
    Exercise Purpose: This is where you truly become a Python “Power User.”
        A Higher-Order Function is a function that treats other functions
        as parameters. This allows you to write extremely generic code that
        can do anything depending on what logic you “plug into” it.
    Given Input:
        # Function 1: add(a, b)
        # Function 2: multiply(a, b)
        # Values: 5, 3
    Expected Output:
        Addition Result: 8
        Multiplication Result: 15

    From <https://pynative.com/python-functions-exercise-with-solutions/>
    :return:
    :rtype:
    """
    print("Exercise 18. Create a Higher-Order Function")
    def add(a, b):
        return a + b

    def multiply(a, b):
        return a * b

    def apply_operation(func, x, y):
        return func(x, y)

    addition_result = apply_operation(add, 5, 3)
    multiplication_result = apply_operation(multiply, 5, 3)
    print(f"Addition Result: {addition_result}")
    print(f"Multiplication Result: {multiplication_result}")
    print()
    pass




