from common.output_writer import OutputWriter
from observer.observer import Observer
from observer.subject import Subject


class Display(Observer):
    def __init__(self, subject: Subject, output: OutputWriter):
        self.output = output
        self.subject = subject
        self.subject.register_observer(self)

    def update(self, temperature: float, humidity: float, pressure: float) -> None:
        self.output.write(f'Current conditions: {temperature}F degree and {humidity}% humidity')

