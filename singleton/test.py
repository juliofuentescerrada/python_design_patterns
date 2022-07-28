import unittest

from singleton.chocolate_boiler import ChocolateBoiler


class SingletonTests(unittest.TestCase):
    @staticmethod
    def test_chocolate_boiler():
        instance_a = ChocolateBoiler()
        instance_b = ChocolateBoiler()

        instance_a.fill()
        assert instance_b.empty is False

        instance_b.boil()
        assert instance_a.boiled is True

        instance_a.drain()
        assert instance_b.empty is True


if __name__ == '__main__':
    unittest.main()
