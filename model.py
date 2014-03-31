from sheet import Sheet
from fileio import FileIO
from cursor import Cursor

class Model:
    def __init__(self, filename):
        self.__sheet = Sheet()
        self.__cursor = Cursor()
        self.__io = FileIO(filename)
        self.__programIsRunning = True
        self.__lastCommand = ""

        self.load()

    def getCursor(self):
        return self.__cursor

    def getSheet(self):
        return self.__sheet

    def load(self):
        self.__sheet.loadPublicObject(self.__io.loadFile())

    def save(self):
        self.__io.saveFile(self.__sheet.getPublicObject())

    def quit(self):
        self.__programIsRunning = False

    def checkProgramExecution(self):
        return self.__programIsRunning

    def echoCommand(self, c):
        self.__lastCommand = c

    def getLastCommand(self):
        return self.__lastCommand
