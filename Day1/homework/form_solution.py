'''
Feladat: Töltsük ki a form-ot python kód segítségével!
Szorgalmi: Próbáljuk meg beküldeni az adatokat!

https://testpages.herokuapp.com/styled/validation/input-validation.html
'''
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

PATH = '/home/user/Asztal/chromedriver_linux64/chromedriver'
s = Service(executable_path=PATH)
o = Options()
o.add_experimental_option("detach", True)
browser = webdriver.Chrome(service=s, options=o)

URL = 'https://testpages.herokuapp.com/styled/validation/input-validation.html'
browser.get(URL)

fname = browser.find_element(By.ID, 'firstname')
fname.send_keys('Eleonora')

lname = browser.find_element(By.ID, 'surname')
lname.send_keys('Tesztesetes')

age_field = browser.find_element(By.ID, 'age')
age_field.send_keys(20)

notes_field = browser.find_element(By.ID, 'notes')
notes_field.send_keys("nincs")

send_button = browser.find_element(By.XPATH, "//input[@type='submit']")
send_button.click()

result = browser.find_element(By.ID, 'valid-input-value').text
if result == 'Your Input passed validation':
    print('Passed')
else:
    print('Failed')

browser.quit()
