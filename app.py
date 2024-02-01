from speech_old import process_audio_input
from commands.modules.volume import volumeMax , volumeMute , volumeDown
import keyboard


print("Press any key to start audio processing or press 'Q' to quit.")
while True:
    
    if keyboard.is_pressed('q'):
        break
    result = process_audio_input()
    if (result != ""):
        if(result == "раз"):
             
            volumeMax()

        if(result == "5"):
            
            volumeMute()

        if(result == "2"):
           
            volumeDown()
    else:
        result = process_audio_input()