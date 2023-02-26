import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

service = Service(executable_path='C:/Users/Csillacsu/OneDrive/Dokumentumok/Progmasters Automata tesztelő 2023/chromedriver_win32/chromedriver.exe')
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

email_input.send_keys('vbweutqiidxzvfpfcz@tmmcv.com')
password_input.send_keys('1234')

login_btn.click()


profile_id = WebDriverWait(browser, 5).until(EC.presence_of_element_located((By.ID, 'profile')))


# if profile_id.text == "Profilom (Péter)":
#     print("Login successful")
# else:
#     print("Login failed")

assert profile_id.text == "Profilom (Péter)"


hotel_list_btn = browser.find_element(By.XPATH, '//button[@class="btn btn-outline-primary btn-block"]')
hotel_list_btn.click()

search_btn = WebDriverWait(browser, 5).until\
    (EC.presence_of_element_located((By.XPATH, '//button[@class="btn btn-primary mr-4"]')))
assert search_btn.is_displayed()

time.sleep(3)

third_checkbox = browser.find_elements(By.XPATH, '//input[@type="checkbox"]')[2]
# assert third_checkbox.is_selected()
assert not third_checkbox.is_selected()
third_checkbox.click()
assert third_checkbox.is_selected()

guestnr_input = browser.find_element(By.ID, 'numberOfGuests')
assert guestnr_input.is_enabled()
# assert not guestnr_input.is_enabled()

hotel_name_list = browser.find_elements(By.XPATH, '//h4[@style="cursor: pointer"]')
print(len(hotel_name_list))
assert len(hotel_name_list) != 0
assert len(hotel_name_list) == 10

bucipanzio = browser.find_element(By.XPATH, '//h4[text()="buci panzió - panzió"]')
bucipanzio.click()

time.sleep(5)

babyfriendly = browser.find_elements(By.XPATH, '//li[@class="text-muted ng-star-inserted"]')[5]
assert babyfriendly.text == 'Bababarát szálláshely'
print(babyfriendly.text)

backtohotel_button = browser.find_element(By.XPATH, '//button[@class ="btn btn-outline-primary ng-star-inserted"]')
assert backtohotel_button.is_enabled()



# browser.quit()


