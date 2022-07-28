from factory.ingredients.cheese import Cheese
from factory.ingredients.chicago.chicago_cheese import ChicagoCheese
from factory.ingredients.chicago.chicago_clam import ChicagoClam
from factory.ingredients.chicago.chicago_dough import ChicagoDough
from factory.ingredients.chicago.chicago_pepperoni import ChicagoPepperoni
from factory.ingredients.chicago.chicago_sauce import ChicagoSauce
from factory.ingredients.chicago.chicago_veggie import ChicagoVeggie
from factory.ingredients.clam import Clam
from factory.ingredients.dough import Dough
from factory.ingredients.ingredient_factory import IngredientFactory
from factory.ingredients.pepperoni import Pepperoni
from factory.ingredients.sauce import Sauce
from factory.ingredients.veggie import Veggie


class ChicagoIngredientFactory(IngredientFactory):
    def create_dough(self) -> Dough:
        return ChicagoDough()

    def create_sauce(self) -> Sauce:
        return ChicagoSauce()

    def create_cheese(self) -> Cheese:
        return ChicagoCheese()

    def create_pepperoni(self) -> Pepperoni:
        return ChicagoPepperoni()

    def create_veggies(self) -> Veggie:
        return ChicagoVeggie()

    def create_clam(self) -> Clam:
        return ChicagoClam()
