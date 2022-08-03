import unittest
from unittest.mock import MagicMock

from command.commands.light_on import LightOnCommand
from command.devices.light import Light
from command.remote_loader import RemoteLoader
from command.simple_remote_control import SimpleRemoteControl


class CommandTests(unittest.TestCase):
    def setUp(self):
        self.output = MagicMock()

    def test_simple_remote(self):
        light = Light('room light', self.output)
        command = LightOnCommand(light)

        remote = SimpleRemoteControl()
        remote.set_command(command)
        remote.press_button()

        self.output.write.assert_called_with('room light is on')

    def test_remote_control(self):
        loader = RemoteLoader(self.output)
        remote = loader.remote

        remote.press_on_button(0)
        self.output.write.assert_called_with('living room light is on')

        remote.press_off_button(0)
        self.output.write.assert_called_with('living room light is off')

        remote.press_on_button(1)
        self.output.write.assert_called_with('kitchen light is on')

        remote.press_off_button(1)
        self.output.write.assert_called_with('kitchen light is off')

        remote.press_on_button(2)
        self.output.write.assert_called_with('ceiling fan is on')

        remote.press_off_button(2)
        self.output.write.assert_called_with('ceiling fan is off')

        remote.press_on_button(3)
        self.output.write.assert_called_with('garage door is up')

        remote.press_off_button(3)
        self.output.write.assert_called_with('garage door is down')

        remote.press_undo_button()
        self.output.write.assert_called_with('garage door is up')


if __name__ == '__main__':
    unittest.main()
