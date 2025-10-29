import tkinter as tk
from tkinter import PhotoImage
from src.interface.components.menu import MenuBar
from src.interface.components.labels import Logo

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        
        self.title('MPTranscribe')
        self.selectedFile = None
        self.optWinOpen = False
        # TODO - add dark theme
        self.theme = None

        self.appSize()
        self.config(menu=MenuBar(self))
        self.logo = Logo(self)

        self.mainloop()

    def appSize(self):
        screen = tk.Tk()

        size = []
        size.append(int(screen.winfo_screenwidth()/2.5))
        size.append(int(screen.winfo_screenheight()/2.5))

        screen.destroy()
    
        self.geometry(f'{size[0]}x{size[1]}')
        self.minsize(size[0], size[1])
        self.maxsize(size[0], size[1])
