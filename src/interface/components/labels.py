import tkinter as tk
from tkinter import ttk, PhotoImage

class Logo(tk.Label):
    def __init__(self, master):
        super().__init__(master)
        self.setImage()
        self.styleImage()
    
    def setImage(self):
        self.image = PhotoImage(file="src/assets/logo_placeholder.png")
        self.config(image=self.image)
        
    def styleImage(self):
        self.pack(side='left')
