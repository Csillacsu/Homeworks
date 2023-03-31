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

# URL = "http://selenium.oktwebs.training360.com/kitchensink.html"
# browser.get(URL)
# browser.maximize_window()
#
# open_tab_btn = browser.find_element(By.ID, 'opentab')
# open_tab_btn.click()
#
# print(browser.window_handles)
# print(browser.title)
#
# main_tab = browser.window_handles[0]
# new_tab = browser.window_handles[1]
#
# browser.switch_to.window(new_tab)
# print(browser.title)

URL = "https://the-internet.herokuapp.com/windows"
browser.get(URL)
browser.maximize_window()

open_tab_link = browser.find_elements(By.TAG_NAME, 'a')[1]
open_tab_link.click()

main_tab = browser.window_handles[0]
new_tab = browser.window_handles[1]

print(browser.title)
browser.switch_to.window(new_tab)
print(browser.title)

# browser.close()
#
# browser.switch_to.window(main_tab)
# browser.close()

browser.switch_to.new_window()
browser.get("https://www.google.com")
print(browser.title)

# browser.execute_script('window.open("URL")')

browser.quit()
