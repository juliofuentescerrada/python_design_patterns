import unittest

from decorator.beverages.dark_roast import DarkRoast
from decorator.beverages.espresso import Espresso
from decorator.condiments.mocha import Mocha
from decorator.condiments.whip import Whip


class DecoratorPatternTestCase(unittest.TestCase):

    @staticmethod
    def test_beverages():
        beverage = Espresso()

        assert beverage.get_description() == 'Espresso'
        assert beverage.cost() == 1.99

        beverage = DarkRoast()
        beverage = Mocha(beverage)
        beverage = Mocha(beverage)
        beverage = Whip(beverage)

        assert beverage.get_description() == 'Dark Roast, Mocha, Mocha, Whip'
        assert beverage.cost() == 1.49


if __name__ == '__main__':
    unittest.main()
