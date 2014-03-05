from sheet import Sheet
import json

class Model:
    def __init__(self, sheet, filename=None):
        self.__sheet = sheet
        self.__filename = filename
        self.__cursorx = 0
        self.__cursory = 0
        self.__lastCommand = ""

        self.loadFile(filename)

    def getCursor(self):
        return (self.__cursorx, self.__cursory)

    def echoCommand(self, c):
        self.__lastCommand = c

    def moveCursorHome(self):
        self.__cursorx = 0
        self.__cursory = 0

    def moveCursorDown(self):
        if self.__cursory < 999:
            self.__cursory += 1

    def moveCursorUp(self):
        if self.__cursory > 0:
            self.__cursory -= 1

    def moveCursorLeft(self):
        if self.__cursorx > 0:
            self.__cursorx -= 1

    def moveCursorRight(self):
        if self.__cursorx < 675:
            self.__cursorx += 1

    def setCellAtCursor(self, s):
        code = self.pairToCode((self.__cursorx, self.__cursory))
        self.__sheet.updateCellContent("Main", code, s)

    def getCell(self, x, y):
        code = self.pairToCode((x,y))
        return self.__sheet.getCell("Main", code)

    def getCellFormat(self, x, y):
        code = self.pairToCode((x,y))
        return self.__sheet.getCellFormat("Main", code)

    def getLastCommand(self):
        return self.__lastCommand

    def loadFile(self, filename):
        if filename is not None:
            try:
                f = open(filename)
                jsonContent = json.loads(f.read())
                f.close()
                self.__sheet.loadPublicObject(jsonContent)
            except IOError:
                pass

    def saveFile(self, filename=None):
        if filename is not None:
            self.__filename = filename
        else:
            filename = self.__filename

        if filename is not None:
            try:
                jsonContent = json.dumps(self.__sheet.getPublicObject())
                f = open(self.__filename, 'w')
                f.write(jsonContent)
                f.close()
            except IOError:
                print "Permission denied in writing file. Maybe write-protected."

    def codeToPair(self, code):
        # This is very hackish.
        # All column codes are either 1 or 2 characters.
        # If the element at code[1] is numeric, we have a length 1 column code.
        x = 0
        y = 0
        if code[1].isdigit():
            x = self.columnCodeToAbsolute(code[0])
            y = self.rowCodeToAbsolute(code[1:])
        else:
            x = self.columnCodeToAbsolute(code[0]+code[1])
            y = self.rowCodeToAbsolute(code[2:])
        return (x, y)

    def pairToCode(self, xypair):
        return self.columnCode(xypair[0]) + self.rowCode(xypair[1])

    def columnCodeToAbsolute(self, xx):
        assert len(xx) == 2 or len(xx) == 1

        if len(xx) == 2:
            return (ord(xx[0])-ord('A')+1)*26 + (ord(xx[1])-ord('A'))

        return (ord(xx[0])-ord('A')+1)*26 + (ord(xx[1])-ord('A'))

    def columnCode(self, x):
        first = int(x / 26)
        second = x % 26

        code = ""
        if first > 0:
            code = chr(ord('A')+first-1) + chr(ord('A')+second)
        else:
            code = chr(ord('A')+second)

        return code

    def rowCodeToAbsolute(self, yy):
        return int(yy)-1

    def rowCode(self, y):
        return str(y+1)
