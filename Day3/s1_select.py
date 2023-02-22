import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

service = Service(executable_path=r'/home/user/Asztal/chromedriver_linux64/chromedriver')
options = Options()
options.add_experimental_option("detach", True)
browser = webdriver.Chrome(service=service, options=options)

URL = 'https://letcode.in/dropdowns'
browser.get(URL)

select_fruit = Select(browser.find_element(By.ID, 'fruits'))
select_fruit.select_by_visible_text('Mango')

select_hero = Select(browser.find_element(By.ID, 'superheros'))
print(select_hero.is_multiple)
select_hero.select_by_value('ca')
select_hero.select_by_value('ds')
select_hero.deselect_by_value('ds')
select_hero.select_by_index('2')

# for hero in select_hero.options:
#     print(hero.text)

for hero in select_hero.all_selected_options:
    print(hero.text)

# select_hero.deselect_all()

print(select_hero.first_selected_option.text)
