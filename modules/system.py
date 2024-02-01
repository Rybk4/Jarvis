import os

from modules.log import logging

# Перезагрузить компьютер
def rebootPC():
    logging('reboot...')

    os.system("shutdown /r /t 1")

# Выйти из системы
def logoutPC():
    logging('logout...')

    os.system("shutdown /l")