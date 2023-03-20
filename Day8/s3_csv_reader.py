











########### Hotel
# import time
# import csv
#
# from selenium import webdriver
# from webdriver_manager.chrome import ChromeDriverManager
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.chrome.options import Options
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import Select
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.support.wait import WebDriverWait
#
#
# service = Service(executable_path=ChromeDriverManager().install())
# options = Options()
# options.add_experimental_option("detach", True)
#
# browser = webdriver.Chrome(service=service, options=options)
#
# URL = "http://hotel-v2.progmasters.hu/"
# browser.get(URL)
# browser.maximize_window()
#
# login_btn = browser.find_element(By.CSS_SELECTOR, 'a[class="nav-link"]')
# login_btn.click()
# email_input = browser.find_element(By.ID, 'email')
# password_input = browser.find_element(By.ID, 'password')
# submit_btn = browser.find_element(By.CSS_SELECTOR, 'button[type="submit"]')
#
# email_input.send_keys('ditoy18234@necktai.com')
# password_input.send_keys('tesztelek2021')
# submit_btn.click()
#
# time.sleep(2)
# profile = browser.find_element(By.CSS_SELECTOR, 'a[id="profile"]')
# assert profile.text == "Profilom (Andrea)"
