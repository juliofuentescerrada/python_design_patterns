from abc import ABC, abstractmethod


class Iterator(ABC):
    @abstractmethod
    def has_next(self):
        raise NotImplementedError

    @abstractmethod
    def next(self):
        raise NotImplementedError
