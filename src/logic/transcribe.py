from src.logic.audio.mic_rec import MicRecording
from speech_recognition import Recognizer

class Transcriber(Recognizer):
    def __init__(self):
        super().__init__()

    def micLiveAudio(self):
        self.audio = MicRecording().recAudio()
    
    def fileGetAudio(self, audioFile):
        self.audio = audioFile # TODO - placeholder

    def fasterWhisper(self):
        self.transcribed = self.recognize_faster_whisper(self.audio, model="base", init_options={ "device": "cpu", "compute_type":"int8" })
