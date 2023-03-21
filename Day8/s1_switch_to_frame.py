from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.ui import Select


service = Service(executable_path=ChromeDriverManager().install())
options = Options()
options.add_experimental_option("detach", True)
options.add_argument('window-position=-1000,0')
browser = webdriver.Chrome(service=service, options=options)

# URL = "https://the-internet.herokuapp.com/nested_frames"
# browser.get(URL)
# # browser.maximize_window()
#
# top_frame = browser.find_element(By.NAME, 'frame-top')
# bottom_frame = browser.find_element(By.NAME, 'frame-bottom')
#
# browser.switch_to.frame(top_frame)
#
# left_frame = browser.find_element(By.NAME, 'frame-left')
# middle_frame = browser.find_element(By.NAME, 'frame-middle')
# right_frame = browser.find_element(By.NAME, 'frame-right')
#
# print(left_frame.get_attribute("src"))
# browser.switch_to.frame(left_frame)
# left_body = browser.find_element(By.XPATH, '//body')
# print(left_body.text)
#
# browser.switch_to.parent_frame()
# browser.switch_to.frame(right_frame)
# right_body = browser.find_element(By.TAG_NAME, 'body')
# print(right_body.text)
#
# browser.switch_to.parent_frame()
# browser.switch_to.frame(middle_frame)
# middle_body = browser.find_element(By.TAG_NAME, 'body')
# print(middle_body.text)
#
# browser.switch_to.parent_frame()
# browser.switch_to.parent_frame()
# browser.switch_to.frame(bottom_frame)
# bottom_body = browser.find_element(By.XPATH, '//body')
# print(bottom_body.text)
#
# browser.quit()

URL = "https://chercher.tech/practice/frames-example-selenium-webdriver"
browser.get(URL)

top_iframe = browser.find_element(By.ID, 'frame1')
bottom_iframe = browser.find_element(By.ID, 'frame2')

browser.switch_to.frame(top_iframe)
inner_iframe = browser.find_element(By.ID, 'frame3')

topic_input = browser.find_element(By.TAG_NAME, 'input')
topic_input.send_keys("Géza")

browser.switch_to.frame(inner_iframe)
checkbox = browser.find_element(By.ID, 'a')
checkbox.click()

browser.switch_to.parent_frame()
browser.switch_to.parent_frame()

browser.switch_to.frame(bottom_iframe)

select_animal = Select(browser.find_element(By.ID, 'animals'))
select_animal.select_by_value('babycat')

browser.quit()
