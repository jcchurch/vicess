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

    def getColAddresses(self, row):
        coladdys = []
        for address in self.__cells:
            parts = self.__parts(address)
            if parts(1) == row:
                coladdys.append(parts(0), address)
        coladdys.sort(key=lambda x: x[0])
        return [x[1] for x in coladdys]
 
    def getRowAddresses(self, col):
        rowaddys = []
        for address in self.__cells:
            parts = self.__parts(address)
            if parts(0) == col:
                rowaddys.append((int(parts(1)), address))
        rowaddys.sort(key=lambda x: x[0])
        return [x[1] for x in rowaddys]
 
    def getCellFormat(self, address):
        if address not in self.__cells:
            return ""

        return self.__cells[address].getFormat()

    def getPublicObject(self):
        c = {}
        for address in self.__cells:
            c[address] = self.__cells[address].getPublicObject()
        return c

    def __parts(self, address):
        if address[1].isdigit():
            return (address[0], address[1:])
        return (address[:2], address[2:])
