from common.output_writer import OutputWriter


class Stereo:
    def __init__(self, name: str, output: OutputWriter):
        self.name = name
        self.output = output

    def on(self):
        self.output.write(f'{self.name} is on')

    def off(self):
        self.output.write(f'{self.name} is off')
