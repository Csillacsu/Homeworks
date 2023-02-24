import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

service = Service(executable_path=r'/home/user/Asztal/chromedriver_linux64/chromedriver')
options = Options()
options.add_experimental_option("detach", True)

browser = webdriver.Chrome(service=service, options=options)

URL = "http://hotel-v2.progmasters.hu/"
browser.get(URL)
browser.maximize_window()

signin_btn = browser.find_element(By.CSS_SELECTOR, 'a[class="nav-link"]')
signin_btn.click()

email_input = browser.find_element(By.ID, 'email')
password_input = browser.find_element(By.ID, 'password')
login_btn = browser.find_element(By.CSS_SELECTOR, 'button[name="submit"]')

email_input.send_keys('andi.teszt2021@gmail.com')
password_input.send_keys('tesztelek2021')

login_btn.click()

time.sleep(1)
profile_id = browser.find_element(By.ID, 'profile')

if profile_id.text == "Profilom (Andrea)":
    print("Login successful")
else:
    print("Login failed")

browser.quit()