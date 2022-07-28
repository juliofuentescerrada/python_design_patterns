from common.output_writer import OutputWriter


class Projector:
    def __init__(self, output: OutputWriter):
        self.output = output

    def on(self):
        self.output.write('Projector: ON')

    def off(self):
        self.output.write('Projector: OFF')

    def set_wide_mode(self):
        self.output.write(f'Projector: SET WIDE MODE')
