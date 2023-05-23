from src.models.dish import Dish  # noqa: F401, E261, E501
import pytest as pt
from src.models.ingredient import Ingredient, Restriction


# Req 2
def test_dish():
    with pt.raises(TypeError):
        Dish("Pizza", "João")
    with pt.raises(ValueError):
        Dish("Pizza", -50.00)

    repr_response = "Dish('Pizza', R$50.00)"
    apple_pie = Dish("Apple Pie", 45.00)
    pizza = Dish("Pizza", 50.00)
    pizza.add_ingredient_dependency(Ingredient("bacon"), 7)
    pizza.add_ingredient_dependency(Ingredient("carne"), 5)
    pizza.add_ingredient_dependency(Ingredient("queijo mussarela"), 12)

    assert Dish("Pizza", 50.00).name == "Pizza"
    assert Dish("Pizza", 50.00).price == 50.00
    assert Dish("Pizza", 50.00).__repr__() == repr_response
    assert Dish("Pizza", 50.00).__eq__(pizza) is True
    assert Dish("Pizza", 50.00).__eq__(apple_pie) is False
    assert Dish("Pizza", 50.00).__hash__() == hash(repr_response)
    assert pizza.get_ingredients() == {
        Ingredient("bacon"),
        Ingredient("carne"),
        Ingredient("queijo mussarela")
    }
    assert pizza.get_restrictions() == {
        Restriction.ANIMAL_DERIVED,
        Restriction.ANIMAL_MEAT,
        Restriction.LACTOSE,
    }
