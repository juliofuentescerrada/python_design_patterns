import unittest
from unittest.mock import MagicMock

from observer.display import Display
from observer.weather_data import WeatherData


class ObserverPatternTests(unittest.TestCase):
    def setUp(self):
        self.output = MagicMock()

    def test_weather_display(self):
        weather_data = WeatherData()
        Display(weather_data, self.output)
        weather_data.set_measurements(10, 10, 10)
        self.output.write.assert_called_with('Current conditions: 10F degree and 10% humidity')


if __name__ == '__main__':
    unittest.main()
