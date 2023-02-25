class PizzaDelivery:
    ordered = []

    def __init__(self, name: str, price: float, ingredients: dict, ordered=False):
        self.name = name
        self.price = price
        self.ingredients = ingredients
        self.ordered = ordered

    def add_extra(self, ingredient: str, quantity: int, price_per_quantity: float):
        if self.name not in PizzaDelivery.ordered:
            if ingredient in self.ingredients.keys():
                self.ingredients[ingredient] += quantity
            else:
                self.ingredients[ingredient] = quantity

            self.price += price_per_quantity * quantity
        else:
            return f"Pizza {self.name} already prepared, and we can't make any changes!"

    def remove_ingredient(self, ingredient: str, quantity: int, price_per_quantity: float):
        if self.name in PizzaDelivery.ordered:
            return f"Pizza {self.name} already prepared, and we can't make any changes!"

        if ingredient not in self.ingredients.keys():
            return f"Wrong ingredient selected! We do not use {ingredient} in {self.name}!"
        elif ingredient in self.ingredients.keys() and quantity > self.ingredients[ingredient]:
            return f"Please check again the desired quantity of {ingredient}!"
        else:
            self.ingredients[ingredient] -= quantity
            self.price -= quantity * price_per_quantity

    def make_order(self):
        result = []
        for k, v in self.ingredients.items():
            result.append(f"{k}: {v}")
        result = ', '.join(result)
        if self.name not in PizzaDelivery.ordered:
            PizzaDelivery.ordered.append(self.name)
            self.ordered = True
            return f"You've ordered pizza {self.name} prepared with {result} " \
                   f"and the price will be {self.price}lv."
        return f"Pizza {self.name} already prepared, and we can't make any changes!"


margarita = PizzaDelivery('Margarita', 12, {'cheese': 2, 'tomatoes': 1})
margarita.add_extra('cheese', 1, 2)
margarita.add_extra('mozzarella', 1, 2.5)
margarita.remove_ingredient('cheese', 1, 1)
print(margarita.remove_ingredient('bacon', 1, 5))
print(margarita.remove_ingredient('tomatoes', 2, 2))
margarita.remove_ingredient('tomatoes', 1, 2)
print(margarita.make_order())
print(margarita.add_extra('mozzarella', 1, 2))



