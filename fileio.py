import json

class FileIO:

    def __init__(self, filename=None):
        self.__filename = None
        self.updateFilename(filename)

    def updateFilename(self, filename=None):
        if filename is not None:
            self.__filename = filename

    def loadFile(self, filename=None):
        self.updateFilename(filename)
        content = ""

        if self.__filename is not None:
            try:
                f = open(self.__filename)
                content = json.loads(f.read())
                f.close()
            except IOError:
                pass

        return content

    def saveFile(self, content, filename=None):
        self.updateFilename(filename)

        if self.__filename is not None:
            try:
                jsonContent = json.dumps(content)
                f = open(self.__filename, 'w')
                f.write(jsonContent)
                f.close()
            except IOError:
                print "Permission denied in writing file. Maybe write-protected."
