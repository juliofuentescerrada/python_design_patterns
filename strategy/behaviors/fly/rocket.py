from common.output_writer import OutputWriter
from strategy.behaviors.fly.fly_behavior import FlyBehavior


class FlyWithRocketBehavior(FlyBehavior):
    def __init__(self, output: OutputWriter):
        self._output = output

    def fly(self) -> None:
        self._output.write('I\'m flying with a rocket! 🚀')
