class Shell:

    def __init__(self):
        self.history = []
        self.commands = {}
        self._addExamples()

    def _addExamples(self):
        def _test(): print("Test command")
        self.addCommand("test", _test)

    def addCommand(self, name, command):
        self.commands[name] = command

    def runCommand(self, command):
        self.history.append(command)
        try:
            self.commands[command]()
            return True
        except (KeyError, TypeError):
            return False
