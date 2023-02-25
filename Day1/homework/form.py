'''
Feladat: Töltsük ki a form-ot python kód segítségével!
Szorgalmi: Próbáljuk meg beküldeni az adatokat!

https://testpages.herokuapp.com/styled/validation/input-validation.html
'''

import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

service = Service(executable_path=r'C:/Users/Csillacsu/OneDrive/Dokumentumok/Progmasters Automata tesztelő 2023/chromedriver_win32/chromedriver.exe')
options = Options()
options.add_experimental_option("detach", True)

browser = webdriver.Chrome(service=service, options=options)
actions = ActionChains(webdriver)

URL = "https://testpages.herokuapp.com/styled/validation/input-validation.html"
browser.get(URL)

first_name = browser.find_element(By.ID, 'firstname')
first_name.send_keys('Zsuzsa')

last_name = browser.find_element(By.ID, 'surname')
last_name.send_keys('Németh')

age = browser.find_element(By.ID, 'age')
age.send_keys('25')

notes = browser.find_element(By.ID, 'notes')
notes.send_keys('semmi')

country = Select(browser.find_element(By.ID, 'country'))
country.select_by_visible_text('Saint Lucia')

submit_button = browser.find_element(By.XPATH, '//input[@type="submit"]')
submit_button.click()

browser.quit()
