import speech_recognition as sr
from user_settings import UserSettings
# Testing .config, init for it will be moved later

settings = UserSettings()

settings.changeConfigOption(opt='MICROPHONE', val='2')
