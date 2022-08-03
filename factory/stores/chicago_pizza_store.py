from common.output_writer import OutputWriter
from factory.ingredients.chicago.chicago_ingredient_factory import ChicagoIngredientFactory
from factory.pizza import Pizza
from factory.pizza_store import PizzaStore
from factory.pizzas.cheese_pizza import CheesePizza
from factory.pizzas.clam_pizza import ClamPizza
from factory.pizzas.pepperoni_pizza import PepperoniPizza
from factory.pizzas.veggie_pizza import VeggiePizza


class ChicagoPizzaStore(PizzaStore):
    def __init__(self, output: OutputWriter):
        self.output = output
        self.ingredient_factory = ChicagoIngredientFactory()

    def create_pizza(self, pizza_type: str) -> Pizza:
        pizza: Pizza
        if pizza_type == 'cheese':
            pizza = CheesePizza(self.ingredient_factory, self.output)
            pizza.set_name('Chicago Style Deep Dish Cheese Pizza')
        elif pizza_type == 'pepperoni':
            pizza = PepperoniPizza(self.ingredient_factory, self.output)
            pizza.set_name('Chicago Style Deep Dish Pepperoni Pizza')
        elif pizza_type == 'veggie':
            pizza = VeggiePizza(self.ingredient_factory, self.output)
            pizza.set_name('Chicago Style Deep Dish Veggies Pizza')
        elif pizza_type == 'clam':
            pizza = ClamPizza(self.ingredient_factory, self.output)
            pizza.set_name('Chicago Style Deep Dish Clams Pizza')
        else:
            raise ValueError

        return pizza
