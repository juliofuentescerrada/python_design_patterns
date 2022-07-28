from common.output_writer import OutputWriter


class Screen:
    def __init__(self, output: OutputWriter):
        self.output = output

    def up(self):
        self.output.write('Screen: UP')

    def down(self):
        self.output.write('Screen: DOWN')
