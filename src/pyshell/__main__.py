from model.shell import Shell
from gui.shellframe import ShellFrame

if __name__ == '__main__':
    shell = Shell()
    ShellFrame(shell).start()
