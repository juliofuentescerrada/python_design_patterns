from factory.ingredients.pepperoni import Pepperoni


class NewYorkPepperoni(Pepperoni):
    def get_name(self):
        return 'NewYork pepperoni'
