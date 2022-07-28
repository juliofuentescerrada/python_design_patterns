import unittest
from unittest.mock import MagicMock

from factory.stores.chicago_pizza_store import ChicagoPizzaStore
from factory.stores.newyork_pizza_store import NewYorkPizzaStore


class FactoryPatternTests(unittest.TestCase):
    def setUp(self):
        self.output = MagicMock()

    def test_pizza_store_factory(self):
        ny_pizza_store = NewYorkPizzaStore(self.output)
        ny_pizza_store.order_pizza('cheese')
        self.output.write.assert_any_call('Preparing NY Style Sauce and Cheese Pizza')

        chicago_pizza_store = ChicagoPizzaStore(self.output)
        chicago_pizza_store.order_pizza('pepperoni')
        self.output.write.assert_any_call('Preparing Chicago Style Deep Dish Pepperoni Pizza')


if __name__ == '__main__':
    unittest.main()
