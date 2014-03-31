import optparse 
from model import Model 
from view import View
from controller import Controller

if __name__ == '__main__':
    desc = """Vicess: Vi-like Terminal Spreadsheet"""

    p = optparse.OptionParser(usage="%prog [options] [file]", version="%prog 0.1", description=desc)
    options, arguments = p.parse_args()

    filename = None
    if len(arguments) > 0:
        filename = arguments[0]

    M = Model(filename)
    V = View(M)
    C = Controller()

    C.start()
    C.main(V, M)
    C.end()
