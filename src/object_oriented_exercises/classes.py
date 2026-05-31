

######################################################################################
class Vehicle:
    color = "White"
    def __init__(self, name, max_speed, mileage = 0):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage

    def get_info(self):
        print(f"Vehicle Name: {self.name}, Speed: {self.max_speed}, Mileage: {self.mileage}")

    def get_info_v2(self):
        print(f"{self.name} - Color: {Vehicle.color}, Speed: {self.max_speed}")

    def display(self):
        # Expected Output: Vehicle: School Bus, Max Speed: 120 km/h
        print(f"Vehicle: {self.name}, Speed: {self.max_speed} km/h")

######################################################################################
class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return (self.length + self.width) * 2


######################################################################################
class Student:
    def __init__(self, name: str, marks: list[float]):
        self.name = name
        self.marks = marks

    def average(self):
        return sum(self.marks) / len(self.marks)


######################################################################################
class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def total_value(self):
        return self.price * self.quantity


######################################################################################
class BankAccount:
    def __init__(self):
        self.balance = 1000

    def deposit(self, amount):
        self.balance += amount
        print(f"Balance after deposit: {self.balance}")

    def withdraw(self, amount):
        if self.balance - amount > 0:
            self.balance -= amount
            print(f"Balance after withdrawal: {self.balance}")
        else:
            print(f"Insufficient funds. Current balance: {self.balance}")


######################################################################################
class Light:
    def __init__(self):
        self._state = "OFF"

    def turn_on(self):
        self._state = "ON"
        print(f"Light is {self.status()}")

    def turn_off(self):
        self._state = "OFF"
        print(f"Light is {self.status()}")

    def status(self):
        return self._state


######################################################################################
class User:
    def __init__(self, name, pswd):
        self._name = name
        self._pswd = pswd

    def check_password(self, input_password):
        return input_password == self._pswd


######################################################################################
class Temperature:
    def __init__(self, temp):
        self._temperature = temp

    def temperature(self):
        return self._temperature

    def to_fahrenheit(self):
        return (self._temperature * 9 / 5) + 32

    def to_kelvin(self):
        return self._temperature + 273.15


######################################################################################
class Notebook:
    def __init__(self):
        self._notes = []

    def add(self, note):
        self._notes.append(note)

    def show_notes(self):
        counter = 1
        for note in self._notes:
            print(f"{counter}. {note}")
            counter += 1


######################################################################################
WATER_NEEDED_FOR_LATTE = 200
COFFEE_NEEDED_FOR_LATTE = 20
MILK_NEEDED_FOR_LATTE = 150

def enough_for_latte(water_, coffee_, milk_):
    return (water_ >= WATER_NEEDED_FOR_LATTE and
            coffee_ >= COFFEE_NEEDED_FOR_LATTE and
            milk_ >= MILK_NEEDED_FOR_LATTE)


class CoffeeMachine:
    def __init__(self, **kwargs):
        self._water = kwargs.get("water")
        self._coffee = kwargs.get("coffee")
        self._milk = kwargs.get("milk")
        print("A latte requires 200ml water, 20g coffee, and 150ml milk.")

    def make_latte(self):
        if enough_for_latte(self._water, self._coffee, self._milk):
            # Latte made! Remaining - Water: 100ml, Coffee: 80g, Milk: 50ml
            self._water -= WATER_NEEDED_FOR_LATTE
            self._coffee -= COFFEE_NEEDED_FOR_LATTE
            self._milk -= MILK_NEEDED_FOR_LATTE
            print(f"Latte made! Remaining - Water: {self._water}ml, Coffee: {self._coffee}ml, Milk: {self._milk}ml")
        else:
            print("Not enough resources to make a latte.")


######################################################################################
####  29MAY2026 Add new version of Vehicle class in order that previous exercises
####  using the Vehicle class will still run without error.
######################################################################################

class Vehicle_v2:
    color = "White"
    def __init__(self, name, max_speed, base_fare = 500):
        self._name = name
        self._max_speed = max_speed
        self._base_fare = base_fare

    def seating_capacity(self, capacity):
        print(f"{self._name} seating capacity is: {capacity}")

    def base_fare(self):
        return self._base_fare

######################################################################################
class Bus(Vehicle):
    pass

class Bus_v2(Vehicle_v2):
    def seating_capacity(self):
        super().seating_capacity(50)


class Taxi(Vehicle_v2):
    def __init__(self, name, max_speed, base_fare = 500):
        super().__init__(name, max_speed, base_fare)
        self._maintenance_fee = self.base_fare() * 0.10

    def total_fare(self):
        return self._maintenance_fee + self._base_fare



######################################################################################
class Media:
    def __init__(self, title, price):
        self.title = title
        self.price = price

    def describe(self):
        raise NotImplementedError(
            f"The {self.__class__.__name__} class must implement the 'describe' method."
        )


class Book(Media):
    def __init__(self, title, price, author):
        super().__init__(title, price)
        self._author = author

    def describe(self):
        # Book: Clean Code by Robert C. Martin - Rs.499
        results = f"{self.__class__.__name__}: {self.title} by {self._author} - Rs. {self.price}"
        return results


class Magazine(Media):
    def __init__(self, title, price, frequency):
        super().__init__(title, price)
        self._frequency = frequency

    def describe(self):
        # Magazine: Wired (Monthly) - Rs.150
        results = f"{self.__class__.__name__}: {self.title} ({self._frequency}) - Rs. {self.price}"
        return results


class DVD(Media):
    def __init__(self, title, price, duration):
        super().__init__(title, price)
        self._duration = duration

    def describe(self):
        # DVD: Inception, 148 mins - Rs.299
        results = f"{self.__class__.__name__}: {self.title}, {self._duration} mins - Rs. {self.price}"
        return results


######################################################################################
class Order:
    def __init__(self, id, total):
        self.id = id
        self.total = total

class DiscountedOrder(Order):
    def __init__(self, id, total):
        super().__init__(id, total)

    def discounted_total(self, discount_rate):
        return self.total - (self.total * discount_rate)


######################################################################################
