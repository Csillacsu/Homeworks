'''
Feladat: Ellenőrizzük le, hogy 5 + 5 eredménye 10 lesz!
Használjunk elágazást és írjunk ki a képernyőre egy az eredménynek megfelelő szöveget!
'''
from selenium import webdriver

from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

import time

PATH = "S:\oktatási anyagok\chromedriver.exe"
s = Service(executable_path=PATH)
o = Options()
o.add_experimental_option("detach", True)
browser = webdriver.Chrome(service=s, options=o)

URL = 'https://testpages.herokuapp.com/styled/calculator'
browser.get(URL)

first_inp = browser.find_element(By.ID, "number1")
second_inp = browser.find_element(By.ID, "number2")
cal_button = browser.find_element(By.ID, 'calculate')

first_inp.send_keys(5)
second_inp.send_keys(5)
cal_button.click()

result = browser.find_element(By.ID, 'answer')  # webelement
result_webelement_szoveg = browser.find_element(By.ID, 'answer').text
# if result_webelement_szoveg == 10:
#     print('OK')
# else:
#     print('Not OK')

print(result_webelement_szoveg)
print(type(result_webelement_szoveg))

if result_webelement_szoveg == str(10):
    print('OK')
else:
    print('Not OK')

browser.quit()


