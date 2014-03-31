import curses

class ActionContext:
    def __init__(self, km, model, stdscr):
        self.__actions = [
                   ResetCommandState(km, model, stdscr),
                   CursorLeft(km, model, stdscr),
                   CursorRight(km, model, stdscr),
                   CursorUp(km, model, stdscr),
                   CursorDown(km, model, stdscr),
                   Save(km, model, stdscr),
                   Quit(km, model, stdscr),
                   Insert(km, model, stdscr)
                  ]

    def do(self, demands):
        if demands is not None:
            for demand in demands.split(","):
                for action in self.__actions:
                    if action.identifier(demand):
                        action.execute()

class Action:
    def __init__(self, km, model, stdscr):
        self.km = km
        self.model = model
        self.cursor = model.getCursor()
        self.stdscr = stdscr

    def identifier(self, demand):
        pass

    def execute(self):
        pass

class ResetCommandState(Action):
    def identifier(self, demand):
        return "reset_command_state" == demand

    def execute(self):
        self.km.reset()

class CursorLeft(Action):
    def identifier(self, demand):
        return "cursor_left" == demand

    def execute(self):
        self.cursor.moveCursorLeft()

class CursorRight(Action):
    def identifier(self, demand):
        return "cursor_right" == demand

    def execute(self):
        self.cursor.moveCursorRight()

class CursorUp(Action):
    def identifier(self, demand):
        return "cursor_up" == demand

    def execute(self):
        self.cursor.moveCursorUp()

class CursorDown(Action):
    def identifier(self, demand):
        return "cursor_down" == demand

    def execute(self):
        self.cursor.moveCursorDown()

class Save(Action):
    def identifier(self, demand):
        return "save" == demand

    def execute(self):
        self.model.save()

class Quit(Action):
    def identifier(self, demand):
        return "quit" == demand

    def execute(self):
        self.model.quit()

class Insert(Action):
    def identifier(self, demand):
        return "insert" == demand

    def execute(self):
        sheet = self.model.getSheet()
        (maxy, maxx) = self.stdscr.getmaxyx()
        (x, y) = (15, maxy-1)
        curses.echo()
        s = self.stdscr.getstr(y,x,100)
        curses.noecho()
        self.cursor.setCellAtCursor(sheet, s)
