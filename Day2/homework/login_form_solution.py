'''
A szövegben lévő adatok kimentés uátni felhasználásával jelentkezzünk be az oldalra, majd validáljuk a megjelenő üzenetet.
http://the-internet.herokuapp.com/login
'''
import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

URL = 'http://hotel-v2.progmasters.hu/'
service = Service(executable_path=r'C:/Users/Csillacsu/OneDrive/Dokumentumok/Progmasters Automata tesztelő 2023/chromedriver_win32/chromedriver.exe')
options = Options()
options.add_experimental_option("detach", True)
browser = webdriver.Chrome(service=service, options=options)

URL = "http://the-internet.herokuapp.com/login"
browser.get(URL)

username_input = browser.find_element(By.ID, 'username')
password_input = browser.find_element(By.ID, 'password')
username = browser.find_elements(By.XPATH, '//h4/em')[0]
password = browser.find_elements(By.XPATH, '//h4/em')[1]
submit_btn = browser.find_element(By.XPATH, '//button[@type="submit"]')

username_input.send_keys(username.text)
password_input.send_keys(password.text)
submit_btn.click()
# time.sleep(1)
# alert_message = browser.find_element(By.ID, 'flash')


# webdriver waitnek meg kell andi a böngészőt ez most a browser és az várakozási időt ami itt 5
# until (vagy intil not is lehet)azt jelenti hogy mi az a feltétel amire várunk
# EC itt az importnál meghatározott expected conditions
# prescence of element located vagyis itt most az hogy alert message megjelenik
alert_message = WebDriverWait(browser, 5).until(EC.presence_of_element_located((By.ID, 'flash')))

if alert_message.get_attribute('class') == "flash success":
    print("OK")
else:
    print("Login failed")

browser.quit()
