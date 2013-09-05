from Command import *

class Shell:
    
    def runCommand(self, command):
        if hasattr(Command, command):
            function = getattr(Command, command)
            if callable(function):
                function()
                return True
        return False
