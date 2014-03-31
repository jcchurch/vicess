import curses
import simplestring

class View:
    def __init__(self, model):
        self.__model = model 
        self.__cursor = model.getCursor()
        self.__firstColumn = 0
        self.__firstRow = 0

    def update(self, stdscr):
        (maxy, maxx) = stdscr.getmaxyx()

        cell_width = 10
        label_column_width = 5

        ncolumns = int((maxx-label_column_width)/cell_width)
        nrows = maxy-2

        (cursorx, cursory) = self.__cursor.getCursor()

        # Special Case: Cursor Moves Home
        if cursorx == 0:
            self.__firstColumn = 0

        if cursory == 0:
            self.__firstRow = 0

        if cursorx < self.__firstColumn:
            self.__firstColumn -= 1

        if cursory < self.__firstRow:
            self.__firstRow -= 1

        if cursorx >= (self.__firstColumn + ncolumns):
            self.__firstColumn += 1

        if cursory >= (self.__firstRow + nrows):
            self.__firstRow += 1

        # Row 0
        stdscr.addstr(0, 0, " "*label_column_width, curses.A_REVERSE) 
        for col in range(ncolumns):
            realCol = col+self.__firstColumn
            displayColumn = self.__cursor.columnCode(realCol)
            formatContent = simplestring.justify(displayColumn, cell_width, 'center')

            if cursorx == realCol:
                stdscr.addstr(0, label_column_width+col*cell_width, formatContent) 
            else:
                stdscr.addstr(0, label_column_width+col*cell_width, formatContent, curses.A_REVERSE) 

        # Remaining Rows
        for row in range(nrows):
            realRow = row+self.__firstRow
            displayRow = self.__cursor.rowCode(realRow)
            formatContent = simplestring.justify(displayRow, label_column_width, 'right')

            if cursory == realRow:
                stdscr.addstr(row+1, 0, formatContent) 
            else:
                stdscr.addstr(row+1, 0, formatContent, curses.A_REVERSE) 

            for col in range(ncolumns):
                realCol = col+self.__firstColumn
                address = self.__cursor.pairToCode((realCol, realRow))
                cell = self.__model.getSheet().getPage().getCell(address)
                form = self.__model.getSheet().getPage().getCellFormat(address)

                formatContent = simplestring.justify(self.__model.getSheet().getPage().getCell(address), cell_width, 'center')

                if cursorx == realCol and cursory == realRow:
                    stdscr.addstr(row+1, label_column_width+col*cell_width, formatContent, curses.A_REVERSE) 
                else:
                    stdscr.addstr(row+1, label_column_width+col*cell_width, formatContent) 

        c = self.__model.getLastCommand()
        if c != "":
            code = self.__cursor.pairToCode((cursorx, cursory))
            formatContent = simplestring.justify('|'+c+"| "+code+": ", 15, 'right')
            stdscr.addstr(maxy-1, 0, formatContent)
