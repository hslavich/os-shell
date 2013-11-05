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
            if len(comm) > 1:
                self.commands[comm[0]](comm[1])
            else:
                self.commands[comm[0]]()
            return True
        except (KeyError, TypeError):
            return False

    def _splitArgs(self, command):
        return command.split(" ", 1)
