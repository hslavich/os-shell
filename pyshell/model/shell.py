class Shell:

    def __init__(self):
        self.history = []
        self.commands = {}
        self._addExamples()

    def _addExamples(self):
        def _test(): print("Test command")
        def _echo(args): print(args)
        self.addCommand("test", _test)
        self.addCommand("echo", _echo)

    def addCommand(self, name, command):
        self.commands[name] = command

    def runCommand(self, command):
        self.history.append(command)
        try:
            comm = self._splitArgs(command)
            self.commands[comm[0]](comm[1])
            return True
        except (KeyError, TypeError):
            return False

    def _splitArgs(self, command):
        list = command.split()
        return (list.pop(0), list)
