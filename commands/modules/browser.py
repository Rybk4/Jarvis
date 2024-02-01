import webbrowser

# Открывает пустую вкладку браузера
def openBrowser():
    url = "https://"
    webbrowser.open(url)

    print('Browser has open')

# Открывает страницу по url
def openPage(url):
    webbrowser.open(url)

    print(f'Open link {url}')