import os
from sound import Sound
import screen_brightness_control as sbc
import webbrowser

# Устанавливает громкость
def setVolume(vol):
    Sound.volume_set(vol)

    #Sound.volume_up() # увеличим громкость на 2 единицы (проценты говорить неправильно)
    #Sound.volume_down() # уменьшим громкость на 2 единицы
    #cur = Sound.current_volume() # получили текущие настройки
    #Sound.mute() # убрали звук
    #Sound.volume_max() # Наоборот, прибавили на максимум
    print(f'Set volume to {vol}')

# Устанавливает яркость
def setBrightness(vol):
    sbc.set_brightness(vol)
    
    print(f'Set brightness to {vol}')

#setVolume(10)
#setBrightness(100)

# Открывает пустую вкладку браузера
def openBrowser():
    url = "https://"
    webbrowser.open(url)

    print('Browser has open')

# Открывает страницу по url
def openPage(url):
    webbrowser.open(url)

    print(f'Open link {url}')

# Перезагрузить компьютер
def rebootPC():
    print('Reboot...')

    os.system("shutdown /r /t 1")

# Перезагрузить компьютер
def logoutPC():
    print('logout...')

    os.system("shutdown /l")

logoutPC()
