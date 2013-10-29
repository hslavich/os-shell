from model.shell import Shell
from gui.shellframe import ShellFrame

if __name__ == '__main__':
    shell = Shell()
    def func(): print("Another test command")
    shell.addCommand("demo", func)
    ShellFrame(shell).start()
