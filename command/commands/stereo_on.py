from command.command import Command
from command.devices.stereo import Stereo


class StereoOnCommand(Command):
    def __init__(self, stereo: Stereo):
        self.stereo = stereo

    def execute(self):
        self.stereo.on()

    def undo(self):
        self.stereo.off()
