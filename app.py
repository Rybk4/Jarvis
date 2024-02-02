from commands.modules.speech import process_audio_input
from commands.modules.volume import volumeMax, volumeMute, volumeDown
from commands.modules.brightness import setBrightness
import keyboard

def on_q_pressed():
    keyboard.unhook_all()  
    print("Quitting the program.")
    exit()

 
keyboard.add_hotkey('q', on_q_pressed)

print("Press 'Q' to quit.")
while True:
    result = process_audio_input()

    if result:
        print("Processed result:", result)

        if result == "раз":
            volumeMax()
        elif result == "5":
            volumeMute()
        elif result == "2":
            volumeDown()
        elif "яркость" in result:
            brightness_value = ''.join(filter(str.isdigit, result))
            if brightness_value:
                setBrightness(int(brightness_value))
        else: print("Please say again")
