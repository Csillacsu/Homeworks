import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

URL = 'http://hotel-v2.progmasters.hu/'
service = Service(executable_path=r'/home/user/Asztal/chromedriver_linux64/chromedriver')
options = Options()
options.add_experimental_option("detach", True)
browser = webdriver.Chrome(service=service, options=options)

browser.get(URL)

### find by name
# guestnr = browser.find_element(By.NAME, 'numberOfGuests')
# guestnr.send_keys('2')

### find by tag name
# guestnr2 = browser.find_element(By.TAG_NAME, 'input')
# guestnr2.clear()
# guestnr2.send_keys('3')
#
# input_fields = browser.find_elements(By.TAG_NAME, 'input')
# input_fields[0].clear()
# input_fields[0].send_keys('6')

### find by link
# main_logo = browser.find_element(By.LINK_TEXT, 'Bejelentkezés')
# main_logo = browser.find_element(By.PARTIAL_LINK_TEXT, 'Bejel')
# main_logo.click()

### find by class
# login_btn = browser.find_element(By.CLASS_NAME, 'nav-link')
# login_btn = browser.find_elements(By.CLASS_NAME, 'nav-link')[1]
# login_btn.click()

### find by css selector
### Console: $$('a[class="nav-link"]')
login_btn = browser.find_element(By.CSS_SELECTOR, 'a[class="nav-link"]')
login_btn.click()

email_input = browser.find_element(By.ID, 'email')
password_input = browser.find_element(By.ID, 'password')

email_input.send_keys('andi.teszt2021@gmail.com')
password_input.send_keys('tesztelek2021')

# submit_btn = browser.find_element(By.NAME, 'submit')
submit_btn = browser.find_element(By.CSS_SELECTOR, 'button[name="submit"]')
submit_btn.click()

time.sleep(1)
logout_btn = browser.find_element(By.LINK_TEXT, 'Kilépés')

if logout_btn.text == "Kilépés":
    print("Boldogság van!")
else:
    print("Gikszer van")

### find by xpath
### Console: $x('//button[@class="btn btn-outline-primary btn-block"]')

hotel_list_btn = browser.find_element(By.XPATH, '//button[@class="btn btn-outline-primary btn-block"]')
hotel_list_btn.click()

time.sleep(1)
hotel_name_list = browser.find_elements(By.XPATH, '//h4[@style="cursor: pointer"]')
hotel_name = hotel_name_list[8]
print(hotel_name.text)

# Console: $x('//h4[text()="Kacsafészek - nyaraló"]')
kacsa_hotel = browser.find_element(By.XPATH, '//h4[text()="Kacsafészek - nyaraló"]')
print(kacsa_hotel.get_attribute('style'))

kacsa_div = browser.find_element(By.XPATH, '//h4[text()="Kacsafészek - nyaraló"]/../../..')
# kacsa_div = browser.find_element(By.XPATH, '//h4[text()="Kacsafészek - nyaraló"]/p/span')
print(kacsa_div.text)

