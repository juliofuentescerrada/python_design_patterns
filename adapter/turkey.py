from abc import abstractmethod, ABC

from common.output_writer import OutputWriter


class Turkey(ABC):
    @abstractmethod
    def gobble(self) -> None:
        raise NotImplementedError

    @abstractmethod
    def fly(self) -> None:
        raise NotImplementedError


class WildTurkey(Turkey):
    def __init__(self, output: OutputWriter):
        self.output = output

    def gobble(self) -> None:
        self.output.write('Gobble, gobble')

    def fly(self) -> None:
        self.output.write('I\'m flying a short distance')
