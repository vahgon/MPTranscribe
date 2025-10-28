import tkinter as tk
from tkinter import filedialog as fd
from src.interface.components.windows import SettingsWindow

class MenuBar(tk.Menu):
    def __init__(self, master):
        super().__init__(master)
        self.fileMenu()
        self.optionsMenu()

    def fileMenu(self):
        file = tk.Menu(self, tearoff=0)
        self.add_cascade(label='File', menu=file)

        file.add_command(label='Open File', command=lambda : self.designateFile())
        file.add_command(label='Save As')
        file.add_separator()
        file.add_command(label='Exit', command=lambda : self.master.quit())
    
    def designateFile(self):
        fileTypes = [
            ('All files', '*.*')
        ]
        self.selectedFile = fd.askopenfilename(title='Choose an audio file', initialdir='/', filetypes=fileTypes)
        self.master.selectedFile = self.selectedFile
    
    def optionsMenu(self):
        optMenu = tk.Menu(self, tearoff=0)
        self.add_cascade(label='Options', menu=optMenu)
        optMenu.add_command(label='Settings', command=self.checkOptionsWindow)
        optMenu.add_command(label='Help')

    def checkOptionsWindow(self):
        if self.master.optWinOpen is False:
            self.master.optWindow = SettingsWindow(self.master)
            self.master.optWinOpen = True
