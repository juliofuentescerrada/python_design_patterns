import unittest
from unittest.mock import MagicMock

from adapter.turkey import WildTurkey
from adapter.turkey_adapter import TurkeyAdapter


class AdapterTests(unittest.TestCase):
    def setUp(self) -> None:
        self.output = MagicMock()

    def test_turkey_adapter(self):
        turkey = WildTurkey(self.output)
        duck = TurkeyAdapter(turkey)

        duck.quack()
        self.output.write.assert_called_with('Gobble, gobble')

        duck.fly()
        self.output.write.assert_called_with('I\'m flying a short distance')


if __name__ == '__main__':
    unittest.main()
