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
        self.km.addCommand('j')
        demands = self.km.translate()
        self.assertTrue(demands == 'cursor_down')

    def test_down(self):
        self.km.addCommand('j')
        demands = self.km.translate()
        self.ac.do(demands)
        (x, y) = self.model.getCursor().getCursor()
        self.assertTrue(x == 0 and y == 1)

    def test_left(self):
        self.km.addCommand('l')
        demands = self.km.translate()
        self.ac.do(demands)
        (x, y) = self.model.getCursor().getCursor()
        self.assertTrue(x == 1 and y == 0)

    def test_looparound(self):
        self.km.addCommand('j')
        demands = self.km.translate()
        self.ac.do(demands)

        self.km.addCommand('l')
        demands = self.km.translate()
        self.ac.do(demands)

        self.km.addCommand('k')
        demands = self.km.translate()
        self.ac.do(demands)

        self.km.addCommand('h')
        demands = self.km.translate()
        self.ac.do(demands)

        (x, y) = self.model.getCursor().getCursor()
        self.assertTrue(x == 0 and y == 0)

    def test_insert(self):
        sample_text = "This is sample text"
        sheet = self.model.getSheet()
        cursor = self.model.getCursor()
        cursor.setCellAtCursor(sheet, sample_text)
        cell = cursor.getCell(sheet)
        self.assertTrue(cell.getRawContent() == sample_text)

    def test_discernText(self):
        sample_text = "This is sample text"
        sheet = self.model.getSheet()
        cursor = self.model.getCursor()
        cursor.setCellAtCursor(sheet, sample_text)
        cell = cursor.getCell(sheet)
        self.assertTrue(cell.getType() == "Text")

    def test_discernNumeric(self):
        sample_text = "3.14159"
        sheet = self.model.getSheet()
        cursor = self.model.getCursor()
        cursor.setCellAtCursor(sheet, sample_text)
        cell = cursor.getCell(sheet)
        self.assertTrue(cell.getType() == "Numeric")

    def test_discernFormula(self):
        sample_text = "=sum(A1:A10)"
        sheet = self.model.getSheet()
        cursor = self.model.getCursor()
        cursor.setCellAtCursor(sheet, sample_text)
        cell = cursor.getCell(sheet)
        self.assertTrue(cell.getType() == "Formula")

if __name__ == '__main__':
    unittest.main()
