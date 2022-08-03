import unittest
from unittest.mock import MagicMock, call

from template_method.coffee import Coffee
from template_method.tea import Tea


class TemplateMethodTests(unittest.TestCase):
    def setUp(self) -> None:
        self.output = MagicMock()

    def test_coffee(self):
        coffee = Coffee(self.output)
        coffee.prepare_recipe()

        calls = [
            call('Boiling water'),
            call('Dripping coffee through filter'),
            call('Pouring into cup'),
            call('Adding sugar and milk'),
        ]

        self.output.write.assert_has_calls(calls)

    def test_tea(self):
        tea = Tea(self.output)
        tea.prepare_recipe()

        calls = [
            call('Boiling water'),
            call('Steeping the tea'),
            call('Pouring into cup'),
            call('Adding lemon'),
        ]

        self.output.write.assert_has_calls(calls)
