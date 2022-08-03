from common.output_writer import OutputWriter


class PopcornPopper:
    def __init__(self, output: OutputWriter):
        self.output = output

    def on(self):
        self.output.write('PopcornPopper: ON')

    def off(self):
        self.output.write('PopcornPopper: OFF')

    def pop(self):
        self.output.write(f'PopcornPopper: POP')
