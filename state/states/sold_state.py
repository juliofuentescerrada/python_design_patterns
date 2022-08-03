from common.output_writer import OutputWriter
from state.gumball_state import GumballState


class SoldState(GumballState):
    def __init__(self, machine, output: OutputWriter):
        self.machine = machine
        self.output = output

    def insert_quarter(self):
        self.output.write('Please wait, we\'re already giving you a gumball')

    def eject_quarter(self):
        self.output.write('Sorry, you already turned the crank')

    def turn_crank(self):
        self.output.write('Turning twice doesn\'t get you another gumball!')

    def dispense(self):
        self.machine.release()
        self.machine.state = self.machine.no_quarter if self.machine.gumballs > 0 else self.machine.sold_out
