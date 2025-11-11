from speech_recognition import Microphone
from src.settings.user_settings import UserSettings
from os import environ
UserSettings()

class UserMicrophone(Microphone):
    def __init__(self):
        super().__init__(int(environ['MICROPHONE']))

