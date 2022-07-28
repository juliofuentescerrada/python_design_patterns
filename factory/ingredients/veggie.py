from abc import ABC, abstractmethod


class Veggie(ABC):
    @abstractmethod
    def get_name(self):
        pass
