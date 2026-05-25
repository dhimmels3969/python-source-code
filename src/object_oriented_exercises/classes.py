

######################################################################################
class Vehicle:
    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage

    def get_info(self):
        print(f"Vehicle Name: {self.name}, Speed: {self.max_speed}, Mileage: {self.mileage}")


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