from page import Page

class Sheet:
    def __init__(self): 
        self.__pages = {}
        self.__current = "Main"
        self.__pages[self.__current] = Page()

    def getCurrentPage(self):
        return self.__pages[self.__current]

    def getLastRowInPage(self, col):
        rows = self.__pages[self.__current].getRowAddresses(col)
        return rows[-1]

    def getLastColInPage(self, row):
        columns = self.__pages[self.__current].getColumnAddresses(row)
        return columns[-1]

    def updateCellContent(self, address, content):
        self.__pages[self.__current].updateCellContent(address, content)

    def updateCellFormat(self, address, form):
        self.__pages[self.__current].updateCellFormat(address, form)

    def getCell(self, address):
        return self.__pages[self.__current].getCell(address)

    def getCellFormat(self, address):
        return self.__pages[self.__current].getCell(address)

    def getPublicObject(self):
        c = {}
        for name in self.__pages:
            c[name] = self.__pages[name].getPublicObject()
        return c

    def loadPublicObject(self, jsonObject):
        for name in jsonObject:
            for address in jsonObject[name]:
                content = jsonObject[name][address]['content']
                form = jsonObject[name][address]['format']
                page = self.getCurrentPage()
                page.updateCellContent(address, content)
                page.updateCellFormat(address, form)
