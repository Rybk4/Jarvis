from commands.modules.volume import volumeMax

from speech import speech_old

s = speech_old.process_audio_input()

if(s == "раз"):
    volumeMax()

