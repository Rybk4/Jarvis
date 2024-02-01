from libs.sound.sound import Sound

from modules.log import logging

# Устанавливает громкость
def volumeSet(vol):
    Sound.volume_set(vol)

    logging(f'volumeSet {vol}')

# Повышает громкость на 2
def volumeUp():
    Sound.volume_up()

    logging(f'volumeUp {Sound.current_volume}')

# Понижает громкость на 2
def volumeDown():
    Sound.volume_down()

    logging(f'volumeDown {Sound.current_volume}')

# Убирает громкость, сохраняет предыдущее
def volumeMute():
    cur = Sound.current_volume()
    Sound.mute()

    logging(f'volumeMute {cur}')

    return cur

# Ставит громкость на всю, сохраняет предыдущее
def volumeMax():
    cur = Sound.current_volume()
    Sound.volume_max()
    
    logging(f'volumeMax {cur}')

    return cur