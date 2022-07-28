from common.output_writer import OutputWriter
from factory.ingredients.ingredient_factory import IngredientFactory
from factory.pizza import Pizza


class PepperoniPizza(Pizza):
    def __init__(self, ingredient_factory: IngredientFactory, output: OutputWriter):
        super().__init__(ingredient_factory, output)
        self.dough = self.ingredient_factory.create_dough()
        self.sauce = self.ingredient_factory.create_sauce()
        self.cheese = self.ingredient_factory.create_cheese()
        self.pepperoni = self.ingredient_factory.create_pepperoni()

    def prepare(self) -> None:
        self.output.write(f'Preparing {self.name}')

