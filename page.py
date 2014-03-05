from cell import Cell

class Page:
    def __init__(self): 
        self.__cells = {}

    def updateCellContent(self, address, content):
        if address not in self.__cells:
            self.__cells[address] = Cell(content)
        else:
            self.__cells[address].update(content)

    def updateCellFormat(self, address, form):
        if address not in self.__cells:
            self.__cells[address] = Cell("", form)
        else:
            self.__cells[address].updateFormat(form)

    def getCell(self, address):
        if address not in self.__cells:
            return ""

        return self.__cells[address].getRawContent()
 
    def getCellFormat(self, address):
        if address not in self.__cells:
            return ""

        return self.__cells[address].getFormat()

    def getPublicObject(self):
        c = {}
        for address in self.__cells:
            c[address] = self.__cells[address].getPublicObject()
        return c
