#
# Exercises found at web page https://pynative.com/python-object-oriented-programming-oop-exercise/
# Exercises 21 through 31
#

from object_oriented_exercises.classes import \
    Vehicle, Bike_v3, Truck_v3, Bus_v3, \
    Vector, ShoppingCart, BankAccount_v2, Multiplier, \
    Flight, Passenger, \
    Animal, Dog, Cat, Lion, Elephant, Parrot, Zoo, \
    Character, PlayList, Song

import object_oriented_exercises.read_spreadsheet as rs
import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

##############################################################################
def exercise_21_class_hierarchy_test():
    """
    Exercise 21: Vehicle Class Hierarchy with Bike, Truck & Bus
    Problem Statement: Write a Python program that defines a Vehicle base
        class and creates Bike, Truck, and Bus subclasses, each defining
        a unique max_speed attribute and a describe() method.
    Purpose: This exercise reinforces the concept of class hierarchies
        and shows how subclasses can specialize a shared blueprint with
        their own attribute values, reflecting how real-world transport
        systems are categorized.
    Given Input:
        Objects of Bike, Truck, and Bus classes
    Expected Output:
        Bike max speed: 120 km/h
        Truck max speed: 90 km/h
        Bus max speed: 100 km/h
    """
    logger.info("Exercise 21: Vehicle Class Hierarchy with Bike, Truck & Bus")
    requests = [Bike_v3(120), Truck_v3(90), Bus_v3(100)]
    for request in requests:
        logger.info(f"  {request.describe()}")
    pass



##############################################################################
def exercise_22_identify_class_type():
    """
    Exercise 22: Identify Object’s Class Using type()
    Problem Statement: Write a Python program that creates objects from
        multiple classes and uses the built-in type() function to identify
        which class each object belongs to.
    Purpose: This exercise teaches you how Python tracks the type of
        every object at runtime. Understanding type() is essential for
        debugging, dynamic dispatch, and writing flexible code that
        reacts differently based on the type of object it receives.
    Given Input:
        Objects from Dog, Cat, and Vehicle classes
    Expected Output:
        d is of type: Dog
        c is of type: Cat
        v is of type: Vehicle
    """
    def get_class_of_item(key, value):
        message = f"{key} is of type: {type(value).__name__}"
        return message

    logger.info("Exercise 22: Object Type Identification")
    myVehicle = Vehicle("Tesla", 250, 0)
    myDog = Dog("Dog")
    myCat = Cat("Cat")
    var_names = ["myVehicle", "myDog", "myCat"]
    var_data = [myVehicle, myDog, myCat]
    # requests contains a list of tuples.
    # Each tuple contains the object name and the object.
    requests = zip(var_names, var_data)
    for k, v in requests:
        logger.info(f"  {get_class_of_item(k, v)}")
    pass



##############################################################################
def exercise_23_type_checking():
    """
    Exercise 23: Type Checking with isinstance() & issubclass()
    Problem Statement: Write a Python program that uses isinstance()
        to check whether an object is an instance of a given class,
        and issubclass() to check whether one class is a
        subclass of another.
    Purpose: This exercise teaches you two of Python’s most important
        type-inspection tools. Unlike type(), both functions are
        inheritance-aware, making them essential for writing flexible,
        safe code that handles mixed object types gracefully.
    Given Input:
        A Dog class inheriting from Animal, and an instance d = Dog()
    Expected Output:
        Is d an instance of Dog? True
        Is d an instance of Animal? True
        Is Dog a subclass of Animal? True
        Is Animal a subclass of Dog? False
    """
    logger.info("Exercise 23: Type Checking with isinstance() & issubclass")
    d = Dog("Dog")
    logger.info(f"  Is d an instance of Dog? {isinstance(d, Dog)}")
    logger.info(f"  Is d an instance of Animal? {isinstance(d, Animal)}")
    logger.info(f"  Is Dog a subclass of Animal? {issubclass(Dog, Animal)}")
    logger.info(f"  Is Animal a subclass of Dog? {issubclass(Animal, Dog)}")
    pass



##############################################################################
def exercise_24_implement_dunder_method():
    """
    Exercise 24: Vector Addition Using add Overloading
    Problem Statement: Write a Python program that creates a Vector class
        representing a 2D vector, and implements the __add__ dunder method
        so that two Vector objects can be added using the + operator.
    Purpose: This exercise introduces operator overloading, a powerful
        OOP feature that lets your custom classes behave like built-in types.
        Implementing __add__ makes your objects integrate naturally
        with Python’s syntax.
    Given Input:
        v1 = Vector(2, 3) and v2 = Vector(4, 1)
    Expected Output:
        Vector(6, 4)
    """
    logger.info("Exercise 24: Vector Addition Using add Overloading")
    v1 = Vector(2, 3)
    v2 = Vector(4, 1)
    v3 = v1 + v2
    logger.info(f"  {v3}")
    pass


##############################################################################
def exercise_25_implement_len_dunder_method():
    """
    Exercise 25: Cart Length Using len Overloading
    Problem Statement: Write a Python program that creates a Cart
        class that stores a list of items, and implements __len__ so
        that calling len(cart) returns the number of items currently
        in the cart.
    Purpose: This exercise introduces the __len__ dunder method,
        which lets your custom class integrate with Python’s built-in
        len() function. This is part of Python’s data model and
        makes your objects behave like native sequences or
        containers.
    Given Input:
        A cart with items ["apple", "banana", "mango"]
    Expected Output:
        Number of items in cart: 3
    """
    logger.info("Exercise 25: Cart Length Using len Overloading")
    myCart = ShoppingCart(["apple", "banana", "mango"])
    logger.info(f"  Number of items in cart: {len(myCart)}")
    pass



##############################################################################
def exercise_26_property_getter_setter_poc():
    """
    Exercise 26: Private Balance with Property Getter & Setter
    Problem Statement: Write a Python program that creates a BankAccount
        class where the balance is stored as a private attribute __balance,
        and exposed safely through a @property getter and a setter that
        validates the value before updating it.
    Purpose: This exercise demonstrates encapsulation, one of the four
        pillars of OOP. Using name-mangled private attributes alongside
        @property lets you control how external code reads and modifies
        internal state, preventing invalid data from being assigned.
    Given Input:
        BankAccount(1000), then deposit 500, then attempt to set balance to -200
    Expected Output:
        Current balance: 1000
        Current balance: 1500
        Invalid balance. Must be non-negative.
    """
    logger.info("Exercise 26: Private Balance with Property Getter & Setter")
    myAccount = BankAccount_v2(1000)
    logger.info(f"  {myAccount}")
    myAccount.deposit(500)
    logger.info(f"  {myAccount}")
    myAccount.deposit(-1700)
    logger.info(f"  {myAccount}")
    pass



##############################################################################
def exercise_27_callable_object_poc():
    """
    Exercise 27: Callable Object Class Using call
    Problem Statement: Write a Python program that creates a Multiplier
        class which stores a factor, and implements __call__ so that an
        instance of the class can be invoked directly like a function
        to multiply a given number by that factor.
    Purpose: This exercise introduces the __call__ dunder method,
        which makes any object callable. This pattern is commonly
        used in machine learning (layer objects), decorators, and
        anywhere you need a stateful function-like object.
    Given Input:
        Multiplier(3) called with 10, and Multiplier(5) called with 7
    Expected Output:
        30
        35
    """
    logger.info("Exercise 27: Callable Object Class Using call")
    mult1 = Multiplier(3)
    mult2 = Multiplier(5)
    for request in [mult1(10), mult2(7)]:
        logger.info(f"  {request}")

    pass



##############################################################################
def exercise_28_class_composition_check():
    """
    Exercise 28: Flight Class with Passenger Capacity Check
    Problem Statement: Write a Python program that creates a Passenger
        class and a Flight class. The Flight class should manage a
        list of Passenger objects and block further bookings when the
        seat capacity is reached.
    Purpose: This exercise models a real-world object composition
        scenario where one class owns and manages a collection of
        another class. It also teaches boundary enforcement, where
        business rules (capacity limits) are built directly into
        the class methods.
    Given Input:
        A Flight with capacity 2, then three booking attempts
    Expected Output:
        Alice booked on Flight AI202.
        Bob booked on Flight AI202.
        Sorry, Flight AI202 is fully booked.
    """
    def reserve(flight, passenger):
        reserve_flight_results = flight.book(passenger)
        logger.info(reserve_flight_results)

    logger.info("Exercise 28: Flight Class with Passenger Capacity Check")
    # Create the flight object
    myFlight = Flight("AI202", 2)
    passenger_20260603001 = Passenger("20260603001", "Lee M", "A!202")
    passenger_20260603002 = Passenger("20260603002", "Bobby H", "A!202")
    passenger_20260603003 = Passenger("20260603003", "Betty C", "A!202")

    for k, v in zip([myFlight, myFlight, myFlight],
                    [passenger_20260603001, passenger_20260603002, passenger_20260603003]):
        reserve(k, v)

    pass



##############################################################################
def exercise_29_combine_composition_polymorphism_pox():
    """
    Exercise 29: Zoo Class that Feeds All Animals
    Problem Statement: Write a Python program that defines an Animal
        base class with an eat() method, creates a few subclasses with
        their own eat() implementations, and builds a Zoo class that
        holds a list of animals and calls eat() on all of them
        via a feed_all() method.
    Purpose: This exercise combines composition with polymorphism.
        The Zoo class does not need to know the specific type of
        each animal; it simply calls the shared eat() interface
        on every object in its collection, and each animal responds
        in its own way.
    Given Input:
        A zoo containing a Lion, a Elephant, and a Parrot
    Expected Output:
        Lion eats meat.
        Elephant eats grass.
        Parrot eats seeds.
    """
    logger.info("Exercise 29: Zoo Class with Polymorphism")
    l = Lion("Lion", "meat")
    e = Elephant("Elephant", "grass")
    p = Parrot("Parrot", "seeds")
    myZoo = Zoo()
    for request in [l, e, p]:
        myZoo.add(request)
    myZoo.feed_all()
    pass



##############################################################################
def exercise_30_manage_state_transitions_poc():
    """
    Exercise 30: Character Class with Auto Level-Up Logic
    Problem Statement: Write a Python program that creates a Character
        class with health, exp, and level attributes. The character
        should automatically level up and reset exp whenever
        accumulated experience reaches or exceeds 100.
    Purpose: This exercise shows how to embed game logic directly into
        a class using a method that manages state transitions. It also
        demonstrates how to handle overflow (excess exp after
        levelling up) and keep multiple related attributes in sync.
    Given Input:
        Character("Aria", health=100), then gain_exp(60) twice
    Expected Output:
        Aria gained 60 exp. (Total: 60)
        Aria gained 60 exp. Level up! Now Level 2. (Remaining exp: 20)
    """
    logger.info("Exercise 30: Character Class with Auto Level Up Logic")
    myCharacter = Character("Aria", health=100)
    logger.info(f"  {myCharacter.gain_exp(60)}")
    logger.info(f"  {myCharacter.gain_exp(60)}")
    logger.info(f"  {myCharacter.gain_exp(75)}")
    logger.info(f"  {myCharacter.gain_exp(42)}")
    logger.info(f"  {myCharacter.gain_exp(63)}")
    pass



##############################################################################
def exercise_31_manage_collection_of_objects_test(src_dir):
    """
    Exercise 31: Playlist Class with Add, Remove & Shuffle
    Problem Statement: Write a Python program that defines a Song class
        and a Playlist class. The Playlist should support adding songs,
        removing songs by title, and shuffling the order of the
        playlist randomly.
    Purpose: This exercise reinforces object composition, list manipulation,
        and the use of the standard library. Managing a collection of objects
        with add, remove, and reorder operations is a pattern found in media
        players, task managers, and many real-world applications.
    Given Input:
        A playlist with three songs, then a removal and a shuffle
    Expected Output:
        Playlist: Blinding Lights, Levitating, Peaches
        Removed: Levitating
        After shuffle: (order will vary)
    """
    def displayList(list):
        for song in list:
            logger.info(f"  {song.title} - {song.artist}")
        logger.info("")

    logger.info("Exercise 31: Playlist Class with Add, Remove & Shuffle")
    songInfo = rs.read_spreadsheet(src_dir
                        , "data/object_oriented_exercises"
                        , "playlists.xlsx"
                        , "1.0")
    mySongsList = PlayList()

    for title, artist in songInfo:
        mySongsList.addSong(Song(title, artist))
    logger.info("  Initial list")
    displayList(mySongsList.songList)

    mySongsList.removeSong("All Along The Watchtower", "Jimi Hendrix Experience")
    logger.info("  After Removing a song")
    displayList(mySongsList.songList)

    # try to remove a song from the playlist where the item can not be found

    ########################################################################

    logger.info("  Shuffle #1")
    shuffled_list = mySongsList.shuffle()
    displayList(shuffled_list)

    logger.info("  Shuffle #2")
    shuffled_list = mySongsList.shuffle()
    displayList(shuffled_list)

    pass



