#
# Exercises found at web page https://pynative.com/python-object-oriented-programming-oop-exercise/
# Exercises 1 through 10
#



##############################################################################
def exercise_01_empty_class():
    """
    Exercise 1: Define an Empty Vehicle Class
    Problem Statement: Write a Python program to create a class
        named Vehicle that has no variables or methods defined
        inside it.
    Purpose: This exercise introduces the most basic form of a
        Python class definition. It teaches you the required
        syntax for declaring a class and the use of the pass
        keyword as a placeholder, which is essential when you
        want to define an empty class or function body without
        causing a syntax error.
    Given Input:
        No input required.
    Expected Output:
        <class '__main__.Vehicle'>
    """
    print("Exercise 1: Define an empty Vehicle Class")
    pass



##############################################################################
def exercise_02_class_with_instance_attributes():
    """
    Exercise 2: Vehicle Class with Instance Attributes
    Problem Statement: Write a Python program to create a Vehicle
        class with two instance attributes: max_speed and mileage.
        Create an object of the class and print both attributes.
    Purpose: Learn to define instance attributes using the __init__
        constructor method. Instance attributes are unique to
        each object, meaning different Vehicle objects can hold
        different values for speed and mileage. This is a
        foundational concept in object-oriented programming.
    Given Input:
        vehicle1 = Vehicle("Tesla Model S", 250, 18)
    Expected Output:
        Vehicle Name: Tesla Model S, Speed: 250, Mileage: 18
    """
    print("Exercise 2: Vehicle Class with Instance Attributes")
    pass



##############################################################################
def exercise_03_rectangle_class():
    """
    Exercise 3: Rectangle Class with Area & Perimeter
    Problem Statement: Write a Python program to create a Rectangle
        class with length and width as instance attributes, and
        two methods: area() that returns the area and perimeter()
        that returns the perimeter.
    Purpose: Learn how to add instance methods to a class. Methods
        allow objects to perform operations using their own data,
        which is a key principle of encapsulation in OOP.
        Calculating geometric properties is a clean, practical
        context for understanding how self connects methods to
        instance data.
    Given Input:
        rect = Rectangle(10, 4)
    Expected Output:
        Area = 40 and Perimeter = 28
    """
    print("Exercise 3: Rectangle Class with Area and Perimeter")
    pass



##############################################################################
def exercise_04_student_class_average_grade():
    """
    Exercise 4: Student Class with Average Grade
    Problem Statement: Write a Python program to create a Student class
        that stores a student’s name and a list of marks. Add a method
        average() that calculates and returns the average of all marks.
    Purpose: This exercise shows how instance attributes can store
        complex data types such as lists, not just simple values.
        It also practices combining OOP with list operations and
        arithmetic, a pattern common in gradebooks, dashboards,
        and reporting tools.
    Given Input:
        s1 = Student("Alice", [85, 90, 78, 92, 88])
    Expected Output:
        Alice's Average Grade: 86.6
    """
    print("Exercise 4: Student Class with Average Grade")
    pass



##############################################################################
def exercise_05_product_class():
    """
    Exercise 5: Product Class with Stock Value Calculator
    Problem Statement: Write a Python program to create a Product
        class with three instance attributes: name, price, and quantity.
        Add a method total_value() that returns the total stock
        value by multiplying price by quantity.
    Purpose: This exercise models a real-world business scenario
        using OOP. It reinforces how instance methods can derive new
        information from existing attributes, a pattern widely used
        in inventory management, e-commerce, and financial
        applications.
    Given Input:
        p1 = Product("Laptop", 899.99, 5)
    Expected Output:
        Total stock value of Laptop: $4499.95
    """
    print("Exercise 5: Product Class with Stock Value Calculator")
    pass



##############################################################################
def exercise_06_bank_account_overdraft_protection():
    """
    Exercise 6: Bank Account with Deposit & Overdraw Protection
    Problem Statement: Write a Python program to create a BankAccount
        class with a balance attribute and two methods:
        deposit(amount) that adds funds to the balance, and
        withdraw(amount) that deducts funds but prevents the
        balance from going below zero.
    Purpose: Learn data validation and conditional logic inside
        instance methods. Preventing overdraw is a real-world business
        rule, and implementing it here teaches you how classes can
        enforce constraints on their own data, a core idea behind
        encapsulation in OOP.
    Given Input:
        Starting balance of 1000,
        deposit 500,
        withdraw 200,
        then attempt to withdraw 2000.
    Expected Output:
        Balance after deposit: 1500
        Balance after withdrawal: 1300
        Insufficient funds. Current balance: 1300
    """
    print("Exercise 6: BankAccount with Deposit & Overdraw Protection")
    pass



##############################################################################
def exercise_07_light_class_state_toggle():
    """
    Exercise 7: Light Class with On/Off State Toggle
    Problem Statement: Write a Python program to create a Light class
        with three methods: turn_on() that switches the light on,
        turn_off() that switches it off, and status() that reports
        whether the light is currently on or off.
    Purpose: This exercise models a simple stateful object, where
        the object remembers and changes its own condition over time.
        It introduces the concept of state management within a class,
        a pattern found everywhere from UI components and IoT
        devices to game objects and workflow engines.
    Given Input:
        Create a Light object, call turn_on(), check status(),
            call turn_off(), and check status() again.
    Expected Output:
        Light is ON
        Current status: ON
        Light is OFF
        Current status: OFF
    """
    print("Exercise 7: Light Class with On/Off State Toggle")
    pass



##############################################################################
def exercise_08_user_account_password_protection():
    """
    Exercise 8: User Class with Password Validation
    Problem Statement: Write a Python program to create a User class that
        stores a username and a password. Add a check_password(input_password)
        method that returns True if the input matches the stored password,
        and False otherwise.
    Purpose: This exercise introduces the idea of controlled access
        to sensitive data inside a class. Rather than exposing the
        password directly, the class provides a dedicated method to
        verify it. This pattern reflects a core principle of encapsulation
        in OOP, where internal data is protected and accessed only
        through defined interfaces.
    Given Input:
        u1 = User("alice", "secure123")
    Expected Output:
        True
        False
    """
    print("Exercise 8: User Class with Password Validation")
    pass



##############################################################################
def exercise_09_temperature_class():
    """
    Exercise 9: Temperature Class with Unit Converters
    Problem Statement: Write a Python program to create a Temperature
        class that stores a temperature in Celsius. Add two methods:
        to_fahrenheit() that converts and returns the value in
        Fahrenheit, and to_kelvin() that converts and returns the
        value in Kelvin.
    Purpose: This exercise demonstrates how a class can act as a data
        container with built-in conversion logic. It reinforces
        writing multiple methods that all operate on the same
        instance attribute, and applies straightforward
        mathematical formulas in a practical scientific context.
    Given Input:
        t = Temperature(100)
    Expected Output:
        Celsius: 100
        Fahrenheit: 212.0
        Kelvin: 373.15
    """
    print("Exercise 9: Temperature Class with Unit Converters")
    pass



##############################################################################
def exercise_10_notebook_class_display_notes():
    """
    Exercise 10: Notebook Class with Add & Display Notes
    Problem Statement: Write a Python program to create a Notebook
        class that maintains an internal list of notes. Add an
        add_note(note) method that appends a new note to the list,
        and a show_notes() method that prints all stored notes.
    Purpose: This exercise shows how a class can manage a growing
        collection of data over its lifetime. It practices
        initializing a mutable data structure inside __init__ and
        writing methods that both modify and read that structure,
        a pattern that appears in to do lists, message queues,
        logs, and many other applications.
    Given Input:
        Add three notes: "Buy groceries", "Read a book", "Call the doctor".
    Expected Output:
        1. Buy groceries
        2. Read a book
        3. Call the doctor
    """
    print("Exercise 10: Notebook Class with Add & Display Notes")
    pass



