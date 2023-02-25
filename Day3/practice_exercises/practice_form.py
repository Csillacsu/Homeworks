'''
https://www.tutorialspoint.com/selenium/selenium_automation_practice.htm
'''

import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains


service = Service(executable_path=r'C:/Users/Csillacsu/OneDrive/Dokumentumok/Progmasters Automata tesztelő 2023/chromedriver_win32/chromedriver.exe')
options = Options()
options.add_experimental_option("detach", True)

browser = webdriver.Chrome(service=service, options=options)
actions = ActionChains(webdriver)

URL = "https://www.tutorialspoint.com/selenium/selenium_automation_practice.htm"
browser.get(URL)
browser.maximize_window()
time.sleep(2)

consent_button = browser.find_element(By.XPATH, '//p[@class="fc-button-label"]')
consent_button.click()

agree_button = browser.find_element(By.ID, 'banner-accept')
agree_button.click()

first_name_input = browser.find_element(By.XPATH, '//input[@name="firstname"]')
first_name_input.send_keys('Csilla')

last_name_input = browser.find_element(By.XPATH, '//input[@name="lastname"]')
last_name_input.send_keys('Lengyel')

sex_input = browser.find_element(By.XPATH, '//input[@value="Female"]')
sex_input.click()
time.sleep(1)


experience_input = browser.find_elements(By.CSS_SELECTOR, 'input[type="radio"]')[5]
experience_input.click()
time.sleep(1)

experience_input.send_keys(Keys.PAGE_DOWN)
time.sleep(2)


date_input = browser.find_elements(By.CSS_SELECTOR, 'input[style="width:95%;padding:4px 0px 4px 5px;margin:4px 0px"]')[2]
date_input.send_keys('1990.09.09.')
time.sleep(1)

profession_input = browser.find_element(By.XPATH, '//input[@value="Automation Tester"]')
profession_input.click()
time.sleep(1)


flavours_input = browser.find_element(By.XPATH, '//input[@value="Selenium Webdriver"]')
flavours_input.click()
time.sleep(1)


continent_select = Select(browser.find_element(By.XPATH, '//select[@name="continents"]'))
continent_select.select_by_visible_text('Europe')
time.sleep(1)

command_select = Select(browser.find_element(By.XPATH, '//select[@name="selenium_commands"]'))
command_select.select_by_visible_text('WebElement Commands')
command_select.select_by_visible_text('Wait Commands')
time.sleep(2)

button_submit = browser.find_element(By.XPATH, '//button[@name="submit"]')
button_submit.click()

time.sleep(2)

actions.send_keys(Keys.ENTER)

time.sleep(1)

browser.quit()