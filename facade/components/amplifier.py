from common.output_writer import OutputWriter


class Amplifier:
    def __init__(self, output: OutputWriter):
        self.output = output

    def on(self):
        self.output.write('Amplifier: ON')

    def off(self):
        self.output.write('Amplifier: OFF')

    def set_cd(self):
        self.output.write('Amplifier: SET CD')

    def set_dvd(self):
        self.output.write('Amplifier: SET DVD')

    def set_stereo_sound(self):
        self.output.write('Amplifier: SET STEREO SOUND')

    def set_surround_sound(self):
        self.output.write('Amplifier: SET SURROUND SOUND')

    def set_volume(self, volume: int):
        self.output.write(f'Amplifier: SET VOLUME TO {volume}')
