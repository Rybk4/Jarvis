import screen_brightness_control as sbc

from commands.modules.log import logging

# Устанавливает яркость
def setBrightness(vol):
    sbc.set_brightness(vol)
    
    logging(f'Set brightness to {vol}')

