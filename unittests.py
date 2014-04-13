import unittest
from keymap import KeyMap
from action import ActionContext
from model import Model

class TestSequenceFunctions(unittest.TestCase):

    def setUp(self):
        self.model = Model()
        self.km = KeyMap()
        self.ac = ActionContext(self.km, self.model, None)

    def test_keymap_sequence(self):
        self.km.addCommand(106)
        demands = self.km.translate()
        self.assertTrue(demands == 'cursor_down')

    def test_down(self):
        self.km.addCommand(106)
        demands = self.km.translate()
        self.ac.do(demands)
        (x, y) = self.model.getCursor().getCursor()
        self.assertTrue(x == 0 and y == 1)

    def test_left(self):
        self.km.addCommand(108)
        demands = self.km.translate()
        self.ac.do(demands)
        (x, y) = self.model.getCursor().getCursor()
        self.assertTrue(x == 1 and y == 0)

    def test_looparound(self):
        self.km.addCommand(106)
        demands = self.km.translate()
        self.ac.do(demands)

        self.km.addCommand(108)
        demands = self.km.translate()
        self.ac.do(demands)

        self.km.addCommand(107)
        demands = self.km.translate()
        self.ac.do(demands)

        self.km.addCommand(104)
        demands = self.km.translate()
        self.ac.do(demands)

        (x, y) = self.model.getCursor().getCursor()
        self.assertTrue(x == 0 and y == 0)

if __name__ == '__main__':
    unittest.main()
