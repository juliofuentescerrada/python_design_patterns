from common.output_writer import OutputWriter
from factory.ingredients.newyork.newyork_ingredient_factory import NewYorkIngredientFactory
from factory.pizza import Pizza
from factory.pizza_store import PizzaStore
from factory.pizzas.cheese_pizza import CheesePizza
from factory.pizzas.clam_pizza import ClamPizza
from factory.pizzas.pepperoni_pizza import PepperoniPizza
from factory.pizzas.veggie_pizza import VeggiePizza


class NewYorkPizzaStore(PizzaStore):
    def __init__(self, output: OutputWriter):
        self.output = output
        self.ingredient_factory = NewYorkIngredientFactory()

    def create_pizza(self, pizza_type: str) -> Pizza:
        pizza: Pizza
        if pizza_type == 'cheese':
            pizza = CheesePizza(self.ingredient_factory, self.output)
            pizza.set_name('NY Style Sauce and Cheese Pizza')
        elif pizza_type == 'pepperoni':
            pizza = PepperoniPizza(self.ingredient_factory, self.output)
            pizza.set_name('NY Style Sauce and Pepperoni Pizza')
        elif pizza_type == 'veggie':
            pizza = VeggiePizza(self.ingredient_factory, self.output)
            pizza.set_name('NY Style Sauce and Veggies Pizza')
        elif pizza_type == 'clam':
            pizza = ClamPizza(self.ingredient_factory, self.output)
            pizza.set_name('NY Style Sauce and Clams Pizza')
        else:
            raise ValueError

        return pizza
