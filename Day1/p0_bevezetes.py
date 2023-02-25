from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

s = Service(executable_path='C:/Users/Csillacsu/OneDrive/Dokumentumok/Progmasters Automata tesztelő 2023/chromedriver_win32/chromedriver.exe')
o = Options()
o.add_experimental_option('detach', True)

browser = webdriver.Chrome(service=s, options=o)

browser.get('https://www.selenium.dev/')


"""
browser.maximize_window()
time.sleep(2)
browser.minimize_window()
time.sleep(2)
browser.fullscreen_window()
time.sleep(2)
browser.set_window_size(800, 600, 'current')
time.sleep(2)

#browser.close()
browser.quit()

"""
"""
title = browser.title
print(title)
print(f'A böngésző címe {title}')
browser.quit()

if title == 'Selenium':
    print('Cím megfelelő')
else:
    print('nem megfelelő')

"""
"""
title = browser.title
browser.save_screenshot(f'screenshot_{title}.png')
"""

"""
used_url = browser.current_url
print(f'aktuális url: {browser.current_url}')
"""

"""
time.sleep(2)
browser.back()
time.sleep(2)
browser.forward()
time.sleep(2)
browser.refresh()
time.sleep(2)

browser.quit()

"""