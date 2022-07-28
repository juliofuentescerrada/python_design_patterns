from common.output_writer import OutputWriter
from strategy.behaviors.fly.wings import FlyWithWingsBehavior
from strategy.behaviors.quack.quack import DefaultQuackBehavior
from strategy.duck import Duck


class MallardDuck(Duck):
    def __init__(self, output: OutputWriter):
        super().__init__(DefaultQuackBehavior(output), FlyWithWingsBehavior(output))
