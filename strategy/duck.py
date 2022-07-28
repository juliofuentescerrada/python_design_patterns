from abc import ABC

from strategy.behaviors.fly.wings import FlyBehavior
from strategy.behaviors.quack.quack_behavior import QuackBehavior


class Duck(ABC):
    def __init__(self, quack: QuackBehavior, fly: FlyBehavior):
        if quack is None:
            raise ValueError('quack')

        if fly is None:
            raise ValueError('fly')

        self._quackBehavior = quack
        self._flyBehavior = fly

    def change_quack_behavior(self, quack: QuackBehavior) -> None:
        self._quackBehavior = quack

    def perform_quack(self) -> None:
        self._quackBehavior.quack()

    def change_fly_behavior(self, fly: FlyBehavior) -> None:
        self._flyBehavior = fly

    def perform_fly(self) -> None:
        self._flyBehavior.fly()
