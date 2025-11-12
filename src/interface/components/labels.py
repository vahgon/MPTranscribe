from tkinter import PhotoImage, StringVar, Label
from os import environ

class Logo(Label):
    def __init__(self, master):
        super().__init__(master)
        self.setImage()
        self.styleImage()
    
    def setImage(self):
        self.image = PhotoImage(file="src/assets/logo_placeholder.png")
        self.config(image=self.image)
        
    def styleImage(self):
        self.pack(side='left')

class MicLabel(Label):
    def __init__(self, master):
        super().__init__(master)
        txtVar = StringVar()
        txtVar.set('Microphone')

        self.config(textvariable=txtVar)
        self.styleMicLabel()
    
    def setMic(self):
        environ['MICROPHONE']

    def showAvailableMics(self):
        from speech_recognition import Microphone
        self.microphones = Microphone.list_working_microphones()
    
    def styleMicLabel(self):
        self.pack(side='left')
