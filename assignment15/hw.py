"""
Exercise 1:
Create a Pizza class that could have ingredients added to it. Raise an error if an attempt is 
made to add a duplicate ingredient.
"""
class Pizza:
    def __init__(self):
        self.ingredients = set()
    
    def add_ingredient(self, ingredient):
        if ingredient in self.ingredients:
            raise ValueError(f"Ingredient '{ingredient}' is already on the pizza!")
        self.ingredients.add(ingredient)


"""
Exercise 2:
Create an Elevator class with methods to go up, go down, and get the current floor. The elevator should not be able to go below the ground floor (floor 0).
"""
class Elevator:
    def __init__(self):
        self.current_floor = 0

    def go_up(self):
        self.current_floor += 1
        print(f"Elevator goes up to floor {self.current_floor}")

    def go_down(self):
        if self.current_floor > 0:
            self.current_floor -= 1
            print(f"Elevator goes down to floor {self.current_floor}")
        else:
            print("Elevator does not go below floor 0")

    def get_current_floor(self):
        return self.current_floor


"""
Exercise 3:
Create a class Stack with methods to push, pop, and check if the stack is empty. Raise an exception if a pop is attempted on an empty stack.
"""
class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if self.is_empty():
            raise IndexError("Can not pop on an empty stack")
        return self.items.pop()
    
    def is_empty(self):
        return len(self.items) == 0
    

"""
Exercise 4:
Design a BankAccount class with methods to deposit, withdraw, and check balance. Ensure that an account cannot go into a negative balance.
"""
class BankAccount:
    def __init__(self, initial_balance):
        if initial_balance < 0:
            raise ValueError("Initial balance can not be negative")
        self.balance = initial_balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited {amount}. Current balance {self.balance}")

    def withdraw(self, amount):
        if amount > self.balance:
            raise ValueError("Insufficient amount to withdraw")
        self.balance -= amount
        print(f"Withdrew {amount}. Current balance {self.balance}")

    def check_balance(self):
        print(f"Current balance {self.balance}")
        return self.balance
    


"""
Exercise 5:
Create a class Person with attributes for name and age. Implement a method birthday that increases the person's age by one. Raise an exception if an age less than 0 is entered.
"""
class Person:
    def __init__(self, name, age):
        if age < 0:
            raise ValueError("The age cannot be less than 0")
       
        self.name = name 
        self.age = age 

    def birthday(self):
        self.age += 1
        print(f"{self.name} turned {self.age}")


"""
Exercise 6:
Create an Animal base class and a Dog and Cat derived classes. Each animal should have a sound method which returns the sound they make.
"""
class Animal:
    def sound(self):
        return("Animal makes sound")

class Dog(Animal):
    def sound(self):
        return("Woof")

class Cat(Animal):
    def sound(self):
        return("Meow")


"""
Exercise 7:
Design a class Calculator with static methods for addition, subtraction, multiplication, and division. Division method should raise a ZeroDivisionError when trying to divide by zero.
"""
class Calculator:
    @staticmethod
    def add(x, y):
        return x + y

    @staticmethod
    def subtract(x, y):
        return x - y

    @staticmethod
    def multiply(x, y):
        return x * y

    @staticmethod
    def divide(x, y):
        if y == 0:
            raise ZeroDivisionError ("Cannot divide by 0")
        return x / y
    

"""
Exercise 8:
Create a class `Car` with attributes for speed and mileage. Raise a ValueError if a negative value for speed or mileage is entered.
"""
class Car:
    def __init__(self, speed, mileage):
        if speed < 0:
            raise ValueError("Speed cannot be negative")
        if mileage < 0:
            raise ValueError("Mileage cannot be negative")
            
        self.speed = speed
        self.mileage = mileage
        


"""
Exercise 9:
Create a Student class and a Course class. Each Course can enroll students and print a list of enrolled students.
"""
class Student:
    def __init__(self, name):
        self.name = name 

class Course:
    def __init__(self):
        self.students = []

    def enroll(self, student):
        self.students.append(student)

    def print_students(self):
        for student in self.students:
            print(student.name)


"""
Exercise 10:
Create a Flight class with a destination, departure time, and a list of passengers. Implement methods to add passengers, change the destination, and delay the flight by a certain amount of time.
"""
class Flight:
    def __init__(self, destination, departure):
        self.destination = destination
        self.departure = departure
        self.passengers = []
        
    def add_passenger(self, passenger):
        self.passengers.append(passenger)

    def change_destination(self, new_destination):
        self.destination = new_destination

    def delay(self, delay_time):
        
        hours, min = map(int, self.departure.split(':'))
        total_min = hours * 60 + min + delay_time * 60
        new_hours = total_min // 60
        new_min = total_min % 60 
        self.departure = f"{new_hours:02}:{new_min:02}"
        

"""
Exercise 11:
Create a Library class with a list of Book objects. The Book class should have attributes for title and author. The Library class should have methods to add books and find a book by title.
"""

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author 

class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def find_by_title(self, title):
        for book in self.books:
            if book.title == title:
                return book
        return None


"""
Exercise 12:
Design a class Matrix that represents a 2D matrix with methods for addition, subtraction, and 
multiplication. Implement error handling for operations that are not allowed 
(e.g., adding matrices of different sizes).
"""
class Matrix:
    def __init__(self, matrix):
        self.matrix = matrix
        self.rows = len(matrix)
        self.columns = len(matrix[0])
        
    def add(self, other):
        if self.rows != other.rows or self.columns != other.columns:
            raise ValueError("Matrices must have the same dimension")
        result = [[self.matrix[i][j] + other.matrix[i][j] for j in range(self.columns)] for i in range(self.rows)]
        return Matrix(result)
    

    def subtract(self, other):
        if self.rows != other.rows or self.columns != other.columns:
            raise ValueError("Matrices must have the same dimension")
        result = [[self.matrix[i][j] - other.matrix[i][j] for j in range(self.columns)] for i in range(self.rows)]

    def multiply(self, other):
        if self.columns != other.rows:
            raise ValueError("Matrices must have the same dimension")
        result = [sum(self.matrix[i][k] * other.matrix[k][j] for k in range(self.columns)) for j in range(other.columns) for i in range(self.rows)]
        return Matrix(result)
    

"""
Exercise 13:
Create a class Rectangle with attributes for height and width. 
Implement methods for calculating the area and perimeter of the rectangle. 
Also, implement a method is_square that returns true if the rectangle is a square and false otherwise.
"""
class Rectangle:
    def __init__(self, height, width):
        self.height = height
        self.width = width 

    def area(self):
        return self.height * self.width 

    def perimeter(self):
        return 2 * (self.height + self.width)

    def is_square(self):
        return self.height == self.width 
    

"""
Exercise 14:
Design a class Circle with attributes for radius. Implement methods for calculating the area and the circumference of the circle. Handle exceptions for negative radius values.
"""
class Circle:
    def __init__(self, radius):
        self.radius = radius
        if radius <= 0:
            raise ValueError("The radius must be positive")

    def area(self):
        return 3.14159265358979323846264338327950288419716939937510 * (self.radius**2)

    def circumference(self):
        return 2 * 3.14159265358979323846264338327950288419716939937510 * self.radius
    

"""
Exercise 15:
Design a class Triangle with methods to calculate the area and perimeter. Implement error handling for cases where the given sides do not form a valid triangle.
"""
import math
class Triangle:
    def __init__(self, side_a, side_b, side_c):
        self.side_a = side_a
        self.side_b = side_b
        self.side_c = side_c 
        
        if side_a <= 0 or side_b <= 0 or side_c <= 0:
            raise ValueError("The sides of the triangle must be only positive")
        if side_a + side_b <= side_c or side_a + side_c <= side_b or side_b + side_c <= side_a:
            raise ValueError("The sum of any two sides of the triangle must be bigger than third side") 

    def area(self):
        p = self.perimeter() / 2
        return math.sqrt(p * (p - self.side_a) * (p - self.side_b) * (p - self.side_c))

    def perimeter(self):
        return self.side_a + self.side_b + self.side_c
    


"""
Exercise 16:
Design a class Triangle with methods to calculate the area and perimeter. Implement error handling for cases where the given sides do not form a valid triangle.
"""


import math
class AbstractShape:
    def area(self):
        raise NotImplementedError("Subclasses must implement the area method.")

    def perimeter(self):
        raise NotImplementedError("Subclasses must implement the perimeter method.")

class Circle(AbstractShape):
    def __init__(self, radius):
    
        if radius <= 0:
            raise ValueError("Radius must be positive")
        self.radius = radius
        
    def area(self):
        return math.pi * self.radius ** 2
    def perimeter(self):
        return 2 * math.pi * self.radius
    
class Rectangle(AbstractShape):
    def __init__(self, height, width):

        if height <= 0 or width <= 0:
            raise ValueError("The height and width must be positive")
        self.height = height
        self.width = width
    def area(self):
        return self.height * self.width 

    def perimeter(self):
        return 2 * (self.height + self.width)
    
class Triangle(AbstractShape):
    def __init__(self, side_a, side_b, side_c):

        if side_a <= 0 or side_b <= 0 or side_c <= 0:
            raise ValueError("The sides of the triangle must be positive")
        if side_a + side_b <= side_c or side_a + side_c <= side_b or side_b + side_c <= side_a:
            raise ValueError("The sum of any two sides of the triangle must be bigger than third side") 
        
        self.side_a = side_a
        self.side_b = side_b
        self.side_c = side_c 
    
    def area(self):
        p = self.perimeter() / 2
        return math.sqrt(p * (p - self.side_a) * (p - self.side_b) * (p - self.side_c))

    def perimeter(self):
        return self.side_a + self.side_b + self.side_c

shapes = [Circle(5), Rectangle(4, 6), Triangle(3, 4, 5)]
for shape in shapes:
    print(f"Area: {shape.area()}, Perimeter: {shape.perimeter()}")

"""
Exercise 17:
Create a MusicPlayer class that contains a list of songs and methods to add songs, play a song, 
and skip to the next song. Also implement a method to shuffle the playlist.
"""
import random
class MusicPlayer:
    def __init__(self):
        self.playlist = []
        self.current_song = 0
    def add_song(self, song):
        self.playlist.append(song)
  
    def play_song(self):
        if not self.playlist:
            raise ValueError("No songs in the playlist")
        return self.playlist[self.current_song]

    def next_song(self):
        if not self.playlist:
            raise ValueError("No song to skip")
        self.current_song = (self.current_song + 1) % len(self.playlist)
        return self.playlist[self.current_song] 
    def shuffle(self):
        if not self.playlist:
            raise ValueError("Nothing to shuffle")
        random.shuffle(self.playlist)
        self.current_song = 0
        return self.playlist
"""
Exercise 18:
Design a Product class for an online store with attributes for name, price, and quantity. Implement methods to add stock, sell product, and check stock levels. Include error handling for attempting to sell more items than are in stock.
"""
class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def add_stock(self, quantity):
        if quantity > 0:
            self.quantity += quantity
        else:
            raise ValueError("Quanity to add must be positive")

    def sell(self, quantity):
        if quantity > self.quantity:
            raise ValueError(f"Cannot sell {quantity}, only {self.quantity} amount is available")
        elif quantity > 0:
            self.quantity -= quantity
        else:
            raise ValueError("Quantity to sell must be positive")

    def check_stock(self):
        return self.quantity


"""
Exercise 19:
Create a VideoGame class with attributes for title, genre, and rating. Implement methods to change the rating, change the genre, and display game details.
"""
class VideoGame:
    def __init__(self, title, genre, rating):
        self.title = title
        self.genre = genre
        self.rating = rating

    def change_rating(self, rating):
        self.rating = rating

    def change_genre(self, genre):
        self.genre = genre

    def display_details(self):
        print(f"Title: {self.title}")
        print(f"Genre: {self.genre}")
        print(f"Rating: {self.rating}")
        


"""
Exercise 20:
Create a School class with a list of Teacher and Student objects. Teacher and Student classes should have attributes for name and age. The School class should have methods to add teachers, add students, and print a list of all people in the school.
"""
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age 
    def __str__(self):
        return f"{self.name}, {self.age} years old"
class Teacher(Person):
    def __init__(self, name, age):
        super().__init__(name, age)
    def __str__(self):
        return f"Teacher {self.name}, {self.age} years old"

class Student(Person):
    def __init__(self, name, age):
        super().__init__(name, age)
    def __str__(self):
        return f"Student {self.name}, {self.age} years old"
class School:
    def __init__(self):
        self.teachers = []
        self.students = []

    def add_teacher(self, teacher):
        if isinstance(teacher, Teacher):
            self.teachers.append(teacher)
        else:
            raise ValueError("Only object Teacher can be added")

    def add_student(self, student):
        if isinstance(student, Student):
            self.students.append(student)
        else:
            raise ValueError("Only object Student can be added")
              
    def print_all(self):
        all_people = self.teachers + self.students
        for person in all_people:
            print(person)
            

"""
Exercise 21:
Design a Card class to represent a playing card with suit and rank. Then design a Deck class that uses the Card class. The Deck class should have methods to shuffle the deck, deal a card, and check the number of remaining cards.
"""
import random
class Card:

    def __init__(self, suit, rank):

        self.suit = suit
        self.rank = rank 
    def __repr__(self):
        return f"{self.rank} of {self.suit}"
class Deck:
    def __init__(self):
        suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
        ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
        self.cards = [Card(suit,rank) for suit in suits for rank in ranks]

    def shuffle(self):
        random.shuffle(self.cards)

    def deal(self):
        if len(self.cards) == 0:
            raise ValueError("Deck is empty")
        return self.cards.pop()
            

    def count(self):
        return len(self.cards)
    