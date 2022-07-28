from abc import ABC, abstractmethod

from common.output_writer import OutputWriter


class Beverage(ABC):
    def __init__(self, output: OutputWriter):
        self.output = output

    def prepare_recipe(self):
        self.boil_water()
        self.brew()
        self.pour_in_cup()
        self.add_condiments()

    def boil_water(self):
        self.output.write('Boiling water')

    def pour_in_cup(self):
        self.output.write('Pouring into cup')

    @abstractmethod
    def brew(self):
        raise NotImplementedError

    @abstractmethod
    def add_condiments(self):
        raise NotImplementedError
