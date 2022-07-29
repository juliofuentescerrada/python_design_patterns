from common.output_writer import OutputWriter
from state.gumball_state import GumballState


class NoQuarterState(GumballState):
    def __init__(self, machine, output: OutputWriter):
        self.machine = machine
        self.output = output

    def insert_quarter(self):
        self.output.write('You inserted a quarter')
        self.machine.state = self.machine.has_quarter

    def eject_quarter(self):
        self.output.write('You haven\'t inserted a quarter')

    def turn_crank(self):
        self.output.write('You turned but there\'s no quarter')

    def dispense(self):
        self.output.write('You need to pay first')
