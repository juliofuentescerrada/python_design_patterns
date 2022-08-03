from template_method.beverage import Beverage


class Tea(Beverage):
    def brew(self):
        self.output.write('Steeping the tea')

    def add_condiments(self):
        self.output.write('Adding lemon')
