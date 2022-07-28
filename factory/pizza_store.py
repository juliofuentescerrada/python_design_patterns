from abc import ABC, abstractmethod

from factory.pizza import Pizza


class PizzaStore(ABC):
    def order_pizza(self, pizza_type: str) -> None:
        pizza = self.create_pizza(pizza_type)
        pizza.prepare()
        pizza.bake()
        pizza.cut()
        pizza.box()

    @abstractmethod
    def create_pizza(self, pizza_type: str) -> Pizza:
        raise NotImplementedError

