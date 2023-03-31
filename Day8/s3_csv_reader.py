import csv

# with open('movies.csv', 'r') as file:
#     movies_table = csv.reader(file, delimiter=',')
#     print(type(movies_table))
#     print(movies_table)
#     for row in movies_table:
#         # print(row)
#         # print(type(row))
#         print(row[0])
#         print(type(row[0]))

# titles = []
# with open('movies.csv', 'r') as file:
#     movies_table = csv.reader(file)
#     next(movies_table)
#     # next(movies_table)
#     for row in movies_table:
#         print(row)
#         titles.append(row[0])
#
# print(titles)

# directors = []
# with open('movies2.csv', 'r') as movies:
#     movies_table = csv.reader(movies, delimiter=';')
#     next(movies_table)
#     for row in movies_table:
#         print(row)
#     movies.seek(0)
#     next(movies_table)
#     for row in movies_table:
#         directors.append(row[1])
#
# print(directors)


########### Hotel
import time
import csv

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
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

login_btn = browser.find_element(By.CSS_SELECTOR, 'a[class="nav-link"]')
login_btn.click()
email_input = browser.find_element(By.ID, 'email')
password_input = browser.find_element(By.ID, 'password')
submit_btn = browser.find_element(By.CSS_SELECTOR, 'button[type="submit"]')

email_input.send_keys('ditoy18234@necktai.com')
password_input.send_keys('tesztelek2021')
submit_btn.click()

time.sleep(2)
profile = browser.find_element(By.CSS_SELECTOR, 'a[id="profile"]')
assert profile.text == "Profilom (Andrea)"

with open('room.csv', 'r') as rooms:
    room_reader = csv.reader(rooms, delimiter=',')
    next(room_reader)
    for room in room_reader:
        new_room_btn = WebDriverWait(browser, 5).until(EC.presence_of_element_located((By.XPATH, '//button[@class="btn btn-primary btn-lg btn-block"]')))
        new_room_btn.click()
        room_name_input = browser.find_element(By.ID, 'roomName')
        room_type = Select(browser.find_element(By.ID, 'roomType'))
        bed_nr = browser.find_element(By.ID, 'numberOfBeds')
        room_area = browser.find_element(By.ID, 'roomArea')
        price = browser.find_element(By.ID, 'pricePerNight')
        description = browser.find_element(By.ID, 'description')
        save_btn = browser.find_element(By.XPATH, '//button[@class="btn btn-primary my-buttons"]')

        room_name_input.send_keys(room[0])
        room_type.select_by_value(room[1])
        bed_nr.send_keys(room[2])
        room_area.send_keys(room[3])
        price.send_keys(room[4])
        description.send_keys(room[5])

        save_btn.click()

