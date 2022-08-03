from common.output_writer import OutputWriter
from strategy.behaviors.quack.quack_behavior import QuackBehavior


class MuteQuackBehavior(QuackBehavior):
    def __init__(self, output: OutputWriter):
        self._output = output

    def quack(self) -> None:
        self._output.write('<< silence >>')
