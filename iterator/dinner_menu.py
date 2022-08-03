from typing import List

from iterator.dinner_menu_iterator import DinnerMenuIterator
from iterator.menu_item import MenuItem


class DinnerMenu:
    items: List[MenuItem] = []

    def __init__(self):
        self.items.append(MenuItem('Vegetarian BLT', 'Vegetarian BLT', 2.99))
        self.items.append(MenuItem('Soup of the day', 'Soup of the day', 3.29))
        self.items.append(MenuItem('Hot dog', 'Hot dog', 3.05))

    def create_iterator(self):
        return DinnerMenuIterator(self.items)
