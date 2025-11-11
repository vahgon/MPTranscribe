from speech_recognition import AudioData, Recognizer
from src.settings.mic_set import UserMicrophone

class MicRecording(Recognizer):
    def __init__(self):
        super().__init__()

    def recAudio(self) -> AudioData:
        with UserMicrophone() as source:
            return self.listen(source)

class AudioFile(AudioData):
    def __init__(self, master):
        super().__init__(master)
