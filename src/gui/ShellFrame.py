import wx
import os
from model.Shell import Shell

class ShellFrame(wx.Frame):
    
    def __init__(self):
        wx.Frame.__init__(self, None, title="OS Shell", size=(450, 300))
        self.shell = Shell()
        self.SetBackgroundColour(wx.BLACK)
        self.initComponents()
        self.initEvents()
        self.Centre()
        self.Show(True)
        
    def initComponents(self):
        self.history = wx.TextCtrl(self, style=wx.TE_MULTILINE | wx.TE_READONLY)
        self.history.SetBackgroundColour(wx.BLACK)
        self.history.SetForegroundColour(wx.WHITE)
        self.history.Refresh()
        self.command = wx.TextCtrl(self, style=wx.TE_PROCESS_ENTER)
        self.command.SetBackgroundColour(wx.BLACK)
        self.command.SetForegroundColour(wx.WHITE)
        self.command.Refresh()
        self.command.SetFocus()
        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(self.history, 1, wx.EXPAND)
        sizer.Add(self.command, 0, wx.EXPAND)
        self.SetSizer(sizer)
        self.SetAutoLayout(1)
        
    def initEvents(self):
        self.Bind(wx.EVT_TEXT_ENTER, self.onEnterCommand, self.command)
        
    def onEnterCommand(self, event):
        command = event.GetString()
        self.history.AppendText("> " + command)
        self.history.AppendText(os.linesep)
        if command and not self.shell.runCommand(command):
            self.history.AppendText("No command '" + command + "' found." + os.linesep)
        self.command.Clear()
        

app = wx.App(False)
ShellFrame()
app.MainLoop()