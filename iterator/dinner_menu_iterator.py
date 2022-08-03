from typing import List

from iterator.iterator import Iterator
from iterator.menu_item import MenuItem


class DinnerMenuIterator(Iterator):
    position: int = 0

    def __init__(self, items: List[MenuItem]):
        self.items = items

    def has_next(self):
        if self.position >= len(self.items) or self.items[self.position] is None:
            return False
        else:
            return True

    def next(self):
        item = self.items[self.position]
        self.position += 1
        return item
