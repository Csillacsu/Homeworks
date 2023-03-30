'''
Feladat:
https://the-internet.herokuapp.com/iframe
Az oldalon található szövegszerkesztő kitöltésének automatizálása.
A beviteli mezőt a https://www.lipsum.com/ oldalon generált szöveggel töltsük ki (nyissuk meg új tabon az oldalt és másoljuk át a generált textet)

(segítség: a szövegszerkesztő beviteli mezője az adott frame body tag-jével azonosítható be)
'''

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
browser = webdriver.Chrome(service=service, options=options)

URL = "https://the-internet.herokuapp.com/iframe"
browser.get(URL)
main_tab = browser.window_handles[0]

browser.switch_to.new_window()
browser.get("https://www.lipsum.com/")

agree_btn = WebDriverWait(browser, 5).until(EC.presence_of_element_located((By.XPATH, '//button[@mode="primary"]')))
agree_btn.click()

amount_input = browser.find_element(By.ID, 'amount')
amount_input.clear()
amount_input.send_keys('15')

words_radio = browser.find_element(By.ID, 'words')
words_radio.click()

generate_btn = browser.find_element(By.ID, 'generate')
generate_btn.click()

lipsum = WebDriverWait(browser, 5).until(EC.presence_of_element_located((By.ID, 'lipsum'))).text

browser.close()
browser.switch_to.window(main_tab)

text_frame = browser.find_element(By.ID, 'mce_0_ifr')
browser.switch_to.frame(text_frame)

text_input = browser.find_element(By.TAG_NAME, 'body')
text_input.clear()
text_input.send_keys(lipsum)

browser.quit()
