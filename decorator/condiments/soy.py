from decorator.beverage import Beverage
from decorator.condiment_decorator import CondimentDecorator


class Soy(CondimentDecorator):
    def __init__(self, beverage: Beverage):
        self.beverage = beverage

    def get_description(self) -> str:
        return self.beverage.get_description() + ', Soy'

    def cost(self) -> float:
        return self.beverage.cost() + .15

