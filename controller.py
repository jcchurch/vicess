import curses
from keymap import KeyMap

class Controller:
    def __init__(self, configFile=None):
        self.__stdscr = None
        self.__km = KeyMap()

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

    def main(self, view, model):
        weShouldKeepGoing = True
        while weShouldKeepGoing:
            view.update(self.__stdscr)

            tightLoop = True
            while tightLoop: 
                c = self.__stdscr.getch() 
                model.echoCommand(str(c))
                tightLoop = False

                self.__km.addCommand(chr(c))
                action = self.__km.translate()

                if action == "reset_command_state":
                    self.__km.reset()

                if action == "cursor_left":
                    model.moveCursorLeft()
                    tightLoop = False

                if action == "cursor_down": 
                    model.moveCursorDown()
                    tightLoop = False

                if action == "cursor_up": 
                    model.moveCursorUp()
                    tightLoop = False

                if action == "cursor_right": 
                    model.moveCursorRight()
                    tightLoop = False

                if action == "quit": 
                    tightLoop = False
                    weShouldKeepGoing = False

                if action == "save_and_quit": 
                    model.saveFile()
                    tightLoop = False
                    weShouldKeepGoing = False

                if action == "insert":
                    (x, y) = view.getInputLine(self.__stdscr)
                    curses.echo()
                    s = self.__stdscr.getstr(y,x,100)
                    curses.noecho()
                    model.setCellAtCursor(s)
                    tightLoop = False

                if c == ord(':'):
                    pass
