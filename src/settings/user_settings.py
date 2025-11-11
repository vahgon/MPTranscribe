from dotenv import set_key, find_dotenv, load_dotenv
from pathlib import Path
from os import environ

class UserSettings:
    def __init__(self):
        self.path = Path('.config')
        if not find_dotenv(filename='.config'):
            self.path.touch(mode=0o600, exist_ok=True)
            self.initConfigOptions()
        else:
            self.setConfig()

    def changeConfigOption(self, opt, val):
        environ[opt] = val
        set_key(self.path, opt, environ[opt])
        self.setConfig()

    def initConfigOptions(self):
        set_key(self.path, "MICROPHONE", "")
        set_key(self.path, "API_PLACEHOLD", "")
        self.setConfig()

    def setConfig(self):
        self.dotenv = load_dotenv(self.path)
