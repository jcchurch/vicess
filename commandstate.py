class CommandState:
    def __init__(self):
        self.__commandlog = []

    def evaluateCommand(self, c):
        self.__commandlog.append(c)

        # There are three types of states:
        # Action States:
        # --- These states require action.
        # Error States:
        # --- These states sound an error bell and reset the command log.
        # Incomplete States:
        # --- These states await more information.

        # Action States

        # Any state ending with an escape key resets the command log.
        if self.__commandlog[-1] == 27:
            self.__commandlog = []
            return None

        if self.__commandlog[0] == 260 or self.__commandlog[1] == chr('h'):
            return 
