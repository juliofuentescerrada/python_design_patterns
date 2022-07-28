from typing import List

from observer.observer import Observer
from observer.subject import Subject


class WeatherData(Subject):
    def __init__(self):
        self._observers: List[Observer] = []
        self.temperature = 0
        self.humidity = 0
        self.pressure = 0

    def register_observer(self, observer: Observer) -> None:
        self._observers.append(observer)

    def remove_observer(self, observer: Observer) -> None:
        self._observers.remove(observer)

    def notify_observers(self) -> None:
        for o in self._observers:
            o.update(self.temperature, self.humidity, self.pressure)

    def set_measurements(self, temperature: float, humidity: float, pressure: float):
        self.temperature = temperature
        self.humidity = humidity
        self.pressure = pressure
        self.notify_observers()
