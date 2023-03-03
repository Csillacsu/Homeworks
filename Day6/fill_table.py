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

URL = "http://selenium.oktwebs.training360.com/filltablewithsum.html"
browser.get(URL)
browser.maximize_window()

# # 1. verzió
product_input = browser.find_element(By.ID, 'product')
product_input.send_keys("ABC")
quantity_input = browser.find_element(By.ID, 'quantity')
quantity_input.send_keys("2")
price_input = browser.find_element(By.ID, 'price')
price_input.send_keys("23")
add_btn = browser.find_element(By.ID, 'add')
add_btn.click()
reset_btn = browser.find_element(By.ID, 'resetbtn')
reset_btn.click()
assert product_input.get_attribute("value") == ""
assert quantity_input.get_attribute("value") == ""
assert price_input.get_attribute("value") == ""
result_row = browser.find_elements(By.XPATH, '//table[@id="results"]/tbody/tr')[-1]
assert result_row.text == "ABC 2 23"

browser.quit()

# 2. verzió
# test_data = {
#     "product": "ABC",
#     "quantity": 2,
#     "price": 23
# }
#
#
# product_input = browser.find_element(By.ID, 'product')
# product_input.send_keys(test_data["product"])
# quantity_input = browser.find_element(By.ID, 'quantity')
# quantity_input.send_keys(test_data["quantity"])
# price_input = browser.find_element(By.ID, 'price')
# price_input.send_keys(test_data["price"])
# add_btn = browser.find_element(By.ID, 'add')
# add_btn.click()
# reset_btn = browser.find_element(By.ID, 'resetbtn')
# reset_btn.click()
# assert product_input.get_attribute("value") == ""
# assert quantity_input.get_attribute("value") == ""
# assert price_input.get_attribute("value") == ""
# result_row = browser.find_elements(By.XPATH, '//table[@id="results"]/tbody/tr')[-1]
# assert result_row.text == f"{test_data['product']} {test_data['quantity']} {test_data['price']}"
#
# browser.quit()


# # 3. verzió
# def fill_form(product_value, quantity_value, price_value):
#     product_input = browser.find_element(By.ID, 'product')
#     product_input.send_keys(product_value)
#     quantity_input = browser.find_element(By.ID, 'quantity')
#     quantity_input.send_keys(quantity_value)
#     price_input = browser.find_element(By.ID, 'price')
#     price_input.send_keys(price_value)
#     add_btn = browser.find_element(By.ID, 'add')
#     add_btn.click()
#     reset_btn = browser.find_element(By.ID, 'resetbtn')
#     reset_btn.click()
#     assert product_input.get_attribute("value") == ""
#     assert quantity_input.get_attribute("value") == ""
#     assert price_input.get_attribute("value") == ""
#     result_row = browser.find_elements(By.XPATH, '//table[@id="results"]/tbody/tr')[-1]
#     assert result_row.text == f"{product_value} {quantity_value} {price_value}"
#
#
# fill_form("G", 1, 32)
# fill_form("A", 4, 12)
#
# browser.quit()

# 4. verzió
# def fill_form(product_value, quantity_value, price_value):
#     product_input = browser.find_element(By.ID, 'product')
#     product_input.send_keys(product_value)
#     quantity_input = browser.find_element(By.ID, 'quantity')
#     quantity_input.send_keys(quantity_value)
#     price_input = browser.find_element(By.ID, 'price')
#     price_input.send_keys(price_value)
#     add_btn = browser.find_element(By.ID, 'add')
#     add_btn.click()
#     reset_btn = browser.find_element(By.ID, 'resetbtn')
#     reset_btn.click()
#     assert product_input.get_attribute("value") == ""
#     assert quantity_input.get_attribute("value") == ""
#     assert price_input.get_attribute("value") == ""
#     result_row = browser.find_elements(By.XPATH, '//table[@id="results"]/tbody/tr')[-1]
#     assert result_row.text == f"{product_value} {quantity_value} {price_value}"
#
#
# test_data = {
#     "product": "ABC",
#     "quantity": 2,
#     "price": 23
# }
#
# fill_form(test_data["product"], test_data["quantity"], test_data["price"])

## 5. verzió
# def fill_form(product_value, quantity_value, price_value):
#     product_input = browser.find_element(By.ID, 'product')
#     product_input.send_keys(product_value)
#     quantity_input = browser.find_element(By.ID, 'quantity')
#     quantity_input.send_keys(quantity_value)
#     price_input = browser.find_element(By.ID, 'price')
#     price_input.send_keys(price_value)
#     add_btn = browser.find_element(By.ID, 'add')
#     add_btn.click()
#     reset_btn = browser.find_element(By.ID, 'resetbtn')
#     reset_btn.click()
#     assert product_input.get_attribute("value") == ""
#     assert quantity_input.get_attribute("value") == ""
#     assert price_input.get_attribute("value") == ""
#     result_row = browser.find_elements(By.XPATH, '//table[@id="results"]/tbody/tr')[-1]
#     assert result_row.text == f"{product_value} {quantity_value} {price_value}"
#
#
# test_data = [{
#     "product": "ABC",
#     "quantity": 2,
#     "price": 23
# },
#     {
#     "product": "EFG",
#     "quantity": 3,
#     "price": 12
#     }
# ]
#
# for test_data in test_data:
#     fill_form(test_data["product"], test_data["quantity"], test_data["price"])
#
# browser.quit()
