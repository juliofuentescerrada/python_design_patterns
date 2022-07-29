from common.output_writer import OutputWriter
from state.gumball_state import GumballState


class HasQuarterState(GumballState):
    def __init__(self, machine, output: OutputWriter):
        self.machine = machine
        self.output = output

    def insert_quarter(self):
        self.output.write('You can\'t insert another quarter')

    def eject_quarter(self):
        self.output.write('Your quarter was returned')
        self.machine.state = self.machine.no_quarter

    def turn_crank(self):
        self.output.write('You turned the crank...')
        self.machine.state = self.machine.sold

    def dispense(self):
        self.output.write('No gumball dispensed')
