from decorator.beverage import Beverage


class DarkRoast(Beverage):
    def __init__(self):
        self.description = 'Dark Roast'

    def cost(self) -> float:
        return .99


