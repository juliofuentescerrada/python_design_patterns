from command.command import Command


class NoCommand(Command):
    def execute(self):
        pass

    def undo(self):
        pass
