import curses
import re

class Controller:
    def __init__(self, configFile=None):
        self.__stdscr = None
        self.__commandstate = []
        self.__establishedCommands = {}

        if configFile is None:
            configFile = ".vicess.config"

        self.loadConfiguration(configFile)

    def start(self):
        try:
            self.__stdscr = curses.initscr()
            curses.noecho()
            curses.cbreak()
            self.__stdscr.keypad(1)
        except:
            self.end()

    def end(self):
        self.__stdscr.keypad(0)
        curses.nocbreak()
        curses.echo()
        curses.endwin()

    def loadConfiguration(self, configFile):
        for line in file(configFile):
            line = re.sub("\".+$", "", line)
            parts = re.split(" +", line);
            action = parts[0]
            sequence = " ".join(parts[1:])
            self.__establishedCommands[sequence] = action

    def translateCommand(self, keypress):
        self.__commandstate.append(chr(keypress))
        command = None

        for level in [1, 2, 3]:
            sequence = " ".join(self.__commandstate[-level:])
            if sequence in self.__establishedCommands:
                command = self.__establishedCommands[sequence]
                self.__commandstate = []

        return command

    def main(self, view, model):
        weShouldKeepGoing = True
        while weShouldKeepGoing:
            view.update(self.__stdscr)

            tightLoop = True
            while tightLoop: 
                c = self.__stdscr.getch() 
                model.echoCommand(str(c))
                tightLoop = False
                command = self.translateCommand(c)

                if command == "clear_commands":
                    self.__commandstate = []

                if command == "cursor_left":
                    model.moveCursorLeft()
                    tightLoop = False

                if command == "cursor_down": 
                    model.moveCursorDown()
                    tightLoop = False

                if command == "cursor_up": 
                    model.moveCursorUp()
                    tightLoop = False

                if command == "cursor_right": 
                    model.moveCursorRight()
                    tightLoop = False

                if command == "save_and_exit": 
                    model.saveFile()
                    tightLoop = False
                    weShouldKeepGoing = False

                if command == "insert":
                    (x, y) = view.getInputLine(self.__stdscr)
                    curses.echo()
                    s = self.__stdscr.getstr(y,x,100)
                    curses.noecho()
                    model.setCellAtCursor(s)
                    tightLoop = False

                if c == ord(':'):
                    pass

                if c == 262: # Home Key
                    model.moveCursorHome()
                    tightLoop = False

