from abc import ABC, abstractmethod

from common.output_writer import OutputWriter


class Duck(ABC):
    @abstractmethod
    def quack(self) -> None:
        pass

    @abstractmethod
    def fly(self) -> None:
        pass


class MallardDuck(Duck):
    def __init__(self, output: OutputWriter):
        self.output = output

    def quack(self) -> None:
        self.output.write('Quack')

    def fly(self) -> None:
        self.output.write('I\'m flying')
