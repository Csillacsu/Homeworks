# Feladat: http://selenium.oktwebs.training360.com/another_form.html

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

service = Service(executable_path=ChromeDriverManager().install())
options = Options()
options.add_experimental_option("detach", True)

browser = webdriver.Chrome(service=service, options=options)
URL = "http://selenium.oktwebs.training360.com/another_form.html"
browser.get(URL)
browser.maximize_window()


## 1. verzió
# name_input = browser.find_element(By.ID, 'fullname')
# dob_input = browser.find_element(By.ID, 'dob')
# email_input = browser.find_element(By.ID, 'email')
# phone_input = browser.find_element(By.ID, "phone")
#
# name_input.send_keys("Andi")
# email_input.send_keys("test@test.hu")
#
# dob_input.send_keys('1999-01-04')
# # dob_input.send_keys('1999' + '1' + Keys.TAB + '4')
#
# phone_input.send_keys("01234 567890")
#
# submit_button = browser.find_element(By.ID, "submit")
# submit_button.click()
#
# result_row = WebDriverWait(browser, 5).until(EC.presence_of_all_elements_located((By.XPATH, '//table[@id="detailsTable"]/tbody/tr')))[-1]
# print(result_row.text)
#
# assert result_row.text == "Andi test@test.hu 1999-01-04 01234 567890 X"
#
# browser.quit()

## 2. verzió

# test_data = {
#     "name": "Andi",
#     "email": "test@test.hu",
#     "date": "1999-01-04",
#     "phone": "01234 567890"
# }
#
# name_input = browser.find_element(By.ID, 'fullname')
# dob_input = browser.find_element(By.ID, 'dob')
# email_input = browser.find_element(By.ID, 'email')
# phone_input = browser.find_element(By.ID, "phone")
#
# name_input.send_keys(test_data["name"])
# email_input.send_keys(test_data["email"])
# dob_input.send_keys(test_data["date"])
# phone_input.send_keys(test_data["phone"])
#
# submit_button = browser.find_element(By.ID, "submit")
# submit_button.click()
#
# result_row = WebDriverWait(browser, 5).until(EC.presence_of_all_elements_located((By.XPATH, '//table[@id="detailsTable"]/tbody/tr')))[-1]
# print(result_row.text)
#
# assert result_row.text == f"{test_data['name']} {test_data['email']} {test_data['date']} {test_data['phone']} X"

# browser.quit()

## 3. verzió
# def fill_form(name, email, date, phone):
#     name_input = browser.find_element(By.ID, 'fullname')
#     dob_input = browser.find_element(By.ID, 'dob')
#     email_input = browser.find_element(By.ID, 'email')
#     phone_input = browser.find_element(By.ID, "phone")
#
#     name_input.send_keys(name)
#     email_input.send_keys(email)
#     dob_input.send_keys(date)
#     phone_input.send_keys(phone)
#
#     submit_button = browser.find_element(By.ID, "submit")
#     submit_button.click()
#
#     result_row = WebDriverWait(browser, 5).until(
#         EC.presence_of_all_elements_located((By.XPATH, '//table[@id="detailsTable"]/tbody/tr')))[-1]
#     print(result_row.text)
#
#     assert result_row.text == f"{name} {email} {date} {phone} X"
#
# fill_form("Andi", "test@test.hu", "1999-01-04", "01234 567890")
# browser.quit()

## 4. verzió
# def fill_from (name, email, date, phone):
#     name_input = browser.find_element(By.ID, 'fullname')
#     dob_input = browser.find_element(By.ID, 'dob')
#     email_input = browser.find_element(By.ID, 'email')
#     phone_input = browser.find_element(By.ID, "phone")
#
#     name_input.send_keys(name)
#     email_input.send_keys(email)
#     dob_input.send_keys(date)
#     phone_input.send_keys(phone)
#
#     submit_button = browser.find_element(By.ID, "submit")
#     submit_button.click()
#
#     result_row = WebDriverWait(browser, 5).until(
#         EC.presence_of_all_elements_located((By.XPATH, '//table[@id="detailsTable"]/tbody/tr')))[-1]
#     print(result_row.text)
#
#     assert result_row.text == f"{name} {email} {date} {phone} X"
#
# test_data = {
#     "name": "Andi",
#     "email": "test@test.hu",
#     "date": "1999-01-04",
#     "phone": "01234 567890"
# }
#
# fill_from(test_data["name"], test_data["email"], test_data["date"], test_data["phone"])
# browser.quit()

## 5. verzió

def fill_from(name, email, date, phone):
    name_input = browser.find_element(By.ID, 'fullname')
    dob_input = browser.find_element(By.ID, 'dob')
    email_input = browser.find_element(By.ID, 'email')
    phone_input = browser.find_element(By.ID, "phone")

    name_input.clear()
    name_input.send_keys(name)
    email_input.clear()
    email_input.send_keys(email)
    dob_input.clear()
    dob_input.send_keys(date)
    phone_input.clear()
    phone_input.send_keys(phone)

    submit_button = browser.find_element(By.ID, "submit")
    submit_button.click()

    result_row = WebDriverWait(browser, 5).until(
        EC.presence_of_all_elements_located((By.XPATH, '//table[@id="detailsTable"]/tbody/tr')))[-1]
    print(result_row.text)

    assert result_row.text == f"{name} {email} {date} {phone} X"


test_data = [
    {
        "name": "Andi",
        "email": "test@test.hu",
        "date": "1999-01-04",
        "phone": "01234 567890"
    },
    {
        "name": "Bandi",
        "email": "test@elek.hu",
        "date": "2011-01-04",
        "phone": "02222 567890"
    }
]

for test_data in test_data:
    fill_from(test_data["name"], test_data["email"], test_data["date"], test_data["phone"])
# browser.quit()
