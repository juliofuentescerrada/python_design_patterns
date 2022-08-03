from abc import ABC, abstractmethod


class OutputWriter(ABC):
    @abstractmethod
    def write(self, output: str) -> None:
        pass
