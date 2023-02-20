import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

s = Service(executable_path='S:\oktatási anyagok\chromedriver.exe')
o = Options()
o.add_experimental_option('detach', True)
browser = webdriver.Chrome(service=s, options=o)
browser.get('https://www.selenium.dev/')

# ---- 1 ---- ablak méretezések
browser.maximize_window()
time.sleep(2)
browser.minimize_window()
time.sleep(2)
browser.fullscreen_window()
time.sleep(2)
browser.set_window_size(800, 600, 'current')
time.sleep(2)

# ---- 2 ---- böngésző címének elkérése
title = browser.title
print(title)
print(f'A böngésző címe: {title}')

if title == "Selenium":
    print('Cím megfelelő')
else:
    print('Nem megfelelő cím')


# ---- 3 ---- képernyő fotó
title = browser.title
browser.save_screenshot(f'screenshot_{title}.png')

# ---- 4 ---- url elkérés
used_url = browser.current_url
print(f'Aktuális url: {browser.current_url}')

# ---- 5 ---- navigáció
time.sleep(2)
browser.back()
time.sleep(2)
browser.forward()
time.sleep(2)
browser.refresh()
time.sleep(2)


# browser.close() # egy ablakot zár
browser.quit() # minden ablakot bezár