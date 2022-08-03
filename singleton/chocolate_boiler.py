from threading import Lock


class SingletonMeta(type):
    _instances = {}
    _lock: Lock = Lock()

    def __call__(cls, *args, **kwargs):
        with cls._lock:
            if cls not in cls._instances:
                instance = super().__call__(*args, **kwargs)
                cls._instances[cls] = instance

        return cls._instances[cls]


class ChocolateBoiler(metaclass=SingletonMeta):
    def __init__(self):
        self.empty: bool = True
        self.boiled: bool = False

    def fill(self):
        if self.empty:
            self.empty = False
            self.empty = False

    def drain(self):
        if not self.empty and self.boiled:
            self.empty = True

    def boil(self):
        if not self.empty and not self.boiled:
            self.boiled = True
