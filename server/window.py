import webview

from modules.log import logging

def createWindow():
    webview.create_window('Jarvice', url='https://www.youtube.com/?gl=RU&hl=ru&themeRefresh=1', width=1280, height=720,resizable=False, fullscreen=False)
    webview.start()

    logging('createWindow webview start')
    