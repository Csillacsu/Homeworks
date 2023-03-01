'''
Automatizáljuk le a játék kitöltését:
https://techstepacademy.com/trial-of-the-stones
'''

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

service = Service(executable_path=r'/home/user/Asztal/chromedriver_linux64/chromedriver')
options = Options()
options.add_experimental_option("detach", True)
browser = webdriver.Chrome(service=service, options=options)

URL = "https://techstepacademy.com/trial-of-the-stones"
browser.get(URL)

first_answer_input = browser.find_element(By.ID, 'r1Input')
first_answer_button = browser.find_element(By.ID, 'r1Btn')
first_answer_input.send_keys("rock")
first_answer_button.click()

second_word = browser.find_element(By.XPATH, '//div[@id="passwordBanner"]/h4')
second_answer_input = browser.find_element(By.ID, 'r2Input')
second_answer_button = browser.find_element(By.ID, 'r2Butn')
second_answer_input.send_keys(second_word.text)
second_answer_button.click()

first_name = browser.find_elements(By.XPATH, '//b')[0]
first_wealth = browser.find_elements(By.XPATH, '//b/../../p')[0]
second_name = browser.find_elements(By.XPATH, '//b')[1]
second_wealth = browser.find_elements(By.XPATH, '//b/../../p')[1]
third_answer_input = browser.find_element(By.ID, 'r3Input')
third_answer_button = browser.find_element(By.ID, 'r3Butn')

if int(first_wealth.text) < int(second_wealth.text):
    third_answer_input.send_keys(second_name.text)
else:
    third_answer_input.send_keys(first_name.text)

third_answer_button.click()

final_button = browser.find_element(By.ID, 'checkButn')
final_button.click()

complete_message = browser.find_element(By.XPATH, '//div[@id="trialCompleteBanner"]')

assert complete_message.text == "Trial Complete"

browser.quit()
