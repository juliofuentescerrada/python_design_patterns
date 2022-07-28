from abc import ABC, abstractmethod


class Clam(ABC):
    @abstractmethod
    def get_name(self):
        raise NotImplementedError
