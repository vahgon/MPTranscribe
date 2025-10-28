import tkinter as tk
from tkinter import ttk

class SettingsWindow(tk.Toplevel):
    def __init__(self, master):
        super().__init__()

        self.transient(self.master)
        self.title('Options')
        self.winSize()

        self.protocol("WM_DELETE_WINDOW", self.closeWindow)

    def winSize(self):
        self.master.update()
        offsetX, offsetY = self.master.winfo_x(), self.master.winfo_y()
        self.geometry(f"+{offsetX}+{offsetY}")

    def closeWindow(self):
        self.destroy()
        self.master.optWinOpen = False
