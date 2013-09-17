from Command import *

class Shell:
    
    def __init__(self):
        self.history = []
    
    def runCommand(self, command):
        self.history.append(command)
        if hasattr(Command, command):
            function = getattr(Command, command)
            if callable(function):
                function()
                return True
        return False
