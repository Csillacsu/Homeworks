import time

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

service = Service(executable_path=ChromeDriverManager().install())
options = Options()
options.add_experimental_option("detach", True)
options.add_argument('window-position=-1000,0')
browser = webdriver.Chrome(service=service, options=options)

URL = "http://selenium.oktwebs.training360.com/trickyelements.html"
browser.get(URL)
browser.maximize_window()

checkboxes = browser.find_elements(By.CLASS_NAME, 'switch')
for checkbox in checkboxes:
    checkbox.click()

time.sleep(1)

buttons = browser.find_elements(By.XPATH, '//form[@id="trickyForm"]/button')

for button in buttons:
    button.click()
    button_id = button.get_attribute('id')
    print(button_id)
    result = browser.find_element(By.ID, 'result')
    print(result.text)
    assert result.text == f"{button_id} was clicked"

browser.quit()
