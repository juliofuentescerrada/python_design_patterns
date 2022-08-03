from template_method.beverage import Beverage


class Coffee(Beverage):
    def brew(self):
        self.output.write('Dripping coffee through filter')

    def add_condiments(self):
        self.output.write('Adding sugar and milk')
