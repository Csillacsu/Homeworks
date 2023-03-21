import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

service = Service(executable_path=ChromeDriverManager().install())
options = Options()
options.add_experimental_option("detach", True)
options.add_argument('window-position=-1000,0')
browser = webdriver.Chrome(service=service, options=options)

URL = "http://hotel-v2.progmasters.hu/"
browser.get(URL)
browser.maximize_window()

hotel_list_btn = browser.find_element(By.XPATH, '//button[@class="btn btn-outline-primary btn-block"]')
hotel_list_btn.click()
time.sleep(2)
# nav_links = WebDriverWait(browser, 5).until(EC.presence_of_all_elements_located((By.XPATH, '//a[@class="page-link"]')))
nav_links = browser.find_elements(By.XPATH, '//li[@class="page-item"]')
#
# for link in nav_links:
#     link.click()
#     print(browser.current_url)

next_button = nav_links[-1]
# print(next_button.text)

while next_button.get_attribute("class") != "page-item disabled":
    next_button.click()
    print(browser.current_url)
    time.sleep(1)

