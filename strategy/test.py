import unittest
from unittest.mock import MagicMock

from strategy.behaviors.fly.rocket import FlyWithRocketBehavior
from strategy.behaviors.quack.mute import MuteQuackBehavior
from strategy.mallard_duck import MallardDuck


class StrategyPatternTestCase(unittest.TestCase):
    def setUp(self):
        self.output = MagicMock()

    def test_should_fly(self):
        duck = MallardDuck(self.output)
        duck.perform_fly()
        self.output.write.assert_called_with('Flying with wings')

    def test_should_change_fly_behavior(self):
        duck = MallardDuck(self.output)
        duck.change_fly_behavior(FlyWithRocketBehavior(self.output))
        duck.perform_fly()
        self.output.write.assert_called_with('I\'m flying with a rocket! 🚀')

    def test_should_quack(self):
        duck = MallardDuck(self.output)
        duck.perform_quack()
        self.output.write.assert_called_with('Quack, quack')

    def test_should_change_quack_behavior(self):
        duck = MallardDuck(self.output)
        duck. change_quack_behavior(MuteQuackBehavior(self.output))
        duck.perform_quack()
        self.output.write.assert_called_with('<< silence >>')


if __name__ == '__main__':
    unittest.main()
