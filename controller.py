import curses
from keymap import KeyMap
from action import ActionContext 

class Controller:
    def __init__(self, configFile=None):
        self.__stdscr = None

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
        km = KeyMap()
        ac = ActionContext(km, model, self.__stdscr)

        while model.checkProgramExecution():
            view.update(self.__stdscr)
            c = self.__stdscr.getch() 
            model.echoCommand(str(c))
            km.addCommand(ch(c))
            demands = km.translate()
            ac.do(demands)
