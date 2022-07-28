from decorator.beverage import Beverage


class HoseBlend(Beverage):
    def __init__(self):
        self.description = 'House Blend Coffee'

    def cost(self) -> float:
        return .89


