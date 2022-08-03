from common.output_writer import OutputWriter


class GarageDoor:
    def __init__(self, name: str, output: OutputWriter):
        self.name = name
        self.output = output

    def up(self):
        self.output.write(f'{self.name} is up')

    def down(self):
        self.output.write(f'{self.name} is down')
