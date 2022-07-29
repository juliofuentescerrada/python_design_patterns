import unittest
from unittest.mock import MagicMock, call

from state.gumball_machine import GumballMachine


class StateTests(unittest.TestCase):
    def setUp(self):
        self.output = MagicMock()

    def test_gumball_machine(self):
        machine = GumballMachine(5, self.output)
        machine.insert_quarter()
        machine.eject_quarter()
        machine.insert_quarter()
        machine.turn_crank()
        machine.eject_quarter()

        calls = [
            call('You inserted a quarter'),
            call('Your quarter was returned'),
            call('You inserted a quarter'),
            call('You turned the crank...'),
            call('A gumball comes rolling out the slot...'),
            call('You haven\'t inserted a quarter'),
        ]

        self.output.write.assert_has_calls(calls)


if __name__ == '__main__':
    unittest.main()
