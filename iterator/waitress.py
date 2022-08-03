from common.output_writer import OutputWriter
from iterator.dinner_menu import DinnerMenu
from iterator.iterator import Iterator


class Waitress:
    def __init__(self, menu: DinnerMenu, output: OutputWriter):
        self.menu = menu
        self.output = output

    def print_menu(self):
        menu_iterator = self.menu.create_iterator()
        self.print_items(menu_iterator)

    def print_items(self, iterator: Iterator):
        while iterator.has_next():
            item = iterator.next()
            self.output.write(f'{item.name}, {item.price} -- {item.description}')