from abc import ABC, abstractmethod
from typing import List

from common.output_writer import OutputWriter
from factory.ingredients.ingredient_factory import IngredientFactory


class Pizza(ABC):
    def __init__(self, ingredient_factory: IngredientFactory, output: OutputWriter):
        self.ingredient_factory = ingredient_factory
        self.output = output
        self.name: str = ''
        self.dough: str = ''
        self.sauce: str = ''
        self.toppings: List[str] = []

    @abstractmethod
    def prepare(self) -> None:
        pass

    def bake(self) -> None:
        self.output.write('Bake for 25 minutes at 350')

    def cut(self) -> None:
        self.output.write('Cutting the pizza into diagonal slices')

    def box(self) -> None:
        self.output.write('Place pizza in official PizzaStore box')

    def set_name(self, name: str) -> None:
        self.name = name

    def get_name(self) -> str:
        return self.name
