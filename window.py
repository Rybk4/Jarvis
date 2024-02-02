import webview

from commands.modules.log import logging

def createWindow():
    webview.create_window('Jarvice', url='http://127.0.0.1:5000/', width=1280, height=720,resizable=False, fullscreen=False)
    webview.start()

    logging('createWindow webview start')
    
createWindow()