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

URL = "http://selenium.oktwebs.training360.com/kitchensink.html"
browser.get(URL)
browser.maximize_window()

# alert_btn = browser.find_element(By.ID, 'alertbtn')
# alert_btn.click()
#
# alert_popup = browser.switch_to.alert
#
# assert alert_popup.text == "Hello , share this practice page and share your knowledge"
#
# alert_popup.accept()
#
# alert_btn.click()
# if EC.alert_is_present():
#     alert_popup = browser.switch_to.alert
#     assert alert_popup.text == "Hello , share this practice page and share your knowledge"
#     alert_popup.accept()
#     print("Alert accepted")
# else:
#     print("No alert present")

# confirm_btn = browser.find_element(By.ID, 'confirmbtn')
# confirm_btn.click()
#
# confirm_popup = browser.switch_to.alert
# time.sleep(2)
# # confirm_popup.accept()
# confirm_popup.dismiss()



