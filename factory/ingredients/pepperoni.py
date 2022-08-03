from abc import ABC, abstractmethod


class Pepperoni(ABC):
    @abstractmethod
    def get_name(self):
        pass
