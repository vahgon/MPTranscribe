import tkinter as tk
from tkinter import ttk
from tkinter import filedialog as fd
from tkinter.messagebox import showinfo

size = []

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('MPTranscribe')
        self.dimensions()
        self.fileFrame = FileDialogueFrame(self)
        self.transFrame = TranscriberFrame(self)
        self.selectedFile = None

        self.mainloop()

    def dimensions(self):
        screen = tk.Tk()
        size.append(int(screen.winfo_screenwidth()/2.5))
        size.append(int(screen.winfo_screenheight()/2.5))
        screen.destroy()

        self.geometry(f'{size[0]}x{size[1]}')
        self.minsize(size[0], size[1])
        self.maxsize(size[0], size[1])


class FileDialogueFrame(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.place(relx=0.1, rely=0.1, relwidth=0.3, relheight=1)
        self.createWidget()

    def createWidget(self):
        self.dialogueButton = ttk.Button(self, text='Open File', command=self.getFileName)
        self.setLayout()

    def setLayout(self):
        self.columnconfigure((0,1,2,3,4,5,6), weight=1, uniform='a')
        self.rowconfigure((0,1,2,3,4,5,6,7,8), weight=1, uniform='a')

        self.dialogueButton.grid(row=7, column=0, padx=10, pady=10, columnspan=2, rowspan=1, sticky='nswe')
    
    def getFileName(self):
        fileTypes = [
            ('All files', '*.*')
        ]
        self.selectedFile = fd.askopenfilename(title='Choose an audio file', initialdir='/', filetypes=fileTypes)
        self.master.selectedFile = self.selectedFile

class TranscriberFrame(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.place(relx=0.7, rely=0.1, relwidth=0.3, relheight=1)
        self.createWidget()

    def createWidget(self):
        self.transcribeButton = ttk.Button(self, text='Transcribe', command=self.printFile)
        self.setLayout()

    def setLayout(self):
        self.columnconfigure((0,1,2,3,4,5,6), weight=1, uniform='a')
        self.rowconfigure((0,1,2,3,4,5,6,7,8), weight=1, uniform='a')

        self.transcribeButton.grid(row=7, column=0, padx=10, pady=10, columnspan=2, rowspan=1, sticky='nswe')
    