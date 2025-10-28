import tkinter as tk
from tkinter import ttk


class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('MPTranscribe')
        self.dimensions()
        self.internal = Internal(self)

    def dimensions(self):
        self.maxsize(width=800, height=400)
        self.minsize(width=800, height=400)

class Internal(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.content = ttk.Frame(master)
        self.frame = ttk.Frame(self.content, borderwidth=5, relief="solid", width=800, height=400)
        self.content.grid(row=0, column=0)
        self.frame.grid(row=0, column=0, columnspan=3, rowspan=2)
        self.buttons = Buttons(self)

class Buttons(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.fileDialogueButton()
        self.tranScrButton()
 
    def fileDialogueButton(self):
        fDiaButton = ttk.Button(self.master.content, text="Choose File")
        fDiaButton.grid(row=0, column=1)
    
    def tranScrButton(self):
        sButton = ttk.Button(self.master.content, text='Transcribe')
        sButton.grid(row=0, column=0)


