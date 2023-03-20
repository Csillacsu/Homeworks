import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

service = Service(executable_path=r'/home/user/Asztal/chromedriver_linux64/chromedriver')
options = Options()
options.add_experimental_option("detach", True)
browser = webdriver.Chrome(service=service, options=options)

URL = "https://www.tutorialspoint.com/selenium/selenium_automation_practice.htm"
browser.get(URL)
browser.maximize_window()

time.sleep(2)

consent_btn = browser.find_element(By.CLASS_NAME, 'fc-button-label')
consent_btn.click()

time.sleep(2)

firstname_input = browser.find_element(By.NAME, 'firstname')
lastname_input = browser.find_element(By.XPATH, '//input[@name="lastname"]')
sex_female = browser.find_element(By.CSS_SELECTOR, 'input[value="Female"]')
exp_4 = browser.find_element(By.XPATH, '//input[@type="radio" and @value="4"]')
experience_radio = browser.find_elements(By.XPATH, '//input[@name="exp"]')
# date_input = browser.find_element(By.XPATH, '//strong[text()="Date:  "]/../../td/input')
date_input =browser.find_elements(By.XPATH, '//input[@type="text"]')[2]
prof_checkbox = browser.find_elements(By.XPATH, '//input[@name="profession"]')
selenium_check_webdriver = browser.find_element(By.XPATH, '//span[text()="  Selenium Webdriver"]/input')
continent_select = Select(browser.find_element(By.NAME, 'continents'))
command_select = Select(browser.find_element(By.NAME, 'selenium_commands'))
submit_btn = browser.find_element(By.CSS_SELECTOR, 'button[name="submit"]')


firstname_input.send_keys("Teszt")
lastname_input.send_keys("Teszt")
sex_female.click()

exp_4.click()
for years in experience_radio:
    years.click()

date_input.send_keys("2023")
prof_checkbox[1].click()
selenium_check_webdriver.click()
continent_select.select_by_index('1')
command_select.select_by_visible_text('Switch Commands')
submit_btn.click()
