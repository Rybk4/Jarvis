from speech_old import process_audio_input
from commands.modules.volume import volumeMax , volumeMute , volumeDown

while True:
    result = process_audio_input()
    if (result != ""):
        if(result == "раз"):
            print("test c")
            volumeMax()

        if(result == "5"):
            print("test c")
            volumeMute()
            
        if(result == "2"):
            print("test c")
            volumeDown()
    else:
        result = process_audio_input()