from abc import ABC, abstractmethod


class Beverage(ABC):
    description: str = None

    def get_description(self) -> str:
        return self.description

    @abstractmethod
    def cost(self) -> float:
        pass
