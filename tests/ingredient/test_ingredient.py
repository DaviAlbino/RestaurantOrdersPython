from src.models.ingredient import Ingredient, Restriction  # noqa: F401, E261, E501


# Req 1
def test_ingredient():
    rest_meat = Restriction.ANIMAL_MEAT
    rest_derived = Restriction.ANIMAL_DERIVED
    repr_response = "Ingredient('queijo mussarela')"
    hash_response = hash("queijo mussarela")
    egg = Ingredient("ovo")
    assert Ingredient("queijo mussarela").name == "queijo mussarela"
    assert Ingredient("queijo mussarela").__repr__() == repr_response
    assert Ingredient("queijo mussarela").__hash__() == hash_response
    assert Ingredient("ovo").__eq__(egg) is True
    assert Ingredient("carne").restrictions == {rest_meat, rest_derived}
