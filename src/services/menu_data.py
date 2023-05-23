import pandas as pd
from models.dish import Ingredient
from models.dish import Dish


# Req 3
class MenuData:
    def __init__(self, source_path: str) -> None:
        self.menu = dict()
        self.dishes = set()
        csv_path = pd.read_csv(source_path).itertuples(index=False)

        for dish, price, ingredient, amount in csv_path:
            if dish not in self.menu.keys():
                self.menu[dish] = Dish(dish, price)
                self.dishes.add(self.menu[dish])

            new_ingredient = Ingredient(ingredient)
            self.menu[dish].add_ingredient_dependency(new_ingredient, amount)
