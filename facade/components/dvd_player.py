from common.output_writer import OutputWriter


class DvdPlayer:
    def __init__(self, output: OutputWriter):
        self.output = output

    def on(self):
        self.output.write('DvdPlayer: ON')

    def off(self):
        self.output.write('DvdPlayer: OFF')

    def play(self, movie: str):
        self.output.write(f'DvdPlayer: PLAY {movie}')

    def stop(self):
        self.output.write(f'DvdPlayer: STOP')

    def stop(self):
        self.output.write(f'DvdPlayer: EJECT')
