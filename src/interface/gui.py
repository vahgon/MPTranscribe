import tkinter as tk
from tkinter import ttk


class App(tk.Tk):
    def __init__(self, size):
        super().__init__()
        self.title('MPTranscribe')
        self.dimensions(size)
        self.fileDialogue = Menu(self)    

        self.mainloop()

    def dimensions(self, size):
        self.geometry(f'{size[0]}x{size[1]}')
        self.minsize(size[0], size[1])
        self.maxsize(size[0], size[1])

class Menu(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.place(x=0,y=0,relwidth=0.3,relheight=1)

        self.createWidgets()

    def createWidgets(self):
        self.dialogueButton = ttk.Button(self, text='Open File')
        self.transcribeButton = ttk.Button(self, text='Start')

        self.setLayout()

    def setLayout(self):
        self.columnconfigure((0,1,2,3,4), weight=1, uniform='a')
        self.rowconfigure((0,1,2,3,4,5,6,7,8), weight=1, uniform='a')

        self.dialogueButton.grid(row=9, column=4, padx=10, pady=10, columnspan=3, rowspan=1, sticky='nswe')
        self.transcribeButton.grid(row=9, column=0, padx=10,pady=10, columnspan=3, rowspan=1, sticky='nswe')
