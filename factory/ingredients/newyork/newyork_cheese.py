from factory.ingredients.cheese import Cheese


class NewYorkCheese(Cheese):
    def get_name(self):
        return 'NewYork cheese'
