"""
💎 Exercise 1: User Management System

Design a User Management System for an application. 
The User class should have details such as name and email. 
he User Management System should allow users to register, 
delete their account, and update their information.
"""

class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        
    def __repr__(self):
        return f"User(name={self.name}, email={self.email})"

class UserManagementSystem:
    def __init__(self):
        self.users = []
    def register(self, user):
        if user not in self.users:
            self.users.append(user)
        
    def delete_account(self, user):
        if user in self.users:
            self.users.remove(user)
        

    def update_info(self, user, new_info):
        if user in self.users:
            if 'name' in new_info:
                user.name = new_info['name']
            if 'email' in new_info:
                user.email = new_info['email']
                

"""
💎 Exercise 2: Quiz Application

Create a Quiz class that has a list of Questions. 
Each Question has a question, a list of options and a correct answer. 
The Quiz should allow questions to be added, and it should calculate the 
score of a user based on the answers they provide.
"""

class Question:
    def __init__(self, question, options, correct_answer):
        self.question = question
        self.options = options
        self.correct_answer = correct_answer

class Quiz:
    def __init__(self):
        self.questions = []
    def add_question(self, question):
        if question not in self.questions:
            self.questions.append(question)

    def calculate_score(self, user_answers):
        score = 0 
        for question in self.questions:
            user_answer = user_answers.get(question.question)
            if user_answer == question.correct_answer:
                score += 1
        return score

"""
💎 Exercise 3: Recipe Management System

Design a Recipe Management System. The Recipe class should have a name, 
a list of ingredients and the preparation steps. 
The Recipe Management System should allow recipes to be added, removed, 
and searched by ingredient.
"""

class Recipe:
    def __init__(self, name, ingredients, steps):
        self.name = name
        self.ingredients = ingredients
        self.steps = steps

class RecipeManagementSystem:
    def __init__(self):
        self.recipes = []
        
    def add_recipe(self, recipe):
        if recipe not in self.recipes:
            self.recipes.append(recipe)

    def remove_recipe(self, recipe):
        if recipe in self.recipes:
            self.recipes.remove(recipe)

    def search_by_ingredient(self, ingredient):
        found_recipes = [] 
        for recipe in self.recipes:
            if ingredient in recipe.ingredients:
                found_recipes.append(recipe) 
        
        return found_recipes
    
"""
💎 Exercise 4: Online Shopping System

Create a ShoppingCart class for an online shopping system. 
The Product class represents a product with name and price. 
The ShoppingCart should allow products to be added, removed, 
and it should calculate the total price of the products in the cart.
"""


class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

class ShoppingCart:
    def __init__(self):
        self.products = []
    def add_product(self, product):
        self.products.append(product)

    def remove_product(self, product):
        if product in self.products:
            self.products.remove(product)

    def calculate_total(self):
        total_price = 0
        for product in self.products:
            total_price += product.price 
        return total_price