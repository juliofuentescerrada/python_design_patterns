from common.output_writer import OutputWriter
from observer.display import Display
from observer.weather_data import WeatherData
from strategy.mallard_duck import MallardDuck


class ConsoleOutputWriter(OutputWriter):
    def write(self, output: str) -> None:
        print(output)


def run() -> None:
    output = ConsoleOutputWriter()

    # Strategy
    duck = MallardDuck(output)
    duck.perform_fly()
    duck.perform_quack()

    # Observer
    weather_data = WeatherData()
    Display(weather_data, output)
    weather_data.set_measurements(36, 45, 50)


if __name__ == '__main__':
    run()
