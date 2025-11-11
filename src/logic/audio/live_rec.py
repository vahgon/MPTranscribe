from speech_recognition import Recognizer, AudioData
from src.logic.audio.microphone import UserMicrophone
from src.settings.user_settings import UserSettings

UserSettings()

class MicRecording(Recognizer):
    def __init__(self):
        super().__init__()

    def RecAudio(self) -> AudioData:
        with UserMicrophone() as source:
            return self.listen(source)

class AudioFile(AudioData):
    def __init__(self, master):
        super().__init__(master)
