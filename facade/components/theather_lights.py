from common.output_writer import OutputWriter


class TheaterLights:
    def __init__(self, output: OutputWriter):
        self.output = output

    def on(self):
        self.output.write('TheaterLights: ON')

    def off(self):
        self.output.write('TheaterLights: OFF')

    def dim(self, value: int):
        self.output.write(f'TheaterLights: DIM LIGHTS TO {value}')

