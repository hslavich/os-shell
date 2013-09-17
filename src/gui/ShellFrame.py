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
        self.txtHistory = wx.TextCtrl(self, style=wx.TE_MULTILINE | wx.TE_READONLY)
        self.txtHistory.SetBackgroundColour(wx.BLACK)
        self.txtHistory.SetForegroundColour(wx.WHITE)
        self.txtHistory.Refresh()
        self.txtCommand = wx.TextCtrl(self, style=wx.TE_PROCESS_ENTER)
        self.txtCommand.SetBackgroundColour(wx.BLACK)
        self.txtCommand.SetForegroundColour(wx.WHITE)
        self.txtCommand.Refresh()
        self.txtCommand.SetFocus()
        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(self.txtHistory, 1, wx.EXPAND)
        sizer.Add(self.txtCommand, 0, wx.EXPAND)
        self.SetSizer(sizer)
        self.SetAutoLayout(1)
        
    def initEvents(self):
        self.Bind(wx.EVT_TEXT_ENTER, self.onEnterCommand, self.txtCommand)
        
    def onEnterCommand(self, event):
        command = event.GetString()
        self.txtHistory.AppendText("> " + command)
        self.txtHistory.AppendText(os.linesep)
        if command and not self.shell.runCommand(command):
            self.txtHistory.AppendText("No txtCommand '" + command + "' found." + os.linesep)
        self.txtCommand.Clear()
        

app = wx.App(False)
ShellFrame()
app.MainLoop()