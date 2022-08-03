from factory.ingredients.cheese import Cheese
from factory.ingredients.clam import Clam
from factory.ingredients.dough import Dough
from factory.ingredients.ingredient_factory import IngredientFactory
from factory.ingredients.newyork.newyork_cheese import NewYorkCheese
from factory.ingredients.newyork.newyork_clam import NewYorkClam
from factory.ingredients.newyork.newyork_dough import NewYorkDough
from factory.ingredients.newyork.newyork_pepperoni import NewYorkPepperoni
from factory.ingredients.newyork.newyork_sauce import NewYorkSauce
from factory.ingredients.newyork.newyork_veggie import NewYorkVeggie
from factory.ingredients.pepperoni import Pepperoni
from factory.ingredients.sauce import Sauce
from factory.ingredients.veggie import Veggie


class NewYorkIngredientFactory(IngredientFactory):
    def create_dough(self) -> Dough:
        return NewYorkDough()

    def create_sauce(self) -> Sauce:
        return NewYorkSauce()

    def create_cheese(self) -> Cheese:
        return NewYorkCheese()

    def create_pepperoni(self) -> Pepperoni:
        return NewYorkPepperoni()

    def create_veggies(self) -> Veggie:
        return NewYorkVeggie()

    def create_clam(self) -> Clam:
        return NewYorkClam()
