from common.output_writer import OutputWriter


class Tuner:
    def __init__(self, output: OutputWriter):
        self.output = output

    def on(self):
        self.output.write('Tuner: ON')

    def off(self):
        self.output.write('Tuner: OFF')
