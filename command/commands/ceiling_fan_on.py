from command.command import Command
from command.devices.ceiling_fan import CeilingFan


class CeilingFanOnCommand(Command):
    def __init__(self, fan: CeilingFan):
        self.fan = fan

    def execute(self):
        self.fan.on()

    def undo(self):
        self.fan.off()
