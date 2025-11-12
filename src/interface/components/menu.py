from tkinter import filedialog, Menu
from src.interface.components.windows import SettingsWindow, ConfigurationWindow

class MenuBar(Menu):
    def __init__(self, master):
        super().__init__(master)
        self.fileMenu()
        self.optionsMenu()
        self.githubMenu()

    def fileMenu(self):
        file = Menu(self, tearoff=0)
        self.add_cascade(label='File', menu=file)

        file.add_command(label='Open File', command=lambda : self.designateFile())
        file.add_command(label='Save As')
        file.add_separator()
        file.add_command(label='Exit', command=lambda : self.master.quit())

    def designateFile(self):
        fileTypes = [
            ('All files', '*.*')
        ]
        self.selectedFile = filedialog.askopenfilename(title='Choose an audio file', initialdir='/', filetypes=fileTypes)
        self.master.selectedFile = self.selectedFile
    
    def optionsMenu(self):
        opt = Menu(self, tearoff=0)
        self.add_cascade(label='Options', menu=opt)
        opt.add_command(label='Settings', command=self.checkOptionsWindow)
        opt.add_command(label='Configure', command=self.checkConfigWindow)
        opt.add_separator()
        opt.add_command(label='Help')

    def checkOptionsWindow(self):
        if self.master.optWinOpen is False:
            self.master.optWindow = SettingsWindow(self.master)
            self.master.optWinOpen = True

    def checkConfigWindow(self):
        if self.master.configWinOpen is False:
            self.master.configWindow = ConfigurationWindow(self.master)
            self.master.configWinOpen = True
    
    def githubMenu(self):
        self.add_command(label='Github', command=self.openGithub)

    def openGithub(self):
        from webbrowser import open_new
        open_new('https://github.com/vahgon/MPTranscribe')
