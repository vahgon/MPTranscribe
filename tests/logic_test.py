from src.logic.transcribe import Transcriber
from speech_recognition import AudioData

def test_mic_return_audio():
    micAudio = Transcriber()
    micAudio.micLiveAudio()
    assert type((micAudio.audio)) == AudioData, "Function did not return object of type AudioData" 

def test_fasterwhisper():
    fwhsper = Transcriber()
    fwhsper.micLiveAudio()
    result = fwhsper.fasterWhisper()

    assert type((result)) == str, "Faster Whisper did not return string"
