'''
https://www.tutorialspoint.com/selenium/selenium_automation_practice.htm
'''

import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

service = Service(executable_path=r'C:/Users/Csillacsu/OneDrive/Dokumentumok/Progmasters Automata tesztelő 2023/chromedriver_win32/chromedriver.exe')
options = Options()
options.add_experimental_option("detach", True)

browser = webdriver.Chrome(service=service, options=options)

URL = "https://www.tutorialspoint.com/selenium/selenium_automation_practice.htm"
browser.get(URL)
browser.maximize_window()

consent_button = browser.find_element(By.XPATH, '//p[@class="fc-button-label"]')
consent_button.click()

first_name_input = browser.find_element(By.XPATH, '//input[@name="firstname"]')
first_name_input.send_keys('Csilla')

last_name_input = browser.find_element(By.XPATH, '//input[@name="lastname"]')
last_name_input.send_keys('Lengyel')

sex_input = browser.find_element(By.XPATH, '//input[@value="Female"]')
sex_input.click()
time.sleep(3)

"""
experience_input = browser.find_elements(By.CSS_SELECTOR, 'input[@type="radio"]')[5]
experience_input.click()
"""

date_input = browser.find_elements(By.CSS_SELECTOR, 'input[style="width:95%;padding:4px 0px 4px 5px;margin:4px 0px"]')[2]
date_input.send_keys('1990.09.09.')


profession_input = browser.find_element(By.XPATH, '//input[@value="Automation Tester"]')
profession_input.click()


"""
flavours_input = browser.find_element(By.XPATH, '//input[@value="Selenium Webdriver"]')
flavours_input.click()

"""

continent_select = Select(browser.find_element(By.XPATH, '//select[@name="continents"]'))
continent_select.select_by_visible_text('Europe')

command_select = Select(browser.find_element(By.XPATH, '//select[@name="selenium_commands"]'))
command_select.select_by_visible_text('WebElement Commands')
command_select.select_by_visible_text('Wait Commands')

button_submit = browser.find_element(By.XPATH, '//button[@name="submit"]')
button_submit.click()

