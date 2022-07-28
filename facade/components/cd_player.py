from common.output_writer import OutputWriter


class CdPlayer:
    def __init__(self, output: OutputWriter):
        self.output = output

    def on(self):
        self.output.write('CdPlayer: ON')

    def off(self):
        self.output.write('CdPlayer: OFF')

    def play(self, album: str):
        self.output.write(f'CdPlayer: PLAY {album}')