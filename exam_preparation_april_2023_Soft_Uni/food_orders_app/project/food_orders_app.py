from typing import List

from project.client import Client
from project.meals.meal import Meal


class FoodOrdersApp:
    RECEIPT_ID = 0

    def __init__(self):
        self.menu: list = []
        self.clients_list: list = []

    def register_client(self, client_phone_number: str):
        if client_phone_number in [c.phone_number for c in self.clients_list]:
            raise Exception("The client has already been registered!")

        self.clients_list.append(Client(client_phone_number))
        return f"Client {client_phone_number} registered successfully."

    def add_meals_to_menu(self, *meals: Meal):
        valid_meals = ["Starter", "MainDish", "Dessert"]
        for meal in meals:
            if meal.__class__.__name__ in valid_meals:
                self.menu.append(meal)

    def menu_is_ready(self):
        if len(self.menu) < 5:
            raise Exception("The menu is not ready!")

    def show_menu(self):
        self.menu_is_ready()
        return '\n'.join(meal.details() for meal in self.menu)

    def get_client_object(self, client_phone_number):
        return [c for c in self.clients_list if client_phone_number == c.phone_number][0]

    def add_meals_to_shopping_cart(self, client_phone_number: str, **meal_names_and_quantities):
        self.menu_is_ready()

        if client_phone_number not in [c.phone_number for c in self.clients_list]:
            self.clients_list.append(Client(client_phone_number))

        client = self.get_client_object(client_phone_number)

        for meal_name, quantity in meal_names_and_quantities.items():
            if meal_name not in [m.name for m in self.menu]:
                raise Exception(f"{meal_name} is not on the menu!")

            meal = [m for m in self.menu if m.name == meal_name][0]
            if meal.quantity < quantity:
                raise Exception(f"Not enough quantity of {meal.__class__.__name__}: {meal_name}!")

        for meal_name, quantity in meal_names_and_quantities.items():
            meal = [m for m in self.menu if m.name == meal_name][0]
            client.shopping_cart.append(meal)
            client.shopping_cart_quantities.append(quantity)
            client.bill += meal.price * quantity
            meal.quantity -= quantity

        meal_names = ', '.join(m.name for m in client.shopping_cart)
        return f"Client {client_phone_number} successfully ordered {meal_names} for {client.bill:.2f}lv."

    def cancel_order(self, client_phone_number: str):
        client = self.get_client_object(client_phone_number)

        if len(client.shopping_cart) == 0:
            raise Exception("There are no ordered meals!")

        for i in range(len(client.shopping_cart)):
            for menu_meal in self.menu:
                if client.shopping_cart[i].name == menu_meal.name:
                    menu_meal.quantity += client.shopping_cart_quantities[i]

        client.shopping_cart = []
        client.shopping_cart_quantities = []
        client.bill = 0
        return f"Client {client_phone_number} successfully canceled his order."

    def finish_order(self, client_phone_number: str):
        client = self.get_client_object(client_phone_number)
        FoodOrdersApp.RECEIPT_ID += 1

        if len(client.shopping_cart) == 0:
            raise Exception("There are no ordered meals!")

        client.shopping_cart = []
        total_paid_money = client.bill
        client.bill = 0
        return f"Receipt #{FoodOrdersApp.RECEIPT_ID} with total amount of {total_paid_money:.2f} " \
               f"was successfully paid for {client_phone_number}."

    def __str__(self):
        return f"Food Orders App has {len(self.menu)} meals on the menu and {len(self.clients_list)} clients."