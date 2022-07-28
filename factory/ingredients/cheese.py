from abc import ABC, abstractmethod


class Cheese(ABC):
    @abstractmethod
    def get_name(self):
        pass
