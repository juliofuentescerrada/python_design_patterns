from abc import ABC, abstractmethod

from factory.ingredients.cheese import Cheese
from factory.ingredients.clam import Clam
from factory.ingredients.dough import Dough
from factory.ingredients.pepperoni import Pepperoni
from factory.ingredients.sauce import Sauce
from factory.ingredients.veggie import Veggie


class IngredientFactory(ABC):
    @abstractmethod
    def create_dough(self) -> Dough:
        raise NotImplementedError

    @abstractmethod
    def create_sauce(self) -> Sauce:
        raise NotImplementedError

    @abstractmethod
    def create_cheese(self) -> Cheese:
        raise NotImplementedError

    @abstractmethod
    def create_pepperoni(self) -> Pepperoni:
        raise NotImplementedError

    @abstractmethod
    def create_veggies(self) -> Veggie:
        raise NotImplementedError

    @abstractmethod
    def create_clam(self) -> Clam:
        raise NotImplementedError
