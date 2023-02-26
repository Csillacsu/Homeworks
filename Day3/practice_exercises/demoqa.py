'''
https://demoqa.com/register
'''

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

URL = 'https://demoqa.com/register'
service = Service(executable_path=r'C:/Users/Csillacsu/OneDrive/Dokumentumok/Progmasters Automata tesztelő 2023/chromedriver_win32/chromedriver.exe')
options = Options()
options.add_experimental_option("detach", True)
browser = webdriver.Chrome(service=service, options=options)

browser.get(URL)
browser.maximize_window()

# first_name = browser.find_element(By.ID, 'firstname')
# first_name.send_keys("Kovács")
#
# last_name = browser.find_element(By.ID, 'lastname')
# last_name.send_keys("Béla")
#
# user_name = browser.find_element(By.ID, 'userName')
# user_name.send_keys("KGB")
#
# password = browser.find_element(By.ID, 'password')
# password.send_keys("KGB3la")
#
# reg_btn = browser.find_element(By.ID, 'register')
# reg_btn.click()
#
# error_msg = browser.find_element(By.ID, 'name')
# print(error_msg.text)
#
# if "Please verify reCaptcha to register!" == error_msg.text:
#     print("OK")
# else:
#     print("Fail")


first_name = browser.find_element(By.ID, 'firstname')
class_before_click = first_name.get_attribute('class')
print(class_before_click)
first_name.send_keys(Keys.PAGE_DOWN)

reg_btn = browser.find_element(By.ID, 'register')
reg_btn.click()

class_after_click = first_name.get_attribute('class')
print(class_after_click)

# if class_before_click == class_after_click:
#     print("Hiba")
# else:
#     print("Jó működés")

if "is-invalid" in class_after_click:
    print("Hibaüzenet megjelent")
