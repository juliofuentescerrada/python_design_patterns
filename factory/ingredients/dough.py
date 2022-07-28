from abc import ABC, abstractmethod


class Dough(ABC):
    @abstractmethod
    def get_name(self):
        raise NotImplementedError
