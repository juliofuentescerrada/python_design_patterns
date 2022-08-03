from adapter.duck import Duck
from adapter.turkey import Turkey


class TurkeyAdapter(Duck):
    def __init__(self, turkey: Turkey):
        self.turkey = turkey

    def quack(self) -> None:
        self.turkey.gobble()

    def fly(self) -> None:
        for i in range(5):
            self.turkey.fly()

