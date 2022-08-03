import unittest
from unittest.mock import MagicMock, call

from iterator.dinner_menu import DinnerMenu
from iterator.waitress import Waitress


class IteratorTests(unittest.TestCase):
    def setUp(self):
        self.output = MagicMock()

    def test_dinner_menu(self):
        menu = DinnerMenu()
        waitress = Waitress(menu, self.output)
        waitress.print_menu()

        calls = [
            call('Vegetarian BLT, 2.99 -- Vegetarian BLT'),
            call('Soup of the day, 3.29 -- Soup of the day'),
            call('Hot dog, 3.05 -- Hot dog'),
        ]

        self.output.write.assert_has_calls(calls)


if __name__ == '__main__':
    unittest.main()
