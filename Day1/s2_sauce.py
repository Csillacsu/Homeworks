import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By


s = Service(executable_path='S:\oktatási anyagok\chromedriver.exe')
o = Options()
o.add_experimental_option('detach', True)
browser = webdriver.Chrome(service=s, options=o)
browser.get('https://www.saucedemo.com/')

user_input = browser.find_element(By.ID, 'user-name')
user_input.send_keys('standard_user')

pw_input = browser.find_element(By.ID, 'password')
pw_input.send_keys('secret_sauce')

login_but = browser.find_element(By.ID, 'login-button')
login_but.click()

new_logged_url = browser.current_url

if new_logged_url != 'https://www.saucedemo.com/':
    print('Sikeres belépés')
else:
    print("Nem sikeres")

hamburger_menu_but = browser.find_element(By.ID, 'react-burger-menu-btn')
hamburger_menu_but.click()

time.sleep(2)

logut_but = browser.find_element(By.ID, 'logout_sidebar_link')
logut_but.click()

new_logged_out_url = browser.current_url

if new_logged_out_url == new_logged_url:
    print("Nem sikeres a kilépés")
else:
    print("Sikeres kilépés")

browser.quit()