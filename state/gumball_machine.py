from common.output_writer import OutputWriter
from state.gumball_state import GumballState
from state.states.has_quarter_state import HasQuarterState
from state.states.no_quarter_state import NoQuarterState
from state.states.sold_state import SoldState
from state.states.soldout_state import SoldOutState


class GumballMachine:
    gumballs: int = 0
    state: GumballState = None
    sold_out: SoldOutState = None
    no_quarter: NoQuarterState = None
    has_quarter: HasQuarterState = None
    sold: SoldState = None

    def __init__(self, gumballs: int, output: OutputWriter):
        self.output = output
        self.sold_out = SoldOutState(self, output)
        self.no_quarter = NoQuarterState(self, output)
        self.has_quarter = HasQuarterState(self, output)
        self.sold = SoldState(self, output)
        self.fill(gumballs)

    def fill(self, gumballs: int):
        self.gumballs = gumballs if gumballs > 0 else 0
        self.state = self.no_quarter if gumballs > 0 else self.sold_out

    def insert_quarter(self):
        self.state.insert_quarter()

    def eject_quarter(self):
        self.state.eject_quarter()

    def turn_crank(self):
        self.state.turn_crank()
        self.state.dispense()

    def release(self):
        self.output.write('A gumball comes rolling out the slot...')
        if self.gumballs > 0:
            self.gumballs -= 1
