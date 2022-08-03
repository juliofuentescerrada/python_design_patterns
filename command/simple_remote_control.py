from command.command import Command


class SimpleRemoteControl:
    slot: Command = None

    def set_command(self, command: Command):
        self.slot = command

    def press_button(self):
        self.slot.execute()
