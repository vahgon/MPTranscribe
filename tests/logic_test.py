from src.logic.audio.live_rec import MicRecording
from speech_recognition import AudioData

def test_mic_class():
    assert type(MicRecording().RecAudio()) == AudioData, "Function did not return object of type AudioData" 
