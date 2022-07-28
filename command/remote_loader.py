from command.commands.ceiling_fan_off import CeilingFanOffCommand
from command.commands.ceiling_fan_on import CeilingFanOnCommand
from command.commands.garage_door_down import GarageDoorDownCommand
from command.commands.garage_door_up import GarageDoorUpCommand
from command.commands.light_off import LightOffCommand
from command.commands.light_on import LightOnCommand
from command.devices.ceiling_fan import CeilingFan
from command.devices.garage_door import GarageDoor
from command.devices.light import Light
from command.remote_control import RemoteControl
from common.output_writer import OutputWriter


class RemoteLoader:
    remote: RemoteControl = RemoteControl()
    living_room_light: Light = None
    kitchen_light: Light = None
    ceiling_fan: CeilingFan = None
    garage_door: GarageDoor = None

    def __init__(self, output: OutputWriter):
        self.initialize_devices(output)
        self.initialize_commands()

    def initialize_devices(self, output: OutputWriter):
        self.living_room_light = Light('living room light', output)
        self.kitchen_light = Light('kitchen light', output)
        self.ceiling_fan = CeilingFan('ceiling fan', output)
        self.garage_door = GarageDoor('garage door', output)

    def initialize_commands(self):
        living_room_light_on = LightOnCommand(self.living_room_light)
        living_room_light_off = LightOffCommand(self.living_room_light)
        self.remote.set_command(0, living_room_light_on, living_room_light_off)

        kitchen_light_on = LightOnCommand(self.kitchen_light)
        kitchen_light_off = LightOffCommand(self.kitchen_light)
        self.remote.set_command(1, kitchen_light_on, kitchen_light_off)

        ceiling_fan_on = CeilingFanOnCommand(self.ceiling_fan)
        ceiling_fan_off = CeilingFanOffCommand(self.ceiling_fan)
        self.remote.set_command(2, ceiling_fan_on, ceiling_fan_off)

        garage_door_up = GarageDoorUpCommand(self.garage_door)
        garage_door_down = GarageDoorDownCommand(self.garage_door)
        self.remote.set_command(3, garage_door_up, garage_door_down)
