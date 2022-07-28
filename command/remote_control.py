from typing import List

from command.command import Command
from command.commands.no_command import NoCommand


class RemoteControl:
    undo_command: Command = None

    def __init__(self):
        self.on_commands: List[Command] = [NoCommand()] * 8
        self.off_commands: List[Command] = [NoCommand()] * 8

    def set_command(self, index: int, on_command: Command, off_command: Command):
        self.on_commands[index] = on_command
        self.off_commands[index] = off_command

    def press_on_button(self, index: int):
        self.on_commands[index].execute()
        self.undo_command = self.on_commands[index]

    def press_off_button(self, index: int):
        self.off_commands[index].execute()
        self.undo_command = self.off_commands[index]

    def press_undo_button(self):
        if self.undo_command is not None:
            self.undo_command.undo()

