from command.command import Command
from command.devices.garage_door import GarageDoor


class GarageDoorUpCommand(Command):
    def __init__(self, door: GarageDoor):
        self.door = door

    def execute(self):
        self.door.up()

    def undo(self):
        self.door.down()
