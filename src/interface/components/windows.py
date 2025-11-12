from src.settings.user_settings import UserSettings
from tkinter import Toplevel

class SettingsWindow(Toplevel):
    def __init__(self, master):
        super().__init__(master)
        UserSettings()
        self.transient(self.master)
        self.title('Settings')
        self.protocol("WM_DELETE_WINDOW", self.closeWindow)
        
        from src.interface.components.labels import MicLabel
        MicLabel(self)
        self.winSize()

    def winSize(self):
        self.master.update()
        offsetX, offsetY = self.master.winfo_x(), self.master.winfo_y()
        self.geometry(f"+{offsetX}+{offsetY}")        

    def closeWindow(self):
        self.destroy()
        self.master.optWinOpen = False

class ConfigurationWindow(Toplevel):
    def __init__(self, master):
        super().__init__(master)

        self.transient(self.master)
        self.title('Configure')
        self.winSize()
        self.protocol("WM_DELETE_WINDOW", self.closeWindow)

    def winSize(self):
        self.master.update()
        offsetX, offsetY = self.master.winfo_x(), self.master.winfo_y()
        self.geometry(f"+{offsetX}+{offsetY}")

    def closeWindow(self):
        self.destroy()
        self.master.configWinOpen = False
