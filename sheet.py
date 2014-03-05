from page import Page

class Sheet:
    def __init__(self): 
        self.__pages = {}
        self.__pages["Main"] = Page()

    def updateCellContent(self, pagename, address, content):
        self.__pages[pagename].updateCellContent(address, content)

    def updateCellFormat(self, pagename, address, form):
        self.__pages[pagename].updateCellFormat(address, form)

    def getCell(self, pagename, address):
        return self.__pages[pagename].getCell(address)

    def getCellFormat(self, pagename, address):
        return self.__pages[pagename].getCell(address)

    def getPublicObject(self):
        return {name:self.__pages[name].getPublicObject() for name in self.__pages}

    def loadPublicObject(self, jsonObject):
        for name in jsonObject:
            for address in jsonObject[name]:
                content = jsonObject[name][address]['content']
                form = jsonObject[name][address]['format']
                self.updateCellContent(name, address, content)
                self.updateCellFormat(name, address, form)
