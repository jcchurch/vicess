from page import Page

class Sheet:
    def __init__(self): 
        self.__pages = {}
        self.__current = "Main"
        self.__pages[self.__current] = Page()

    def getPage(self):
        return self.__pages[self.__current]

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
                page = self.getPage()
                page.updateCellContent(address, content)
                page.updateCellFormat(address, form)
