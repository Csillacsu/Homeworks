'''
Feladat: Ellenőrizzük le, megfelelően történik-e a háromszög fajták meghatározása!
Használjunk elágazást és írjunk ki a képernyőre egy az eredménynek megfelelő szöveget!

https://testpages.herokuapp.com/styled/apps/triangle/triangle001.html
'''
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time

service = Service(executable_path=r'/home/user/Asztal/chromedriver_linux64/chromedriver')
options = Options()
options.add_experimental_option("detach", True)
browser = webdriver.Chrome(service=service, options=options)

URL = 'https://testpages.herokuapp.com/styled/apps/triangle/triangle001.html'
browser.get(URL)

s1_inp = browser.find_element(By.ID, 'side1')
s2_inp = browser.find_element(By.ID, 'side2')
s3_inp = browser.find_element(By.ID, 'side3')
button = browser.find_element(By.ID, 'identify-triangle-action')

# Teszt1
s1_inp.clear()
s1_inp.send_keys(5)
s2_inp.clear()
s2_inp.send_keys(5)
s3_inp.clear()
s3_inp.send_keys(5)
button.click()

if browser.find_element(By.ID, 'triangle-type').text == 'Equilateral':
    print('As expected')
else:
    print('Wrong result')

time.sleep(1)

# Teszt2
s1_inp.clear()
s1_inp.send_keys(5)
s2_inp.clear()
s2_inp.send_keys(5)
s3_inp.clear()
s3_inp.send_keys(6)
button.click()

if browser.find_element(By.ID, 'triangle-type').text == 'Isosceles':
    print('As expected')
else:
    print('Wrong result')

time.sleep(1)

# Teszt3
s1_inp.clear()
s1_inp.send_keys(3)
s2_inp.clear()
s2_inp.send_keys(4)
s3_inp.clear()
s3_inp.send_keys(5)
button.click()

if browser.find_element(By.ID, 'triangle-type').text == 'Scalene':
    print('As expected')
else:
    print('Wrong result')

time.sleep(1)

# Teszt4
s1_inp.clear()
s1_inp.send_keys(3)
s2_inp.clear()
s2_inp.send_keys(4)
s3_inp.clear()
s3_inp.send_keys(0)
button.click()

if 'Error' in browser.find_element(By.ID, 'triangle-type').text:
    print('As expected')
else:
    print('Wrong result')

time.sleep(1)

browser.quit()
