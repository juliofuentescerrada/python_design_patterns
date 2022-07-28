from abc import ABC, abstractmethod


class Sauce(ABC):
    @abstractmethod
    def get_name(self):
        raise NotImplementedError
