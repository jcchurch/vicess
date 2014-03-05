class Cell:
    def __init__(self):
        self.__form = ""
        self.__content = ""
        self.__type = "Text"

    def __init__(self, content="", form=""):
        self.update(content, form)

    def discernType(self):
        self.__type = "Text"
        if len(self.__content) > 0:
            if self.__content[0] == "=":
                self.__type = "Formula"
            else:
                try:
                    float(self.__content)
                    self.__type = "Numeric"
                except:
                    pass

    def update(self, content, form=None):
        self.__content = content
        if form is not None:
            self.__form = form
        self.discernType()

    def updateFormat(self, form):
        self.__form = form 

    def getRawContent(self):
        return self.__content

    def getFormat(self):
        return self.__form

    def getType(self):
        return self.__type

    def getPublicObject(self):
        return {"format":self.__form,"content":self.__content}
