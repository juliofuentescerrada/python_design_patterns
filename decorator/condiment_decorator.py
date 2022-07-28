from abc import ABC, abstractmethod
from decorator.beverage import Beverage


class CondimentDecorator(Beverage, ABC):

    @abstractmethod
    def get_description(self) -> str:
        raise NotImplementedError
