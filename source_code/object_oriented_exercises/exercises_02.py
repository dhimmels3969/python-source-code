
import math

from object_oriented_exercises.classes import \
    Vehicle, Student, Rectangle, Product, BankAccount, \
    Light, User, Temperature, Notebook, CoffeeMachine, \
    Vehicle_v2, Bus, Bus_v2, Taxi, \
    Dog, Cat, Book, Magazine, DVD, \
    DiscountedOrder
import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

#
# Exercises found at web page https://pynative.com/python-object-oriented-programming-oop-exercise/
# Exercises 11 through 20
#



##############################################################################
def exercise_11_coffee_machine_class():
    """
    Exercise 11: Coffee Machine with Multi-Resource Tracking
    Problem Statement: Write a Python program to create a CoffeeMachine
        class that tracks three resource attributes: water, coffee,
        and milk (in ml/g). Add a make_latte() method that checks
        whether sufficient resources are available, deducts them if
        so, and prints an appropriate message in either case.
    Purpose: This exercise combines state management, resource tracking,
        and conditional logic inside a single class. It mirrors how
        real-world stateful systems (vending machines, inventory
        systems, game resource managers) check preconditions before
        executing an action and update their internal state only
        when the action is valid.
    Given Input:
        CoffeeMachine(water=300, coffee=100, milk=200).
        A latte requires 200ml water, 20g coffee, and 150ml milk.
    Expected Output:
        Latte made! Remaining - Water: 100ml, Coffee: 80g, Milk: 50ml
        Not enough resources to make a latte.
    """
    logger.info("Exercise 11: Coffee Machine with Multi-Resource Tracking")
    ourCoffeeMachine = CoffeeMachine(water=300, coffee=100, milk=200)
    ourCoffeeMachine.make_latte()
    ourCoffeeMachine.make_latte()
    # print()
    pass



##############################################################################
def exercise_12_shared_class_attribures():
    """
    Exercise 12: Shared Class Attribute Across Instances
    Problem Statement: Write a Python program to create a Vehicle class
        with a class attribute color = "White" that is shared by all
        instances. Create two vehicle objects and demonstrate that both
        share the same default color, then show that changing the class
        attribute updates all instances that have not overridden it.
    Purpose: This exercise clarifies the distinction between class
        attributes and instance attributes. Class attributes are defined
        directly on the class and shared across every instance, making t
        hem ideal for default values or constants that apply universally.
        Understanding this difference prevents subtle bugs when mutable
        data is accidentally shared between objects.
    Given Input:
        v1 = Vehicle("Tesla", 250) and v2 = Vehicle("BMW", 200).
    Expected Output:
        Tesla - Color: White, Speed: 250
        BMW - Color: White, Speed: 200
        Tesla - Color: Red, Speed: 250
        BMW - Color: Red, Speed: 200
    """
    logger.info("Exercise 12: Shared Class Attribute Across Instances")
    v1 = Vehicle("Tesla", 250, 0)
    v2 = Vehicle("BMW", 200, 0)
    v1.get_info_v2()
    v2.get_info_v2()
    logger.info("------------AFTER--------------")
    Vehicle.color = "Red"
    v1.get_info_v2()
    v2.get_info_v2()
    pass



##############################################################################
def exercise_13_subclass_inheritance():
    """
    Exercise 13: Bus Subclass Inheriting from Vehicle
    Problem Statement: Write a Python program to create a Vehicle parent
        class with name and max_speed attributes and a display() method.
        Then create a Bus child class that inherits everything from
        Vehicle without adding anything new, and confirm that an
        instance of Bus can access the parent’s method.
    Purpose: This exercise introduces inheritance, one of the four
        pillars of OOP. Inheritance lets a child class automatically
        receive all attributes and methods from its parent, promoting
        code reuse and expressing natural “is-a” relationships.
        A Bus is a Vehicle, so it makes sense for it to share the
        same interface.
    Given Input:
        bus1 = Bus("School Bus", 120)
    Expected Output:
        Vehicle: School Bus, Max Speed: 120 km/h
    """
    logger.info("Exercise 13: Bus Subclass Inheriting from Vehicle")
    bus1 = Bus("School Bus", 120)
    # Python first looks for display on the Bus instance,
    # then on the Bus class, and finally on Vehicle, where it finds
    # and executes the method.This lookup process is known as
    # the Method Resolution Order (MRO).
    bus1.display()
    pass



##############################################################################
def exercise_14_override_parent_method():
    """
    Exercise 14: Override Parent Method Using super()
    Problem Statement: Write a Python program where a Vehicle parent
        class has a seating_capacity() method that accepts a capacity
        argument. Create a Bus child class that overrides this
        method to provide a default seating capacity of 50, using
        super() to call the parent’s version internally.
    Purpose: This exercise covers method overriding and the use of
        super(), two key tools in OOP inheritance. Overriding lets a
        child class customize or extend a parent method’s behavior
        without rewriting it from scratch. super() delegates part of
        the work back to the parent, keeping the code DRY and
        maintaining the original logic as a foundation.
    Given Input:
        bus = Bus("School Bus", 120)
    Expected Output:
        School Bus seating capacity is: 50
    """
    logger.info("Exercise 14: Override Parent Method Using super()")
    bus = Bus_v2("School Bus", 120)
    bus.seating_capacity()
    pass



##############################################################################
def exercise_15_extend_child_class():
    """
    Exercise 15: Add Maintenance Fee in Child Class via super()
    Problem Statement: Write a Python program that creates a Vehicle parent
        class with a base fare, then extends a Taxi child class that adds
        a 10% maintenance fee on top of the base fare using super().
    Purpose: This exercise teaches you how to use super() to call the
        parent class constructor, extend child class behaviour by
        building on inherited attributes, and model real-world pricing
        logic using inheritance.
    Given Input:
        base_fare = 500
    Expected Output:
        Total fare with maintenance fee: 550.0
    """
    logger.info("Exercise 15: Add Maintenance Fee in Child Class via super()")
    myTaxi = Taxi("Taxi", 120, 500)
    logger.info(f"  Total fare with maintenance fee: {myTaxi.total_fare()}")
    pass



##############################################################################
def exercise_16_polymorphism_poc():
    """
    Exercise 16: Polymorphism with Dog & Cat speak()
    Problem Statement: Write a Python program that defines an Animal
        base class with a speak() method, then overrides it in Dog
        and Cat subclasses to return their respective sounds.
    Purpose: This exercise introduces method overriding, one of the
        core pillars of polymorphism in OOP. It shows how different
        subclasses can share the same interface but provide their
        own specific behaviour.
    Given Input:
        Objects of Dog and Cat classes
    Expected Output:
        Dog says: Woof!
        Cat says: Meow!
    """


    def Speak(creature):
        # Dog says: Woof!
        logger.info(f"  {creature.name} says: {creature.speak()}")

    logger.info("Exercise 16: Polymorphism with Dog & Cat speak()")
    myDog = Dog("Dog")
    Speak(myDog)
    myCat = Cat("Cat")
    Speak(myCat)
    pass



##############################################################################
def exercise_17_create_subclasses():
    """
    Exercise 17: Full-Time vs Part-Time Employee Pay Logic
    Problem Statement: Write a Python program that defines an Employee
        base class, then creates FullTimeEmployee and PartTimeEmployee
        subclasses, each implementing different pay calculation logic.
    Purpose: This exercise models a common HR scenario and teaches
        you how to use inheritance to share common attributes while
        allowing each subclass to define its own business logic
        for calculating pay.
    Given Input:
        FullTimeEmployee("Alice", 60000) and
        PartTimeEmployee("Bob", 500, 20)
    Expected Output:
        Alice's monthly pay: 5000.0
        Bob's monthly pay: 10000
    """
    class Employee:
        def __init__(self, name):
            self.name = name

        def calculate_pay(self):
            return 0

    class FullTimeEmployee(Employee):
        def __init__(self, name, annual_salary):
            super().__init__(name)
            self._salary = annual_salary

        def calculate_pay(self):
            return self._salary / 12.0

    class PartTimeEmployee(Employee):
        def __init__(self, name, hourly_rate, number_hours):
            super().__init__(name)
            self._hourly_rate = hourly_rate
            self._number_hours = number_hours

        def calculate_pay(self):
            return self._hourly_rate * self._number_hours

    def display_info(employee):
        message = f"  {employee.name}'s monthly pay: ${employee.calculate_pay():,.0f}"
        logger.info(message)
        pass

    logger.info("Exercise 17: FullTimeEmployee and PartTimeEmployee pay logic")
    full_time_emp = FullTimeEmployee("Alice", 60000)
    display_info(full_time_emp)

    part_time_emp = PartTimeEmployee("Bob", 500, 20)
    display_info(part_time_emp)
    pass



##############################################################################
def exercise_18_implement_subclasses():
    """
    Exercise 18: Shape Subclasses with Custom area() Methods
    Problem Statement: Write a Python program that defines a Shape base
        class with an area() method, then implements it in Circle, Square,
        and Triangle subclasses using the appropriate geometric formulas.
    Purpose: This exercise is a classic demonstration of polymorphism. Each
        shape shares the same area() interface but provides a completely
        different calculation, showing how OOP handles real-world
        variation cleanly.
    Given Input:
        Circle(7), Square(4), Triangle(6, 8)
    Expected Output:
        Circle area: 153.94
        Square area: 16
        Triangle area: 24.0
    """
    class Shape:
        def area(self):
            logger.error(f"  The {self.__class__.__name__} class must implement the 'area' method.")
            raise NotImplementedError(
                f"  The {self.__class__.__name__} class must implement the 'area' method."
            )

    class Circle(Shape):
        def __init__(self, radius):
            self._radius = radius

        def area(self):
            return math.pi *  (self._radius**2)

    class Square(Shape):
        def __init__(self, side):
            self._side = side
        def area(self):
            return self._side ** 2

    class Triangle(Shape):
        def __init__(self, base, height):
            self._base = base
            self._height = height

        def area(self):
            return self._base * self._height * 0.5



    logger.info("Exercise 18: Shape Subclasses with Custom area() method")
    # myCircle = Circle(7)
    # mySquare = Square(4)
    # myTriangle = Triangle(6, 8)

    shapes = [Circle(7), Square(4), Triangle(6, 8)]
    for shape in shapes:
        logger.info(f"  {type(shape).__name__} area: {shape.area():.2f}")

    pass



##############################################################################
def exercise_19_subclasses_with_custom_attributes():
    """
    Exercise 19: Media Subclasses with Type-Specific Attributes
    Problem Statement: Write a Python program that defines a Media base class,
        then creates Book, Magazine, and DVD subclasses, each with
        type-specific attributes and a describe() method.
    Purpose: This exercise shows how inheritance can model a taxonomy of
        related objects. Each media type shares a common identity
        (title, price) but carries unique attributes specific to its
        format, reflecting real-world library or inventory systems.
    Given Input:
        Book("Clean Code", 499, "Robert C. Martin"),
        Magazine("Wired", 150, "Monthly"),
        DVD("Inception", 299, 148)
    Expected Output:
        Book: Clean Code by Robert C. Martin - Rs.499
        Magazine: Wired (Monthly) - Rs.150
        DVD: Inception, 148 mins - Rs.299
    """
    logger.info("Exercise 19: Media Subclasses with Type-Specific Attributes")
    media_items = [Book("Clean Code", 499, "Robert C. Martin"),
                   Magazine("Wired", 150, "Monthly"),
                   DVD("Inception", 299, 148)]
    for item in media_items:
        logger.info(f"  {item.describe()}")
    pass



##############################################################################
def exercise_20_discounted_order_subclass():
    """
    Exercise 20: Discounted Order Subclass with 10% Off
    Problem Statement: Write a Python program that creates an Order class
        with a total amount, then creates a DiscountedOrder subclass that
        applies a 10% discount to the total.
    Purpose: This exercise models a common e-commerce pattern and shows
        how a child class can extend a parent’s behaviour by modifying
        a calculated value, without changing the parent class at all.
    Given Input:
        DiscountedOrder("ORD001", 1200)
    Expected Output:
        Order ID: ORD001
        Original Total: 1200
        Discounted Total: 1080.0
    """
    logger.info("Exercise 20: Discounted Order Subclass with 10% Off")
    myOrder = DiscountedOrder("ORD001", 1200)
    logger.info(f"  Order ID: {myOrder.id}")
    logger.info(f"  Original Total: {myOrder.total:.2f}")
    logger.info(f"  Discounted Total: {myOrder.discounted_total(0.10):.2f}")
    pass



