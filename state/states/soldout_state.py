from common.output_writer import OutputWriter
from state.gumball_state import GumballState


class SoldOutState(GumballState):
    def __init__(self, machine, output: OutputWriter):
        self.machine = machine
        self.output = output

    def insert_quarter(self):
        self.output.write('Sorry, there are no gumballs left')

    def eject_quarter(self):
        self.output.write('You haven\'t inserted a quarter')

    def turn_crank(self):
        self.output.write('You turned but there\'s no quarter')

    def dispense(self):
        self.output.write('You need to pay first')
