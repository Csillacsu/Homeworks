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

# guestnr = browser.find_element(By.NAME, 'numberOfGuests')
# guestnr.send_keys('2')

# guestnr2 = browser.find_element(By.TAG_NAME, 'input')
# guestnr2.clear()
# guestnr2.send_keys('3')
#
# input_fields = browser.find_elements(By.TAG_NAME, 'input')
# input_fields[0].clear()
# input_fields[0].send_keys('6')


